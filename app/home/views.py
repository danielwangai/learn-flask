from flask import abort, render_template
from flask_login import current_user, login_required


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

@home.route("/admin/dashboard")
@login_required
def admin_dashboard():
    """
    To render admin dashboard
    """
    if current_user.is_admin:
        return render_template("home/admin_dashboard.html", title="Admin Dashboard")

    abort(403)
