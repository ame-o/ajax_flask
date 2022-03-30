from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt= Bcrypt(app)

from flask_app.models import user_model

class Essay:
    def __init__(self,data):
        self.id = data["id"]
        self.title = data["title"]
        self.reading = data["reading"]
        self.prompt = data["prompt"]
        self.due_date = data["due_date"]
        self.user_id = data["user_id"]
        self.week_id = data["week_id"]