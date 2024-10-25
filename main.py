    # Let's create a website with flask. This framewor will manage multiple html web pages.

from flask import (
    Flask,
    render_template,
)  # Flask is a class that create object instances.import
import pandas as pd


app = Flask(
    __name__
)  # create a variable where it can be executed when ir is called from the main program.

stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[
    ["STAID", "STANAME                                 "]
]  # display those 2 columns.


# Decorator app.route for the function home to call the home page when we access the url.
@app.route(
    "/"
)  # is a decorator that connect that method to the function above.
def home():
    return render_template(
        "home.html", data=stations.to_html()
    )  # home.html HAS to be inside the folder templates and the render_templates go to that folder and start the html file.
    # stations.to_html() is to give the structure of the html code. And inside the home.html we have to put |safe after data, to can see it in cells table form.


# Decorator app.route for the function api to call the page when that url is called.
@app.route(
    "/api/v1/<station>/<date>"
)  # with <station>/<date> user can change thore parameters.
def api(station, date):  # api funtion use those parameters.
    file_station = f"data_small/TG_STAID{str(station).zfill(6)}.txt"  # extract into file_station the station chosed by the user + zeros before until 6 digits in total.
    df = pd.read_csv(
        file_station, skiprows=20, parse_dates=["    DATE"]
    )  # read the csv file in base to that station chosed and get the info of date. parse_dates convert column DATE into a date format .
    temp = (
        df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10
    )  # we 'squeeze' TG column to extract that particular value for the station and date.
    return {
        "station": station,
        "date": date,
        "temperature": temp,
    }  # the function returns this dicctionari when the web page is called with those parameters.


# Decorator app.route for the function all_data to call the page when that url is called.
@app.route(
    "/api/v1/<station>"
)  # when it's called this show info about the station chosed (date and temperatures).
def all_data(station):
    file_station = f"data_small/TG_STAID{str(station).zfill(6)}.txt"
    df = pd.read_csv(file_station, skiprows=20, parse_dates=["    DATE"])
    result = df.to_dict(
        orient="records"
    )  # format de data frame to dictionary and with orient it turns on a list of diccionaries.
    return result


@app.route("/api/v1/yearly/<station>/<year>")
def yearly(station, year):
    file_station = f"data_small/TG_STAID{str(station).zfill(6)}.txt"
    df = pd.read_csv(file_station, skiprows=20)
    df["    DATE"] = df["    DATE"].astype(
        str
    )  # this convert DATE column from numbers to text, string.
    result = df[df["    DATE"].str.startswith(str(year))].to_dict(
        orient="records"
    )
    return result


if __name__ == "__main__":
    app.run(
        debug=True
    )  # we call the Flask app and with the debugger we can see erros on the nav window.
