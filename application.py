from sqlalchemy import ForeignKey, create_engine, inspect
import datetime
from flask import Flask, url_for, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
import pyodbc
import urllib.parse
import os
# Configure Database URI:
params = urllib.parse.quote_plus("Driver={ODBC Driver 17 for SQL Server};"
                                 "Server=tcp:lsdworld-server.database.windows.net,1433;"
                                 "Database=lsdworld_database;Uid=azureuser;"
                                 "Pwd={gHostbat9&};"
                                 "Encrypt=yes;"
                                 "TrustServerCertificate=no;"
                                 "Connection Timeout=30;")


# Initialization
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lsdworld_database.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
#extensions
conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
engine_azure = create_engine(conn_str, echo=True)
insp = inspect(engine_azure)
print(insp.get_table_names())
db = SQLAlchemy(app)


class user_profile(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    gender_identity = db.Column(db.String)
    phone_number = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True)
    city = db.Column(db.Text)
    tripsitter = db.Column(db.Boolean)
    safety_contact_name = db.Column(db.Text)
    safety_contact_phone_number = db.Column(db.Text)


class substance_table(db.Model):
    substance_id = db.Column(db.Integer, primary_key=True, nullable=False)
    substance_name = db.Column(db.Text, unique=True, nullable=False)
    category = db.Column(db.String)

def get_time():
    return datetime.datetime.utcnow()

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
    new_substance_name = request.form['substance_name']
    print(new_substance_name)
    #cursor.execute("INSERT INTO TRIP_REPORTS ("
   #                "trip_report_id,"
   #                "user_id,"
   #                "title,"
   #                "substance_id,"
   #                "report_content)"
   #                "VALUES(7,7, 'doeds it work 7', 0, 'sample report content' )")

    substance_id = substance_table.query.filter_by(
        substance_name=request.form['substance_name']
             ).first().substance_id
    print(substance_id)
    title = request.form['title']
    report_content = request.form['report_content']
    print(report_content)
    new_trip_report = trip_reports(
        trip_report_id=5,
        user_id=5,
        title=request.form['title'],
        substance_id=substance_id,
        report_content=request.form['report_content']
        )
    db.session.add(new_trip_report)
    db.session.commit()
    print("we finished method????")
    return redirect('submit_trip_report_page')

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


@app.route('/create_profile', methods=['GET','POST'])
def create_profile():
   return redirect('create_profile_page')

@app.route('/need_help', methods=['GET', 'POST'])
def need_help():
    return render_template('need_help.html')


# @app.route('/auth/logout')
# def auth_logout():
#    return render_template('auth.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
