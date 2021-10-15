from flask import Flask, url_for,request, render_template
app = Flask(__name__)
@app.route('/')
def home_page():
    return render_template('layout_auth.html')
@app.route('/local_tripsitters')
def local_tripsitters():
    return render_template('local_tripsitters.html')
if __name__ == "__main__":
 	app.run(host="0.0.0.0", port=80)

#{% extends "templates/layout_auth.html" %}
#{{ super()}}