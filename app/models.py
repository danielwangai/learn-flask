from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


class Employee(UserMixin, db.Model):
    """
    Define Employee attributes
    """
    # ensures pluralization of table
    __tablename__ = "employees"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25), index=True)
    last_name = db.Column(db.String(25), index=True)
    username = db.Column(db.String(30), index=True, unique=True)
    email = db.Column(db.String(80), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    is_admin = db.Column(db.Boolean, default=False)


    @property
    def password(self):
        """
        Prevent password from being accessed
        """
        raise AttributeError("Password is not a readable attribute.")


    @password.setter
    def password(self):
        """
        To hash passwords
        """
        self.password_hash = generate_password_hash(password)


    def verify_password(self):
        """
        Check if passwords match
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<Employee> - {}".format(self.username)

    @login_manager.user_loader
    def load_user(user_id):
        return Employee.query.get(int(user_id))


class Department(db.Model):
    """
    Define Department attributes
    """

    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    employees = db.relationship('Employee', backref='department',
                                lazy='dynamic')

    def __repr__(self):
        return '<Department: {}>'.format(self.name)
