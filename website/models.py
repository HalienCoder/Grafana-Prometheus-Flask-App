from . import db #importing db from the current package
from flask_login import UserMixin #module to help with user authentication
from sqlalchemy.sql import func
 
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000), nullable=False)
    date = db.Column(db.DateTime(timezone = True), default = func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    firstName = db.Column(db.String(150), nullable=False)
    notes= db.relationship('Note') # whenever we create a note for that user, it will add the note id of that note to the user. This will be a list.

