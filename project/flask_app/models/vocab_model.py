from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt= Bcrypt(app)

from flask_app.models import user_model

class Vocab:
    def __init__(self,data):
        self.id = data["id"]
        self.spelling = data["spelling"]
        self.definition = data["definition"]
        self.sentence = data["sentence"]
        self.user_id = data["user_id"]
        self.week_id = data["week_id"]

# =========================================================
    #Static Methods
# =========================================================
    @staticmethod
    def validate_add(form_data):
        is_valid = True
        if len(form_data['spelling']) < 2:
            flash("Genre must be at least 2 characters")
            is_valid=False
        if len(form_data['definition']) < 2:
            flash("City must be at least 2 characters")
            is_valid=False
        return is_valid

    # @staticmethod
    # def validate_login(form_data):
    #     #1st check: does this user exist in the db?
    #     is_valid = True
    #     user_in_db = user_model.User.get_by_email(form_data)
    #     #if not, let them know
    #     if not user_in_db:
    #         flash("Invalid Email/Password")
    #         is_valid = False
    #     #check password matches what is in db
    #     if not bcrypt.check_password_hash(user_in_db.password,form_data['password']):
    #         flash("Invalid Email/Password")
    #         is_valid = False

    #     return is_valid


# =========================================================
    #get all instances in bands and users <- from database
# =========================================================
    @classmethod
    def one_to_one(cls):
        query = """SELECT * FROM vocabulary
        JOIN users ON users.id= vocabulary.user_id;"""
        results = connectToMySQL("writingworkshop").query_db(query)
        all_all = []
        for dic in results:
            vocab_data = {
                "id" : dic["id"],
                "spelling" : dic["spelling"],
                "definition" : dic["definition"],
                "sentence" : dic["sentence"],
                "due_date" : dic["due_date"],
                "user_id" : dic["user_id"],
                "week_id" : dic["week_id"]
            }
            vocab = cls(vocab_data)
            user_data = {
                "id" : dic['user_id'],
                "first_name" : dic['first_name'],
                "last_name" : dic['last_name'],
                "email" : dic['email'],
                "password" : dic['password'],
                "created_at" : dic['users.created_at'],
                "updated_at" : dic['users.updated_at'],
            }
            vocab.user = user_model.User(user_data)
            all_all.append(vocab)
        return all_all
    # @classmethod
    # def get_all(cls):
    #     query = "SELECT * FROM vocabulary JOIN users ON vocabulary.user_id = users.id;"
    #     results = connectToMySQL("writingworkshop").query_db(query)
    #     all_magazines = []
    #     if results:
    #         for dict in results:
    #             all_magazines.append(cls(dict))
    #     return all_magazines


# =========================================================
    #Get an instance <- send to database
# =========================================================

    @classmethod
    def get_one_instance(cls,data):
        query = "SELECT * FROM vocabulary JOIN users ON vocabulary.user_id = users.id WHERE vocabulary.id = %(id)s;"
        results = connectToMySQL("writingworkshop").query_db(query, data)
        if results:
            vocabulary= cls(results[0])
            vocabulary.creator = user_model.User(results[0])
            return vocabulary
# =========================================================
    #create new instance of a band
# =========================================================
    @classmethod
    def create_instance(cls,data):
        query = "INSERT INTO vocabulary (spelling, definition, sentence, due_date, user_id, week_id) VALUES (%(spelling)s,%(definition)s,%(due_date)s,%(user_id)s,%(week_id)s)"
        results = connectToMySQL("writingworkshop").query_db(query, data)
        return results

# =========================================================
    # edit one instance in band -> send to database
# =========================================================
    @classmethod
    def edit_instance(cls,data):
        query = "UPDATE vocabulary SET spelling=%(spelling)s, definition=%(definition)s,due_date=%(due_date)s,user_id=%(user_id)s,week_id=%(week_id)s WHERE id = %(id)s;"
        return connectToMySQL("writingworkshop").query_db(query,data)


# =========================================================
    #delete an instance in band -> send to database
# =========================================================
    @classmethod
    def delete_instance(cls,data):
        query = "DELETE FROM vocabulary WHERE id = %(id)s;"
        return connectToMySQL("writingworkshop").query_db(query,data)
