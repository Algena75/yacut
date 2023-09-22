from http import HTTPStatus
from urllib.parse import urljoin

from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import get_unique_short_id
from .validators import validate_custom_id, validate_url


@app.route('/api/id/', methods=['POST'])
def add_record():
    data = request.get_json()
    if data is None:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('\"url\" является обязательным полем!')
    url = validate_url(data['url'])
    if data.get('custom_id'):
        short_id = validate_custom_id(data.get('custom_id'))
        if URLMap.query.filter_by(short=short_id).first() is not None:
            raise InvalidAPIUsage(f'Имя "{short_id}" уже занято.')
    else:
        short_id = get_unique_short_id()
    new_record = URLMap(
        original=url,
        short=short_id
    )
    db.session.add(new_record)
    db.session.commit()
    return jsonify({
        'url': url,
        'short_link': urljoin('http://localhost/', short_id)
    }), HTTPStatus.CREATED


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_url(short_id):
    record = URLMap.query.filter_by(short=short_id).first()
    if record is None:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': record.original}), HTTPStatus.OK
