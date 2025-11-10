from flask import render_template, Blueprint

methodology=Blueprint('methodology',__name__)

@methodology.route('/methodology')
def methodology_home():
  return render_template('methodology.html', title='methodology')

@methodology.route('/paper')
def paper():
    return render_template('buttons/paper.html')