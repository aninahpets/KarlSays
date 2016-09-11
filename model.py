from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import session, flash
import bcrypt

db = SQLAlchemy()

class User(db.Model):
    """User of the app."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(75), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(75), nullable=False)


    @classmethod
    def log_user_in(cls, username, password):
        # retrieves user object from database
        user = User.query.filter_by(username=username).first()
        if user == None:
            return False

        # logs current user out if session exists
        if 'user_id' in session:
            del session['user_id']

        # checks for password match and creates new session if successful
        if bcrypt.checkpw(password, user.password):
        # if user.password == password:
            session['user_id'] = user.user_id
            return True

        # redirects to login page if unsuccessful
        else:
            return False

    @classmethod
    def log_user_out(cls):
        # remove user session and confirm user logout
        del session['user_id']

    @classmethod
    def create_user(cls, username, password):

        # hash and salt user pw
        password = bcrypt.hashpw(password, bcrypt.gensalt())

        # create new user record and add to database
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        session['user_id'] = new_user.user_id

    @classmethod
    def user_logged_in(cls):
        if 'user_id' in session:
            return True
        return False


class Park(db.Model):
    """Parks in SF."""

    __tablename__ = 'parks'

    park_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    park_name = db.Column(db.String, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    neighborhood = db.Column(db.String, nullable=False)


def connect_to_db(app, db_uri='postgresql:///karlsays'):
    """Connect the database to the Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == '__main__':
    # If this file is run interactively, you will be able to interact directly
    # with the database
    from server import app
    connect_to_db(app)
    