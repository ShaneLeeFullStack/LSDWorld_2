# py4web~=1.20210602.1
# pydal~=20210215.1
from textFunc import rivers_func

from flask import Flask, url_for, request, render_template, redirect


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template('layout_auth.html')


@app.route('/local_tripsitters', methods=['GET', 'POST'])
def local_tripsitters():
    return render_template('local_tripsitters.html')


@app.route('/submit_trip_report_page', methods=['GET', 'POST'])
def submit_trip_report_page():
    return render_template('submit_trip_report_form.html')


@app.route('/submit_trip_report', methods=['POST'])
def submit_trip_report():
    redirect('submit_trip_report_page')


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
    app.run(host="0.0.0.0", port=80)

# {% extends "templates/layout_auth.html" %}
# {{ super()}}
