from flask import Flask, url_for,request, render_template

app = Flask(__name__)
@app.route('/')
def hello():
    return "LSD WORLD is the networking app for psychonauts"
@app.route('/index', methods=['GET','POST'])
def index():
    return render_template('local_tripsitters.html')
if __name__ == "__main__":
 	app.run(host="0.0.0.0", port=80)