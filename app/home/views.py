from flask import render_template
from flask_login import login_required


from . import home

@home.route("/")
def homepage():
    """
    Render home page of the site
    """
    return render_template("home/index.html", title="Welcome")


@home.route("/dashboard")
@login_required
def dashboard():
    """
    Render landing page after successfull login
    """
    return render_template("home/dashboard.html", title="Dashboard")
