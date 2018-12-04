from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("home.html")


@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')


@app.route('/sign_in')
def sign_in():
    return render_template('sign_in.html')


@app.route('/myjourney')
def myjourney():
    return render_template('myjourney.html')


@app.route('/planner')
def planner():
    return render_template('planner.html')


@app.route('/petrol')
def petrol():
    return render_template('petrol.html')


@app.route("/shelter")
def shelter():
    return render_template("shelter.html")


@app.route('/weather')
def weather():
    return render_template('weather.html')


@app.route('/updates')
def updates():
    return render_template('updates.html')


@app.route('/camera')
def camera():
    return render_template('camera.html')


@app.route('/parking')
def parking():
    return render_template('parking.html')


@app.route('/S_parking')
def S_parking():
    return render_template('S_parking.html')


@app.route('/erp')
def erp():
    return render_template('erp.html')


if __name__ == "__main__":
    app.run(debug=True)
