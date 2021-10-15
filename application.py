from flask import Flask, url_for,request, render_template
app = Flask(__name__)
@app.route('/')
def hello():
    return "LSD WORLD is the networking app for psychonauts" \
           "Also, Julian Hodge is so damn sexy"
@app.route('/local_tripsitters', methods=['GET','POST'])
def index():
    return render_template('local_tripsitters.html')
    #return render_template('local_tripsitters.html')
if __name__ == "__main__":
 	app.run(host="0.0.0.0", port=80)

#{% extends "templates/layout_auth.html" %}
#{{ super()}}