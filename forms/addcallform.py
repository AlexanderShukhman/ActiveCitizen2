from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired



class AddCallForm(FlaskForm):
    message = TextAreaField('Сообщение', validators=[DataRequired(message="Поле 'сообщение' не может быть пустым")])
    submit = SubmitField('Обработать сообщение')
