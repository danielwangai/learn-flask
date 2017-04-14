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


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle requests to the /login route
    Log an employee in through the login form
    """
    form = LoginForm()
    if form.validate_on_submit():
        employee = Employee.query.filter_by(email=form.email.data).first()
        if employee is not None and employee.verify_password(
                form.password.data):
            # log employee in
            login_user(employee)

            # redirect to the dashboard page after login
            return redirect(url_for('home.dashboard'))

            # when login details are incorrect
            else:
            flash('Invalid email or password.')

    # load login template
    return render_template('auth/login.html', form=form, title='Login')
