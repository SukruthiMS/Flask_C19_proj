from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/prediction")
def prediction():    
    return render_template("prediction.html")

@app.route("/world")
def world():
    return render_template("world.html")


@app.route("/india", methods = ["POST", "GET"])
def india():

    from data_render import daywise_data_india
    india_plot_daywise_data = daywise_data_india()
    day = india_plot_daywise_data[0]
    confirmed = india_plot_daywise_data[1]
    deaths = india_plot_daywise_data[2]

    from data_render import statewise_analysis
    statewise_data = statewise_analysis()

    india_data_url = "https://disease.sh/v2/countries/India?yesterday=true&strict=true"
    india_content = requests.get(india_data_url)
    india_data = india_content.json()

    #from data_render import district_zone_analysis
    #states_district_zone_data = district_zone_analysis()
    #district_data = states_district_zone_data

    return render_template("india.html", data = india_data, day = day, confirmed = confirmed, deaths = deaths, states = statewise_data)


@app.route("/map")
def map():
    return render_template("map.html")

@app.route("/karnataka")
def karnataka():
    return render_template("karnataka.html")

@app.route("/countries")
def countries():
    return render_template("countries.html")


@app.route("/vaccination")
def vaccination():
    return render_template("vaccination.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/article")
def article():
    return render_template("article.html")

if __name__ == "__main__":
    app.run(debug = True)