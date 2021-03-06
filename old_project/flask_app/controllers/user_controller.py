from flask_app import app
from flask import render_template, redirect, request,flash, session
from flask import flash

from flask_app.models.user_model import User
from flask_app.models.vocab_model import Vocab

from flask_bcrypt import Bcrypt
bcrypt= Bcrypt(app) #use wherever you need it in there

from flask_app.controllers import vocab_controller
#IMPORTANT table 1 should be the table that has the info for the connection
# of one to many

#========================================================== 
# Index / Registration Form and Login Form
# =========================================================

@app.route('/')
def index():
    if "user_id" in session:
        return redirect('/dashboard')
    return render_template('index.html')


#========================================================== 
# Register Validation/ Create User --> send to database
# =========================================================

@app.route('/register', methods=['POST'])
def register():
#1 validate user
    if not User.validate_register(request.form):
        return redirect('/')
#2 collect data from html form
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data_query = {
            "username" : request.form['username'],
            "password" : pw_hash
        }
#3 run query to send form data to database
    user_id = User.create_instance(data_query)
    #3a putting user into session
    session['user_id'] = user_id
#4 redirect
    return redirect('/dashboard')

#========================================================== 
# Login Validation/ access User <-- from database
# =========================================================

@app.route('/login', methods=['POST'])
def login():
#1 validate user
    if not User.validate_login(request.form):
        return redirect("/")
#2 collect data from html form
    # query_data={
    #     "username" : request.form["username"]
    # }
#3 run query to send form data to database
    # logged_in = User.get_by_username(query_data)
#4 put ID into session
    # session['user_id'] = logged_in.id
#5 redirect
    return redirect('/dashboard')

#========================================================== 
# Dashboard / Validated User <-- from database
# =========================================================

@app.route('/dashboard')
def dashboard():
    # if "user_id" not in session:
    #     return redirect('/')
    # data_query = {
    #     "id": session["user_id"]
    # }
    # all_vocabs = Vocab.one_to_one()
    # logged_in = User.get_by_id(data_query)
    # logged_in=logged_in,, all_vocabs=all_vocabs
    return render_template("dashboard.html")


#========================================================== 
# edit existing user --> send to database
# =========================================================
@app.route('/user/account')
def form_edit_user():
    if "user_id" not in session:
        return redirect('/')
    data_query = {
        "id": session["user_id"]
    }
    logged_in = User.get_by_id(data_query)
    user_mags= User.user_magazines(data_query)
    print(user_mags)
    print(user_mags.magazines)
    return render_template("update_user.html", user_mags =user_mags,logged_in=logged_in)

@app.route('/user/account/process', methods = ['POST'])
def process_edit_user():
    data = {
        "id": session["user_id"],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "username": request.form["username"]
    }
    print(data)
    User.edit_instance(data)
    return redirect ("/dashboard")


#========================================================== 
# DELETE existing user --> send to database
# =========================================================
@app.route('/delete/<int:id>')
def delete(id):
    query_data = {
        "id" :id
    }
    Magazine.delete_instance(query_data)
    return redirect('/dashboard')

#========================================================== 
# Logout / Clear Session
# =========================================================
@app.route('/logout')
def logout():
    session.clear()
    return redirect("/")



# #========================================================== 
# # Show All User's vocabs  / One to Many
# # =========================================================

@app.route('/myvocab')
def show_user_vocabs():
    # if "user_id" not in session:
    #     return redirect('/')
    # data_query = {
    #     "id": session["user_id"]
    # }
    # logged_in = User.get_by_id(data_query)
    # all_vocab = User.user_vocab(data_query)
    # return render_template("user_vocab.html", logged_in=logged_in,all_vocab=all_vocab)
    return render_template("user_vocab.html")