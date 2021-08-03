# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import get_lunch_rating


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/homepage.html')
def index():
    return render_template("homepage.html")


@app.route('/aboutUs.html')
def aboutUs():
    return render_template("aboutUs.html")


@app.route('/apple')
def apple():
    return render_template("apple.html")


@app.route('/results', methods=["GET", "POST"])
def results():
    print(request.form["lunch"])
    user_lunch = request.form["lunch"]
    user_nickname = request.form["nickname"]
    lunch_rating = get_lunch_rating(user_lunch)
    if request.method == "POST":
        return render_template("/results.html", user_lunch=user_lunch, user_nickname=user_nickname, lunch_rating=lunch_rating)
    else:
        return "404 error"
