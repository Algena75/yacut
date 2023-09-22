from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional, Regexp

PATTERN = r'^[0-9A-Za-z]+$'


class AddURLForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле'),
                    URL()]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[Length(1, 16, message='Длина не превышает 16 символов'),
                    Optional(strip_whitespace=True),
                    Regexp(PATTERN, message='Недопустимые символы')]
    )
    submit = SubmitField('Создать')
