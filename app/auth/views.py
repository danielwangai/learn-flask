from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import auth
from forms import LoginForm, RegistrationForm
from .. import db
from ..models import Employee


@auth.route("/register", methods=["GET", "POST"])
def register():
    """
    Handle account creation requests
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        employee = Employee(email=form.email,
                            username=form.username,
                            first_name=form.first_name,
                            last_name=form.last_name,
                            password=form.password
                            )
        # add employee to database
        db.session.add(employee)
        db.session.commit()
        flash("Registration successful. You can now login.")

        # redirect to login page
        return redirect(url_for("auth.login"))
