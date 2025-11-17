from flask_wtf import FlaskForm
from wtforms import  SubmitField,  SelectField,  FloatField
from wtforms.validators import InputRequired

class BusForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Diesel', 'Diesel')])
  days_used = SelectField(
    'Days used per week',
    choices=[(i, str(i)) for i in range(1, 8)],
    validators=[InputRequired()])
  submit = SubmitField('Submit')

class CarForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Electric', 'Electric')])
  days_used = SelectField(
    'Days used per week',
    choices=[(i, str(i)) for i in range(1, 8)],
    validators=[InputRequired()])
  submit = SubmitField('Submit')  

class PlaneForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Kerosene', 'Kerosene')])
  days_used = SelectField(
    'Days used per week',
    choices=[(i, str(i)) for i in range(1, 8)],
    validators=[InputRequired()])
  submit = SubmitField('Submit')
  
class FerryForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Diesel', 'Diesel')])
  days_used = SelectField(
    'Days used per week',
    choices=[(i, str(i)) for i in range(1, 8)],
    validators=[InputRequired()])
  submit = SubmitField('Submit')  

class MotorbikeForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel')])
  days_used = SelectField(
    'Days used per week',
    choices=[(i, str(i)) for i in range(1, 8)],
    validators=[InputRequired()])
  submit = SubmitField('Submit')

class BicycleForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Electric', 'Electric'), ('Normal', 'Normal')])
  days_used = SelectField(
    'Days used per week',
    choices=[(i, str(i)) for i in range(1, 8)],
    validators=[InputRequired()])
  submit = SubmitField('Submit')  

class WalkForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('No Fossil Fuel', 'No Fossil Fuel')])
  days_used = SelectField(
    'Days used per week',
    choices=[(i, str(i)) for i in range(1, 8)],
    validators=[InputRequired()])
  submit = SubmitField('Submit')  

class ScooterForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Electric', 'Electric')])
  days_used = SelectField(
    'Days used per week',
    choices=[(i, str(i)) for i in range(1, 8)],
    validators=[InputRequired()])
  submit = SubmitField('Submit')  

class TrainForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Diesel', 'Diesel'), ('Electric', 'Electric')])
  days_used = SelectField(
    'Days used per week',
    choices=[(i, str(i)) for i in range(1, 8)],
    validators=[InputRequired()])
  submit = SubmitField('Submit')