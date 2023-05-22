from flask import Blueprint

habit = Blueprint('habit',__name__)

from . import routes