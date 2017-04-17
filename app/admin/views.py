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
