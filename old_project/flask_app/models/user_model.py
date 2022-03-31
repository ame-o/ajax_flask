from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt= Bcrypt(app)

from flask_app.models import vocab_model

class User:
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.username = data["username"]
        self.password = data["password"]


# =========================================================
    #Validations
# =========================================================

    @staticmethod
    def validate_register(form_data):
        is_valid = True
        # if len(form_data['first_name']) < 3:
        #     flash("First name must be at least 2 characters")
        #     is_valid=False
        # if len(form_data['username']) < 3:
        #     flash("First name must be at least 2 characters")
        #     is_valid=False
        # if len(form_data['password']) < 8:
        #     flash("Password must be at least 8 characters")
        #     is_valid=False
        # if form_data['password'] != form_data['con_password']:
        #     flash("Passwords don't match")
        #     is_valid=False
        print(form_data)
        return is_valid

    @staticmethod
    def validate_login(form_data):
        #1st check: does this user exist in the db?
        is_valid = True
        # user_in_db = User.get_by_username(form_data)
        # #if not, let them know
        # if not user_in_db:
        #     flash("Invalid /Password")
        #     is_valid = False
        # #check password matches what is in db
        # elif not bcrypt.check_password_hash(user_in_db.password,form_data['password']):
        #     flash("Invalid /Password")
        #     is_valid = False
        print(form_data)
        return is_valid

# =========================================================
        #Class Methods
# =========================================================
    #get only 1 instance in user <- from database
# =========================================================
    @classmethod    
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL("writingworkshop").query_db(query, data)
        return cls(results[0])
    
    @classmethod    
    def get_by_username(cls, data):
        # query = "SELECT * FROM users WHERE username = %(username)s;"
        # results = connectToMySQL("writingworkshop").query_db(query, data)
        # if len(results) < 1:
        #     return False
        # return cls(results[0])
        print(data)

# =========================================================
    #create a new instance in user -> send to database
# =========================================================
    @classmethod
    def create_instance(cls,data):
        #create new instances of user class linked to database
        query = "INSERT INTO users (first_name,username, password) VALUES (%(first_name)s,%(username)s,%(password)s)"
        results = connectToMySQL("writingworkshop").query_db(query, data)
        return results

# =========================================================
    # edit one instance in user -> send to database
# =========================================================
    @classmethod
    def edit_instance(cls,data):
        query = "UPDATE users SET username=%(username)s, updated_at=NOW() WHERE id = %(id)s;"
        results= connectToMySQL("writingworkshop").query_db(query,data)
        if len(results) < 1:
            return False
        return results


# =========================================================
    #join one to all
# =========================================================
    # @classmethod
    # def user_bands(cls,data):
    #     query = """SELECT * FROM users 
    #     JOIN bands ON users.id= bands.user_id
    #     WHERE users.id = %(id)s;"""
    #     results = connectToMySQL("writingworkshop").query_db(query,data)
    #     if len(results) < 1:
    #         return False
    #     user = cls(results[0])
    #     for dic in results:
    #         band_data = {
    #             "id" : dic["bands.id"],
    #             "name" : dic["name"],
    #             "genre" : dic["genre"],
    #             "city" : dic["city"],
    #             "user_id" : dic["user_id"],
    #             "created_at" : dic['bands.created_at'],
    #             "updated_at" : dic['bands.updated_at'],
    #         }
    #         band_instance = band_model.Band(band_data)
    #         user.bands.append(band_instance)
    #     return user


