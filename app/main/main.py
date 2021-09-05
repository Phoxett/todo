from . import mainbp
from flask import render_template, request
from flask_login import login_required, login_user, logout_user
from ..model import User, List, Values, sqlalchemy as db


@mainbp.route('/')
def index():

    return render_template('index.html')


@mainbp.route('/join', methods=['POST', 'GET'])
def join():
    if request.method == 'POST':
        pass
    return render_template('join.html')