from py4web.utils import url_signer
from sqlalchemy import ForeignKey, select, create_engine, Integer, String, insert, Column, MetaData, Table
from sqlalchemy.engine import URL
from py4web import URL
from sqlalchemy.orm import Session
import datetime
from flask import Flask, jsonify, url_for, request, render_template, redirect
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import pyodbc
import urllib.parse
from sqlalchemy.ext.declarative import declarative_base
# configuration
DEBUG = True
Base = declarative_base()


def get_time():
    return datetime.datetime.utcnow()

# Configure Database URI:
params = urllib.parse.quote_plus("Driver={ODBC Driver 18 for SQL Server};"
                                 "Server=tcp:lsdworld-server.database.windows.net,1433;"
                                 "Database=lsdworld_database_2023-06-02T15-39Z;"
                                 "Uid=azureuser;"
                                 "Pwd={gHostbat9&};"
                                 "Encrypt=yes;"
                                 "TrustServerCertificate=no;"
                                 "Connection Timeout=30;"
                                 )

# Initialization
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# extensions
CORS(app)
# CORS(app, resources={r'/*': {'origins': '*'}})
conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
engine_azure = create_engine(conn_str, echo=False)
db = SQLAlchemy(app)

meta = MetaData()

SUBSTANCES = Table('SUBSTANCES', meta,
                   Column('substance_id', Integer, primary_key=True, autoincrement=True),
                   Column('substance_name', String)
                   )
TRIP_REPORTS = Table('TRIP_REPORTS', meta,
                     Column('report_id', Integer, primary_key=True, autoincrement=True),
                     Column('substance_id', Integer),
                     Column('title', String),
                     Column('report_content', String),
                     # Column('diff_headspace',)
                     )
USER_PROFILE = Table('USER_PROFILE', meta,
                     Column('user_id', Integer, primary_key=True, autoincrement=True),
                     Column('user_name', String),
                     Column('user_phone_number', Integer),
                     Column('user_city', String),
                     Column('safety_contact_name', String),
                     Column('safety_contact_phone_number', String)
                     )
# magic happens at this line, where we create our sqlalchemy
# database in our azure cloud engine, so it is stored in azure cloud
meta.create_all(engine_azure)


@app.route('/', methods=['GET', 'POST'])
def layout():
    return render_template('layout_auth.html')


@app.route('/local_tripsitters', methods=['GET', 'POST'])
def local_tripsitters():
    return render_template('local_tripsitters.html')


@app.route('/submit_trip_report_page', methods=['GET', 'POST'])
def submit_trip_report_page():
    return render_template('submit_trip_report_form.html')


@app.route('/submit_trip_report', methods=['GET', 'POST'])
def submit_trip_report():
    # inserting into substances
    # insert_new_substance = insert(SUBSTANCES).values(
    #    substance_name=request.form['substance_name']
    # )
    # engine_azure.connect().execute(insert_new_substance)
    # this is me getting id of substance user entered
    sub_id_query = select(SUBSTANCES).where(
        SUBSTANCES.columns.substance_name ==
        request.form['substance_name'])
    substance_id_result = engine_azure.connect().execute(sub_id_query)
    new_substance_id = substance_id_result.first()[0]
    # inserting new trip report into database
    insert_trip_reports_4 = insert(TRIP_REPORTS).values(
        substance_id=new_substance_id,
        title=request.form['title'],
        report_content=request.form['report_content'],
    )
    with engine_azure.connect() as conn:
        conn.execute(insert_trip_reports_4)

    # return dict(fetch_profile_fields=URL('fetch_profile_fields', signer=url_signer))
    return redirect('submit_trip_report_page')


# fetched_trip_reports = ["Pikachu", "Charizard", "Squirtle", "Jigglypuff",
#             "Bulbasaur", "Gengar", "Charmander", "Mew", "Lugia", "Gyarados"]


# defining home page
@app.route('/home_page', methods=['GET', 'POST'])
def home_page():
    # sub_id_query = "SELECT * FROM TRIP_REPORTS"
    # fetched_trip_reports = engine_azure.connect().execute(sub_id_query)
    return render_template('home_page.html')
    # , fetched_trip_reports=fetched_trip_reports)


@app.route('/journey_safe_page', methods=['GET', 'POST'])
def journey_safe():
    return render_template('journey_safe_form.html')


@app.route('/map_page', methods=['GET', 'POST'])
def map_page():
    return render_template('map.html')

@app.route('/map_cont', methods=['GET', 'POST'])
def map_cont():
    return render_template('map_form.html')
    #return dict(map_cont=URL('map_cont', signer=url_signer))

# @app.route('/fetch_tags', methods=['GET', 'POST'])
# #@app.url_map('create_profile_page.html')
# def fetch_tags():
#     sub_id_query = select(SUBSTANCES).where(
#         SUBSTANCES.columns.substance_name ==
#         'marijuana')
#     substance_id_result = engine_azure.connect().execute(sub_id_query)
#     new_substance_id = substance_id_result.first()[0]
#     tags = ["ego death"],
#     #new_substance_id
#     return render_template('create_profile_form.html',
#                            tags=tags)


@app.route('/fetch_trip_reports', methods=['GET', 'POST'])
# @app.use
def fetch_trip_reports():
    # engine_azure.execute()
    # sub_id_query =  select(TRIP_REPORTS.columns.)
    # select(TRIP_REPORTS).where(
    #     TRIP_REPORTS.
    #     .columns.substance_name ==
    #     'marijuana')
    sub_id_query = select(TRIP_REPORTS).where(TRIP_REPORTS.columns.report_id == 9)
    trip_reports = engine_azure.connect().execute(sub_id_query)
    # new_substance_id = substance_id_results.first()[0]
    # fetched_trip_reports = new_substance_id
    return render_template('submit_trip_report_form.html',
                           trip_reports=trip_reports.report_ids,
                           trip_reports_title = trip_reports.title)


@app.route('/fetch_profile_fields', methods=['GET', 'POST'])
def fetch_profile_fields():
    sub_id_query = select(SUBSTANCES).where(
        SUBSTANCES.columns.substance_name ==
        'marijuana')
    substance_id_result = engine_azure.connect().execute(sub_id_query)
    new_substance_id = substance_id_result.first()[0]
    profile_fields = 55
    #new_substance_id
    return dict(profile_fields=profile_fields)


@app.route('/create_profile_page', methods=['GET', 'POST'])
def create_profile_page():
    return render_template('create_profile_form.html')


@app.route('/create_profile', methods=['GET', 'POST'])
def create_profile():
    user_name = request.form['user_name']
    user_phone_number = request.form['phone_number']
    user_city = request.form['city']
    user_safety_contact_name = request.form['safety_contact_name']
    user_safety_contact_phone_number = request.form['safety_contact_phone_number']
    return redirect('create_profile_page')


@app.route('/need_help', methods=['GET', 'POST'])
def need_help():
    return render_template('need_help.html')

# @app.route('/auth/logout')
# def auth_logout():
#    return render_template('auth.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)