
from flask import Flask, make_response
from flask import Flask, make_response,jsonify
from flask_migrate import Migrate

from models import db, Earthquake
def index():
    return make_response(body, 200)