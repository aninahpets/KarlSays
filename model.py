from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import session, flash
import bcrypt

db = SQLAlchemy()

class User(db.Model):
    """User of the app."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(75), unique=True, nullable=False)
    password = db.Column(db.String(75), nullable=False)

    @classmethod
    def log_user_in(cls, email, password):
        # retrieves user object from database
        user = User.query.filter_by(email=email).first()
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
        flash('You are now logged out.')

    @classmethod
    def create_user(cls, email, password):

        # hash and salt user pw
        password = bcrypt.hashpw(password, bcrypt.gensalt())

        # create new user record and add to database
        new_user = User(email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        session['user_id'] = new_user.user_id

    @classmethod
    def user_logged_in(cls):
        if 'user_id' in session:
            return True
        return False


if __name__ == '__main__':
    # If this file is run interactively, you will be able to interact directly
    # with the database
    from server import app
    connect_to_db(app)


    