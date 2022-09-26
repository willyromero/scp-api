from flask import Blueprint, render_template

main = Blueprint("home", __name__)

@main.route("/")
@main.route("/scp/api/")
def home():
    return render_template("home.html")