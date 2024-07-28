from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, SubmitField, SelectField, PasswordField
from wtforms.validators import DataRequired

class UsersForm(FlaskForm):
    id = StringField('Patient ID:', validators=[DataRequired()])
    date = DateField('Date Added:', validators=[DataRequired()])
    username = StringField('Username:', validators=[DataRequired()])
    fname = StringField('First Name:', validators=[DataRequired()])
    lname = StringField('Last Name:', validators=[DataRequired()])
    mname = StringField('Middle Name:', validators=[DataRequired()])
    address = StringField('Address:', validators=[DataRequired()])
    gender = SelectField('Gender:', choices=[('Male'), ('Female')], validators=[DataRequired()])
    mstatus = SelectField('Marital Status:', choices=[('Single'), ('Married'), ('Divorced'), ('Unmarried')], validators=[DataRequired()])
    bday = DateField('Birthday:', validators=[DataRequired()])
    age = IntegerField('Age:', validators=[DataRequired()])
    phid = StringField('PhilHealth ID:', validators=[DataRequired()])
    phone = StringField('Phone:', validators=[DataRequired()])
    email = StringField('Email:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    submit = SubmitField("Submit")  
    search = StringField('')

class RecordsForm(FlaskForm):
    name = StringField('Name:', validators=[DataRequired()])
    note = StringField('Note Type:', validators=[DataRequired()])
    doctor = StringField('Assigned Doctor:', validators=[DataRequired()])
    validated = StringField('Validated:', validators=[DataRequired()])
    date = StringField('Date Added:', validators=[DataRequired()])
    data = StringField('Record Copy:', validators=[DataRequired()])
    filename = StringField('File Name:', validators=[DataRequired()])
