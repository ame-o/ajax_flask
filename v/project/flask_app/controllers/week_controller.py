from flask import render_template, redirect, request,flash, session
from flask_app import app

from flask_app.models.vocab_model import Vocab
from flask_app.models.user_model import User

from flask_app.controllers import user_controller

@app.route('/hamburger')
def new_essay():
    return render_template("hamburger.html")