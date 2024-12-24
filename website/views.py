from flask import Blueprint, render_template
# we are going to define tha this file here is the Blueprint of our appplication which means that it has a bunch of routes and urls defined inside of it.
#its a way to seperate our app out so we dont have to have all of our views defined in one file, we can have them in different files. split them up into different files. 

views = Blueprint('views', __name__)
# this is the blueprint of our application. we are going to define all of our routes and urls inside of this blueprint. we are going to call it views. we are going to pass in the name of the file that this blueprint is in. which is __name__ which is a python variable that holds the name of the current file.

#this function will run whenever we go to the defined route

@views.route('/')
def home():
    return render_template("home.html")

#we have these blueprints registered, but we need to register these blueprints to the init.py file. we need to tell flask that we have a blueprint that we want to register.