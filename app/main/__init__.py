from flask import Blueprint


mainbp = Blueprint('mainbp', __name__)

from . import main