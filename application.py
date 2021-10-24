from sqlalchemy import ForeignKey, create_engine, inspect, insert
import datetime
from flask import Flask, url_for, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
import pyodbc
import urllib.parse

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
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# extensions
conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
engine_azure = create_engine(conn_str, echo=True)
db = SQLAlchemy(app)


def get_time():
    return datetime.datetime.utcnow()


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
    # substance_id = dbo.SUBSTANCE_TABLE.query.filter_by(
    #    substance_name=request.form['substance_name']
    # ).first().substance_id
    # print(substance_id)
    title = request.form['title']
    report_content = request.form['report_content']
    engine_azure.execute("SET IDENTITY_INSERT dbo.TRIP_REPORTS ON")
    engine_azure.execute("INSERT INTO TRIP_REPORTS ("
                         "report_id,"
                         "user_id,"
                         "title,"
                         "substance_id,"
                         "substance_name,"
                         "report_content)"
                         "VALUES(1,12, 'second title' , 4,  'marijuana','first report content')")
    db.session.commit()
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


@app.route('/create_profile', methods=['GET', 'POST'])
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
