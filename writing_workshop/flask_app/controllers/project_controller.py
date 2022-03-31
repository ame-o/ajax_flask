from flask import render_template, redirect, request,flash, session
from flask_app import app

from flask_app.models.vocab_model import Vocab
from flask_app.models.user_model import User
from flask_app.models.week_model import Weekly

from flask_app.controllers import user_controller

#==========================================================
#   Misc
# =========================================================
@app.route('/cinderella')
def this_week():
    return render_template("cinderella.html")

@app.route('/hamburger')
def new_essay():
    if "user_id" not in session:
        return redirect('/')
    data_query = {
        "id": session["user_id"]
    }
    data = {
        "id": int(1)
    }
    logged_in = User.get_by_id(data_query)
    week= Weekly.get_one_instance(data)
    return render_template("hamburger.html",logged_in=logged_in,weekly=week)

@app.route('/lost')
def lost():
    return render_template('lost.html')