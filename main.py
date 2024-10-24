    # Let's create a website with flask. This framewor will manage multiple html web pages.

from flask import Flask, render_template  # Flask is a class that create object instances.import

app = Flask(__name__)  # create a variable where

@app.route("/")  # is a decorator that connect that method to the function above.
def home():
    return render_template("home.html")  # init_tutorial HAS to be inside the folder templates and the render_templates go to that folder and iniate the html file.

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)  # we call the Flask app and with the debugger we can see erros on the nav window.