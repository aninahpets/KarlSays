import os
import pdb
import yelp
import requests
from pyowm import OWM
from model import User, connect_to_db, db
from random import randrange
from flask import Flask, render_template, redirect, request, flash, session
from flask_sqlalchemy import SQLAlchemy

def check_if_raining():

    ''' Makes Open Weather Map API call to check whether it's raining.

        Returns a boolean: TRUE for indoors, FALSE for outdoors '''

    WEATHER_API_KEY = os.environ.get('WEATHER_TOKEN')
    owm = OWM(WEATHER_API_KEY)

    # Daily weather forecast just for the next 1 days over San Francisco
    fc = owm.daily_forecast('San Francisco County,us', limit=1)

    #forecast object, with all of the info about weather forcast
    f = fc.get_forecast()

    # Will it rain
    rain = fc.will_have_rain()
    #return True or False

    # if  function returns TRUE, call YELP API to stay indoors
    # if function returns FALSE, call Parks API to stay outdoors
    return rain

def get_restaurant(neighborhood):
    ''' Makes Yelp API call to retrieve a restaurant.'''

	# Authentication steps needed to make Yelp API call
	app_id = os.environ.get("YELP_TOKEN")
	app_secret = os.environ.get("YELP_SECRET")

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
