from flask import render_template, Blueprint, request, redirect, url_for, flash
from capp.models import Transport
from capp import db
from datetime import timedelta, datetime, date
from flask_login import login_required, current_user
from capp.carbon_app.forms import BusForm, CarForm, PlaneForm, FerryForm, MotorbikeForm, BicycleForm, ScooterForm, TrainForm

carbon_app=Blueprint('carbon_app',__name__)

#Emissions factor per transport in kg per passenger km
#Data from: http://efdb.apps.eea.europa.eu/?source=%7B%22query%22%3A%7B%22match_all%22%3A%7B%7D%7D%2C%22display_type%22%3A%22tabular%22%7D
efco2={'Bus':{'Diesel':0.08},
    'Car':{'Petrol':0.122,'Diesel':0.148,'Electric':0},
    'Plane':{'Kerosene':0.225},
    'Ferry':{'Diesel':0.267},
    'Motorbike':{'Petrol':0.112,'Diesel':0.089},
    'Scooter':{'Electric':0.034},
    'Bicycle':{'Normal':0.0,'Electric':0.03},
    'Walk':{'No Fossil Fuel':0},
    'Train':{'Diesel':0.063,'Electric':0.005}}

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
        days_used = form.days_used.data
        transport = 'Car'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]

        co2 = float("{:.2f}".format(co2))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, days_used=days_used, author=current_user)
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
        days_used = form.days_used.data
        transport = 'Bus'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]

        co2 = float("{:.2f}".format(co2))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, days_used=days_used, author=current_user)
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
        days_used = form.days_used.data
        transport = 'Plane'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]

        co2 = float("{:.2f}".format(co2))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, days_used=days_used, author=current_user)
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
        days_used = form.days_used.data
        transport='Train'

        co2 = float(kms) * efco2[transport][fuel]

        co2 = round(co2, 2)

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, days_used=days_used, author=current_user)
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
        days_used = form.days_used.data
        transport = 'Scooter'

        co2 = float(kms) * efco2[transport][fuel]

        co2 = round(co2, 2)

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, days_used=days_used, author=current_user)
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
        days_used = form.days_used.data
        transport = 'Bicycle'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]

        co2 = float("{:.2f}".format(co2))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, days_used=days_used, author=current_user)
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
        days_used = form.days_used.data
        transport = 'Ferry'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]

        co2 = float("{:.2f}".format(co2))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, days_used=days_used, author=current_user)
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
        days_used = form.days_used.data
        transport = 'Motorbike'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]

        co2 = float("{:.2f}".format(co2))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, days_used=days_used, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template("carbon_app/motorbike_emission.html", form=form)

@carbon_app.route('/carbon_app/your_data')
@login_required
def your_data():
    entries = Transport.query.filter_by(author=current_user). \
        order_by(Transport.date.desc()).order_by(Transport.transport.asc()).all()

    # 2️⃣ Preparazione dati per i grafici
    vehicle_labels = []       # Pie chart: tipi di veicolo
    vehicle_totals = []       # Pie chart: totale emissioni per veicolo

    weekly_labels = []        # Bar chart: etichette veicolo + carburante
    weekly_emissions = []     # Bar chart: emissioni settimanali

    for e in entries:
        # --- PIE CHART ---
        if e.transport not in vehicle_labels:
            vehicle_labels.append(e.transport)
            vehicle_totals.append(float(e.co2))
        else:
            index = vehicle_labels.index(e.transport)
            vehicle_totals[index] += float(e.co2)

        # --- BAR CHART ---
        weekly_labels.append(f"{e.transport} ({e.fuel})")
        weekly_emissions.append(float(e.co2) * int(e.days_used))

    return render_template('carbon_app/your_data.html', title='your_data', entries=entries, vehicle_labels=vehicle_labels, vehicle_totals=vehicle_totals, weekly_labels=weekly_labels, weekly_emissions=weekly_emissions)

#Delete emission
@carbon_app.route('/carbon_app/delete-emission/<int:entry_id>')
def delete_emission(entry_id):
    entry = Transport.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for('carbon_app.your_data'))
    
