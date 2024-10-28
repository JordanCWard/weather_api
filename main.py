# Import flask to use multiple HTML web pages
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


# the next line is connected to home function because of the @ symbol
@app.route("/")
def home():
    return render_template("home.html")


# Special syntax around station and date
@app.route("/api/v1/<station>/<date>")
def about(station, date):

    # zfill adds zeros on the left till we have a 6-digit number
    filename = "weather_station_data/TG_STAID" + str(station).zfill(6) + ".txt"

    # Skip 20 rows because tables start at line 20 in each file
    weather_data = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = weather_data.loc[weather_data['    DATE'] == date]['   TG'].squeeze() / 10


    return {"station": station,
            "date": date,
            "temperature": temperature}


# Only runs the website if this script is run directly from this file
if __name__ == "__main__":
    # Adding debug=True allows us to see errors on the web page
    app.run(debug=True)
