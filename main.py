    # Let's create a website with flask. This framewor will manage multiple html web pages.

from flask import Flask, render_template  # Flask is a class that create object instances.import
import pandas as pd


app = Flask(__name__)  # create a variable where it can be executed when ir is called from the main program.

stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]  # display those 2 columns.

@app.route("/")  # is a decorator that connect that method to the function above.
def home():
    return render_template("home.html", data=stations.to_html())  # home.html HAS to be inside the folder templates and the render_templates go to that folder and start the html file.
                                                                                      # stations.to_html() is to give the structure of the html code. And inside the home.html we have to put |safe after data, to can see it in cells table form.

@app.route("/api/v1/<station>/<date>")   # with <station>/<date> user can change thore parameters.
def api(station, date):                  # api funtion use those parameters.
    file_station = f"data_small/TG_STAID{str(station).zfill(6)}.txt"       # extract into file_station the station chosed by the user + zeros before until 6 digits in total.
    df = pd.read_csv(file_station, skiprows=20, parse_dates=['    DATE'])  # read the csv file with the station and date for that station chosed.
    temp = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10          # we 'squeeze' TG column to extract that particular value for the station and date.
    return {"station": station,
            "date": date,
            "temperature": temp}         # the function returns this dicctionari when the web page is called with those parameters.


if __name__ == "__main__":
    app.run(debug=True)  # we call the Flask app and with the debugger we can see erros on the nav window.