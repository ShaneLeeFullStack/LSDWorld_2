# py4web~=1.20210602.1
# pydal~=20210215.1
from sqlalchemy import ForeignKey

from textFunc import rivers_func
import datetime
from flask import Flask, url_for, request, render_template, redirect
import sqlite3 as sql
from flask_sqlalchemy import SQLAlchemy

# define connection and cursor
#connection = sql.connect('LSDWorld_DATABASE.sqlite')
#cursor = connection.cursor()

#cursor.execute(command1)

def get_time():
    return datetime.datetime.utcnow()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lsdworld_database.db'
db = SQLAlchemy(app)


class user_profile(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    gender_identity = db.Column(db.String)
    phone_number = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String,unique=True)
    city = db.Column(db.Text)
    tripsitter = db.Column(db.Boolean)
    safety_contact_name = db.Column(db.Text)
    safety_contact_phone_number = db.Column(db.Text)

class substance_table(db.Model):
    substance_id = db.Column(db.Integer, primary_key=True, nullable=False)
    substance_name = db.Column(db.Text, unique=True, nullable=False)
    category = db.Column(db.String)

class trip_reports(db.Model):
    trip_report_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Text, default=get_time())
    user_id = db.Column(db.Integer, db.ForeignKey('user_profile.user_id'),
                        nullable=False)
    title = db.Column(db.Text)
    substance_id = db.Column(db.Integer, db.ForeignKey('substance_table.substance_id'),
                             nullable=False)
    report_content = db.Column(db.Text)
    diff_headspace = db.Column(db.Boolean)
    anti_depressants = db.Column(db.Boolean)
    at_festival = db.Column(db.Boolean)
    is_showing = db.Column(db.Integer, db.ForeignKey('trip_reports.trip_report_id'))

class text_analysis(db.Model):
    id = db.Column(db.Integer, ForeignKey(trip_reports.trip_report_id), primary_key=True)
    user_profile_id = db.Column(db.Integer, db.ForeignKey('user_profile.user_id'))
    tags = db.Column(db.String)


@app.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template('layout_auth.html')


@app.route('/local_tripsitters', methods=['GET', 'POST'])
def local_tripsitters():
    return render_template('local_tripsitters.html')


@app.route('/submit_trip_report_page', methods=['GET', 'POST'])
def submit_trip_report_page():
    return render_template('submit_trip_report_form.html')


@app.route('/submit_trip_report', methods=['GET', 'POST'])
def submit_trip_report():
    #substance_array = substance_table.select()
    #substance_name = request.params.get('substance_name')
    new_substance_name = request.form['substance_name']
    print(new_substance_name)
    substance_row = db.select(substance_table.substance_name == new_substance_name)
    print(substance_row)
    return redirect('submit_trip_report_page')
    #return render_template('submit_trip_report_form.html')


# @app.route('/home_page', methods =['GET', 'POST'])
# def home_page():
#    return render_template('index.html')
@app.route('/journey_safe_page', methods=['GET', 'POST'])
def journey_safe():
    return render_template('journey_safe_form.html')


@app.route('/map_page', methods=['GET', 'POST'])
def map_page():
    return render_template('map_form.html')


@app.route('/create_profile_page', methods=['GET', 'POST'])
def create_profile_page():
    return render_template('create_profile_form.html')


@app.route('/need_help', methods=['GET', 'POST'])
def need_help():
    return render_template('need_help.html')


# @app.route('/auth/logout')
# def auth_logout():
#    return render_template('auth.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)


# {% extends "templates/layout_auth.html" %}
# {{ super()}}
