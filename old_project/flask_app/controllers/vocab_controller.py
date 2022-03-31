from flask import render_template, redirect, request,flash, session
from flask_app import app

from flask_app.models.vocab_model import Vocab
from flask_app.models.user_model import User

from flask_app.controllers import user_controller
#use wherever you need it in there

#========================================================== 
#Create New vocab --> send to database
# =========================================================

@app.route('/view/vocab/')
def this_week_vocab():
    return render_template('week_vocab.html')


@app.route('/new/vocab')
def new_vocab():
#     if "user_id" not in session:
#         return redirect('/')
#     user_id = session["user_id"]
#     query_data = {
#         "id": session["user_id"]
#     }
#     logged_in = User.get_by_id(query_data)
#     return render_template('add_vocab.html',user_id=user_id,logged_in=logged_in)
    return render_template('add_vocab.html')
# =========================================================
@app.route('/new/vocab/process', methods = ['POST'])
def create_vocab():
    if not Vocab.validate_add(request.form):
        return redirect("/new/sighting")
    query_data = {
                "spelling" : request.form["spelling"],
                "definition" : request.form["definition"],
                "sentence" : request.form["sentence"],
                "due_date" : request.form["due_date"],
                "user_id" : request.form["user_id"],
                "week_id" : request.form["week_id"]
            }
    Vocab.create_instance(query_data)
    return redirect("/dashboard") 

#========================================================== 
# edit existing vocab --> send to database
# =========================================================
@app.route('/edit/vocab/')#<int:id>
def form_edit_vocab(): #id
    # if "user_id" not in session:
    #     return redirect('/')
    # user_id = session["user_id"]
    # query_data = {
    #     "id": session["user_id"]
    # }
    # logged_in = User.get_by_id(query_data)
    # data = {
    #     "id" : id
    # }
    # one_vocab= Vocab.get_one_instance(data)
    # return render_template('update_vocab.html',user_id=user_id,logged_in=logged_in,one_vocab=one_vocab)
    return render_template('update_vocab.html')
#========================================================== 
@app.route('/edit/vocab/process', methods = ['POST'])
def process_edit_vocab():
    if not Vocab.validate_add(request.form):
        id = int(request.form['id'])
        return redirect(f"/edit/{id}")
    query_data = {
                "id" : request.form["id"],
                "spelling" : request.form["spelling"],
                "definition" : request.form["definition"],
                "sentence" : request.form["sentence"],
                "due_date" : request.form["due_date"],
                "user_id" : request.form["user_id"],
                "week_id" : request.form["week_id"]
    }
    Vocab.edit_instance(query_data)
    return redirect ("/dashboard")

#========================================================== 
# delete existing vocab --> send to database
# =========================================================
@app.route('/delete/vocab/<int:id>')
def delete_vocab(id):
    data = {
        "id" : id
    }
    Vocab.delete_instance(data)
    return redirect("/dashboard")