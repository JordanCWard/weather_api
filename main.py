# Import flask to use multiple HTML web pages
from flask import Flask, render_template

app = Flask("Website")


# the next line is connected to home function because of the @ symbol
@app.route("/home")
def home():
    return render_template("tutorial.html")


@app.route("/about")
def about():
    return render_template("about.html")


# Adding debug=True allows us to see errors on the web page
app.run(debug=True)
