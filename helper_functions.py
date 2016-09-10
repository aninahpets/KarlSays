import os
import pdb
import yelp
import requests
from model import User, connect_to_db, db
from random import randrange
from flask import Flask, render_template, redirect, request, flash, session
from flask_sqlalchemy import SQLAlchemy

def get_restaurant(neighborhood):
	''' Makes Yelp API call to retrieve a restaurant.'''
	pdb.set_trace()
	# Authentication steps needed to make Yelp API call
	app_id = os.environ.get("YELP_TOKEN")
	app_secret = os.environ.get("YELP_APP_SECRET")

	payload = {'grant_type':'client_credentials',
			   'client_id':app_id,
			   'client_secret':app_secret}
	r = requests.post('https://api.yelp.com/oauth2/token', params=payload).json()
	token = r['access_token']

	headers = {}
	headers['Authorization'] = 'Bearer ' + str(token)

	# Modify with search params for Yelp call
	search = {}
	search['location'] = 'neighborhood'
	search['open_now'] = True
	search['categories'] = 'food'

	# Yelp API call. Input is search terms, output is a list of businesses 
	url = 'https://api.yelp.com/v3/businesses/search?'
	response = requests.get(url,headers=headers,params=search)

	# Saves list of businesses from Yelp API call
	businesses = response.json()['businesses']

	print businesses
	return businesses

	# What info do we want to get from businesses 
get_restaurant('Nob Hill')
