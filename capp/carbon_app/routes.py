from flask import render_template, Blueprint, request, redirect, url_for, flash
from capp.models import Transport
from capp import db
from datetime import timedelta, datetime, date
from flask_login import login_required, current_user
from capp.carbon_app.forms import BusForm, CarForm, PlaneForm, FerryForm, MotorbikeForm, BicycleForm, ScooterForm, TrainForm

carbon_app=Blueprint('carbon_app',__name__)

#Emissions factor per transport in kg per passenger km
#Data from: http://efdb.apps.eea.europa.eu/?source=%7B%22query%22%3A%7B%22match_all%22%3A%7B%7D%7D%2C%22display_type%22%3A%22tabular%22%7D
efco2={'Bus':{'Diesel':0.67,'Electric':0.16},
    'Car':{'Petrol':0.125,'Diesel':0.127,'Electric':0.65},
    'Plane':{'Kerosene':0.225},
    'Ferry':{'Diesel':0.267},
    'Motorbike':{'Petrol':0.112,'Diesel':0.89},
    'Scooter':{'Electric':0.60},
    'Bicycle':{'Normal':0.07,'Electric':0.17},
    'Walk':{'No Fossil Fuel':0},
    'Train':{'Diesel':0.63,'Electric':0.2075}}

@carbon_app.route('/carbon_app')
@login_required
def carbon_app_home():
    return render_template('carbon_app/carbon_app.html')

@carbon_app.route("/tutorial")
def tutorial():
    return render_template("carbon_app/tutorial.html")

@carbon_app.route("/car-emission", methods=['GET','POST'])
@login_required
def car_emission():
    form = CarForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Car'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]

        co2 = float("{:.2f}".format(co2))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template("carbon_app/car_emission.html", form=form)

@carbon_app.route("/bus-emission", methods=['GET','POST'])
@login_required
def bus_emission():
    form = BusForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Bus'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]

        co2 = float("{:.2f}".format(co2))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template("carbon_app/bus_emission.html", form=form)

@carbon_app.route("/plane-emission", methods=['GET','POST'])
@login_required
def plane_emission():
    form = PlaneForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Plane'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]

        co2 = float("{:.2f}".format(co2))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template("carbon_app/plane_emission.html", form=form)

@carbon_app.route("/train-emission", methods=['GET','POST'])
@login_required
def train_emission():
    form=TrainForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport='Train'

        co2 = float(kms) * efco2[transport][fuel]

        co2 = round(co2, 2)

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template("carbon_app/train_emission.html", form=form)

@carbon_app.route("/scooter-emission", methods=['GET','POST'])
@login_required
def scooter_emission():
    form = ScooterForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Scooter'

        co2 = float(kms) * efco2[transport][fuel]

        co2 = round(co2, 2)

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template("carbon_app/scooter_emission.html", form=form)


@carbon_app.route("/bicylce-emission", methods=['GET','POST'])
@login_required
def bicycle_emission():
    form = BicycleForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Bicycle'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]

        co2 = float("{:.2f}".format(co2))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template("carbon_app/bicycle_emission.html", form=form)

@carbon_app.route("/ferry-emission", methods=['GET','POST'])
@login_required
def ferry_emission():
    form = FerryForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Ferry'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]

        co2 = float("{:.2f}".format(co2))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template("carbon_app/ferry_emission.html", form=form)

@carbon_app.route("/motorbike-emission", methods=['GET','POST'])
@login_required
def motorbike_emission():
    form = MotorbikeForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Motorbike'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]

        co2 = float("{:.2f}".format(co2))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template("carbon_app/motorbike_emission.html", form=form)

@carbon_app.route('/carbon_app/your_data')
@login_required
def your_data():
    #Table
    entries = Transport.query.filter_by(author=current_user). \
        filter(Transport.date> (datetime.now() - timedelta(days=5))).\
        order_by(Transport.date.desc()).order_by(Transport.transport.asc()).all()
    return render_template('carbon_app/your_data.html', title='your_data', entries=entries)

#Delete emission
@carbon_app.route('/carbon_app/delete-emission/<int:entry_id>')
def delete_emission(entry_id):
    entry = Transport.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for('carbon_app.your_data'))
    