import os
import bcrypt
import json
import pdb
from flask import Flask, render_template, request, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from model import User, Venue, Visit, connect_to_db, db
from helper_functions import *

app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/')
def index():
    """Checks for user login and returns homepage or login template."""
    # checks to see if user logged in; redirects to login if not
    if User.user_logged_in():
        return render_template('index.html', google_api_key=google_api_key)
    else:
        return redirect('/login')


################################################
# User management routes

@app.route('/login')
def login():
    """Provides user login form."""
    # checks to see if user logged in; redirect to homepage if so
    if 'user_id' in session:
        return redirect('/')
    else:
        return render_template('login.html')


@app.route('/login_submit', methods=['POST'])
def submit_login():
    """Logs user in to app."""
    # gets user email and pw from login form
    email = request.form.get('email')
    password = request.form.get('password')

    # retrieves user object from database
    if User.log_user_in(email, password):
        return redirect('/')
    return render_template('login.html')


@app.route('/register', methods=['POST'])
def register():
    """Registers user as a user of the app."""
    username = request.form.get('username')
    password = request.form.get('password')
    User.create_user(email, password)

    return redirect('/')


@app.route('/logout')
def logout():
    """Logs user out of app."""
    User.log_user_out()
    return redirect('/login')


################################################
# App functionality routes


if __name__ == '__main__': # pragma: no cover
   
    app.debug = True
   
    connect_to_db(app)
   
    # DebugToolbarExtension(app)

    # app.run(host='0.0.0.0')
    app.run()
