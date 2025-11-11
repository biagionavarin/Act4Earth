from flask import render_template, Blueprint

home=Blueprint('home',__name__)

@home.route('/')
@home.route('/home')
def home_home():
  return render_template('home.html')

@home.route('/meet_us')
def meet_us():
    return render_template('buttons/meet_us.html')

@home.route('/cbnapp')
def cbnapp():
    return render_template('buttons/cbnapp.html')