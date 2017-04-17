from flask import abort, flash, render_template, redirect, url_for
from flask_login import login_required, current_user

from . import admin
from forms import DepartmentForm
from .. import db
from ..models import Department


def check_admin():
    """
    prevent non admins from accessing this page
    """
    if not current_user.is_admin:
        # forbidden error
        abort(403)


# department views

@admin.route('/departments', methods=['GET', 'POST'])
@login_required
def list_departments():
    """
    list all departments
    """
    check_admin()

    # get all department objects
    departments = Department.query.all()

    return render_template('admin/departments/departments.html',
                           departments=departments, title='Departments')


@admin.route('/departments/add', methods=['GET', 'POST'])
@login_required
def add_department():
    """
    To add a department
    """
    check_admin()

    add_department = True

    form = DepartmentForm
    if form.validate_on_submit():
        department = Department(name=form.name.data,
                                description=form.description.data)

        try:
            # add department to database
            db.session.add(department)
            db.session.commit()
            flash('You have successfully added a new department.')
        except:
            # in case department name already exists
            flash('Department name already exists')
        return redirect(url_for('admin.list_departments'))

    return render_template("admin/departments/department.html", action='Add',
                           add_department=add_department, form=form,
                           title="Add Department")

@admin.route('/admin/departments/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_department(id):
    """
    Edit a department
    """
    check_admin()

    add_department = False

    department = Department.query.get_or_404(id)

    form = DepartmentForm(obj=department)
    if form.validate_on_submit():
        department.name = form.name.data
        department.description = form.description.data
        db.session.commit()
        flash("You've successfully edited the department.")
        return redirect(url_for("admin.list_departments"))

    form.name.data = department.name
    form.description.data = department.description

    return render_template("admin/departments/department", action="Edit",
                           add_department=add_department, form=form,
                           department=department, title="Edit Department")
