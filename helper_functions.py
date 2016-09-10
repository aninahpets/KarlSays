import os
import pdb
import requests
from model import User, connect_to_db, db
from random import randrange
from flask import Flask, render_template, redirect, request, flash, session
from flask_sqlalchemy import SQLAlchemy

