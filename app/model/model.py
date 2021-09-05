from re import L
from .. import sqlalchemy
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_login import UserMixin


class User(sqlalchemy.Model, UserMixin):
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(20))
    surname = sqlalchemy.Column(sqlalchemy.String(20))
    username = sqlalchemy.Column(sqlalchemy.String(20))
    password = sqlalchemy.Column(sqlalchemy.String(100))
    email = sqlalchemy.Column(sqlalchemy.String(100))
    lists = sqlalchemy.relationship('List', backref='lists', lazy=True)

    def set_password(self, password):
        self.password = generate_password_hash(password, 'sha256', 32)
    
    def check_password(self, password):
        return check_password_hash(password, password)


class List(sqlalchemy.Model):
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    title = sqlalchemy.Column(sqlalchemy.String(20))
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('user.id'), nullable=False)
    values = sqlalchemy.relationship('Values', backref='lists', lazy=True)


class Values(sqlalchemy.Model):
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    value = sqlalchemy.Column(sqlalchemy.String(40))
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('list.id'), nullable=False)

class Key(sqlalchemy.Model):
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    url = sqlalchemy.Column(sqlalchemy.String(40))
    secret_key = sqlalchemy.Column(sqlalchemy.String(40))
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('list.id'), nullable=False)
    joins = sqlalchemy.relationship('Join', backref='joins', lazy=True)

class Join(sqlalchemy.Model):
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    user_key = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('key.secret_key'), nullable=False)