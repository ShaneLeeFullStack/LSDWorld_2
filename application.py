#py4web~=1.20210602.1
#pydal~=20210215.1
from common import db,  auth
from textFunc import rivers_func

from flask import Flask, url_for,request, render_template, redirect
def get_user_id():
    user_id = db(db.user_profile.email == auth.current_user.get('email')).select()
    return user_id[0].id
app = Flask(__name__)
@app.route('/', methods =['GET', 'POST'])
def home_page():
    return render_template('layout_auth.html')
@app.route('/local_tripsitters', methods =['GET', 'POST'])
def local_tripsitters():
    return render_template('local_tripsitters.html')
@app.route('/submit_trip_report_page', methods =['GET', 'POST'])
def submit_trip_report_page():
    return render_template('submit_trip_report_form.html')
@app.route('/submit_trip_report', methods=['POST'])
def submit_trip_report():
    substance_array = db(db.substance_table).select()
    substance_name = request.params.get('substance_name')
    substance_row = db(db.substance_table.substance_name ==
                       substance_name).select()
    substance_id = substance_row[0].id
    title = request.params.get('title')
    report_content = request.params.get('report_content')
    dif_headspace = request.params.get('dif_headspace')
    anti_depress = request.params.get('anti_depress')
    at_festival = request.params.get('at_festival')
    new_trip_report_id = db.trip_reports.insert(title=title,
                                                substance_id=substance_id,
                                                user_id=get_user_id(),
                                                report_content=report_content,
                                                difficult_headspace=dif_headspace,
                                                anti_depressants=anti_depress,
                                                at_festival=at_festival,
                                                )
    newest_trip_report = db.trip_reports[new_trip_report_id]
    analyze_this_content = newest_trip_report.report_content
    tags_list = rivers_func(analyze_this_content)
    new_id = db.text_analysis.insert(id=new_trip_report_id,
                                     user_profile_id=get_user_id(),
                                     tags=tags_list)
    redirect('submit_trip_report_page')
#@app.route('/home_page', methods =['GET', 'POST'])
#def home_page():
#    return render_template('index.html')
@app.route('/journey_safe_page', methods =['GET', 'POST'])
def journey_safe():
    return render_template('journey_safe_form.html')
@app.route('/map_page', methods =['GET', 'POST'])
def map_page():
    return render_template('map_form.html')
@app.route('/create_profile_page', methods =['GET', 'POST'])
def create_profile_page():
    return render_template('create_profile_form.html')
@app.route('/need_help', methods =['GET', 'POST'])
def need_help():
    return render_template('need_help.html')
#@app.route('/auth/logout')
#def auth_logout():
#    return render_template('auth.html')
if __name__ == "__main__":
 	app.run(host="0.0.0.0", port=80)

#{% extends "templates/layout_auth.html" %}
#{{ super()}}