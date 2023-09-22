from flask import flash, redirect, render_template

from . import app, db
from .forms import AddURLForm
from .models import URLMap
from .utils import get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = AddURLForm()
    if form.validate_on_submit():
        original_link = form.original_link.data
        if form.custom_id.data and form.custom_id.data.strip() != '':
            short_url = form.custom_id.data
            if URLMap.query.filter_by(short=short_url).first() is not None:
                flash(f'Имя {short_url} уже занято!')
                return render_template('main.html', form=form)
        else:
            form.custom_id.data = get_unique_short_id()
        new_record = URLMap(
            original=original_link,
            short=form.custom_id.data
        )
        db.session.add(new_record)
        db.session.commit()
        flash('Ваша новая ссылка готова:')

    return render_template('main.html', form=form)


@app.route('/<short_url>')
def redirect_func(short_url):
    page = URLMap.query.filter_by(short=short_url).first_or_404()
    return redirect(page.original)
