from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextField
from wtforms.validators import DataRequired, EqualTo, Email

#registerform inherits from flask form AND WILL HAVE ALL IT'S METHODS
class PhoneBook(FlaskForm):
    
    name = StringField('Full Name', validators=[DataRequired()])
    phone_number = IntegerField('Phone Number', validators=[DataRequired()])
    address = TextField('Full Address', validators=[DataRequired()])
    submit = SubmitField()
