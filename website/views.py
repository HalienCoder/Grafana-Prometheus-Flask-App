from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from .models import Note
from . import db
import json

# we are going to define tha this file here is the Blueprint of our appplication which means that it has a bunch of routes and urls defined inside of it.
#its a way to seperate our app out so we dont have to have all of our views defined in one file, we can have them in different files. split them up into different files. 

views = Blueprint('views', __name__)
# this is the blueprint of our application. we are going to define all of our routes and urls inside of this blueprint. we are going to call it views. we are going to pass in the name of the file that this blueprint is in. which is __name__ which is a python variable that holds the name of the current file.

#this function will run whenever we go to the defined route

@views.route('/', methods =['GET', "POST"])
@login_required
def home():
    if request.method =='POST':
        note =request.form.get('note')

        if len(note) < 1:
            flash ("Note is too short!", category='error')
        else:
            new_note =Note(data=note, user_id = current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash ("Note added!", category='success')
    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods =['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note.get('noteID')
    note= Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})

#we have these blueprints registered, but we need to register these blueprints to the init.py file. we need to tell flask that we have a blueprint that we want to register.