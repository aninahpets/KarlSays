import os
import bcrypt
import json
import pdb
from flask import Flask, render_template, request, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from model import User, connect_to_db, db
from helper_functions import *

app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/')
def index():
    """Checks for user login and returns homepage or login template."""
    # checks to see if user logged in; redirects to login if not
    if User.user_logged_in():
        return #ok to render homepage
    else:
        return #render login modal again


################################################
# User management routes

@app.route('/login')
def login():
    """Provides user login form."""
    # checks to see if user logged in; redirect to homepage if so
    if 'user_id' in session:
        return #ok to render homepage
    else:
        return #render login modal again


@app.route('/login_submit', methods=['POST'])
def submit_login():
    """Logs user in to app."""
    # gets username and pw from login form
    username = request.form.get('username')
    password = request.form.get('password')

    # retrieves user object from database
    if User.log_user_in(username, password):
        return #ok to render homepage
    return #render login modal again

@app.route('/register', methods=['POST'])
def register():
    """Registers user as a user of the app."""
    username = request.form.get('username')
    password = request.form.get('password')
    User.create_user(username, password)

    return #ok to render homepage


@app.route('/logout')
def logout():
    """Logs user out of app."""
    User.log_user_out()
    return #render login modal again


################################################
# App functionality routes


if __name__ == '__main__': # pragma: no cover
   
    app.debug = True
   
    connect_to_db(app)
   
    # DebugToolbarExtension(app)

    # app.run(host='0.0.0.0', port=5000)
    app.run()
