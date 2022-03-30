from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt= Bcrypt(app)

from flask_app.models import student_model

class Weekly:
    def __init__(self,data):
        self.id = data["id"]
        self.vocab_done = data["vocab_done"]
        self.vocab_story = data["vocab_story"]
        self.hamburger_1 = data["hamburger_1"]
        self.hamburger_2 = data["hamburger_2"]
        self.essay_1 = data["essay_1"]
        self.essay_2 = data["essay_2"]
        self.project_done = data["project_done"]
        self.student_id = data["student_id"]
        self.week_id = data["week_id"]

# =========================================================
    #Static Methods
# =========================================================

# =========================================================
    #Get an instance <- send to database
# =========================================================

    @classmethod
    def get_one_instance(cls,data):
        query = "SELECT * FROM weekly JOIN students ON weekly.user_id = students.id WHERE weekly.id = %(id)s;"
        results = connectToMySQL("writingworkshop").query_db(query, data)
        if results:
            weekly= cls(results[0])
            weekly.creator = student_model.Student(results[0])
            return weekly
# =========================================================
    #create new instance of a band
# =========================================================
    @classmethod
    def create_instance(cls,data):
        query = "INSERT INTO weekly (spelling, definition, sentence, due_date, user_id, week_id) VALUES (%(spelling)s,%(definition)s,%(due_date)s,%(user_id)s,%(week_id)s)"
        results = connectToMySQL("writingworkshop").query_db(query, data)
        return results

# =========================================================
    # edit one instance in band -> send to database
# =========================================================
    @classmethod
    def edit_instance(cls,data):
        query = "UPDATE weekly SET spelling=%(spelling)s, definition=%(definition)s,due_date=%(due_date)s,user_id=%(user_id)s,week_id=%(week_id)s WHERE id = %(id)s;"
        return connectToMySQL("writingworkshop").query_db(query,data)


# =========================================================
    #delete an instance in band -> send to database
# =========================================================
    @classmethod
    def delete_instance(cls,data):
        query = "DELETE FROM weekly WHERE id = %(id)s;"
        return connectToMySQL("writingworkshop").query_db(query,data)
