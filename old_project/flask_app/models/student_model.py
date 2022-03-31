from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt= Bcrypt(app)

from flask_app.models import vocab_model

class Student:
    def __init__(self,data):
        self.id = data["id"]
        self.username = data["username"]
        self.password = data["password"]


# =========================================================
    #Validations
# =========================================================