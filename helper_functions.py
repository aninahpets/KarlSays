import os
import pdb
import yelp
import requests
import random
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
    # if function returns FALSE, query db to stay outdoors
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
	search['location'] = neighborhood+' San Francisco'
	search['open_now'] = True
	search['categories'] = 'food'

	# Yelp API call. Input is search terms, output is a list of businesses 
	url = 'https://api.yelp.com/v3/businesses/search?'
	response = requests.get(url,headers=headers,params=search)

	# Saves list of businesses from Yelp API call
	businesses = response.json()['businesses']

	business = random.choice(businesses)
	restaurant = {'name': business['name'],
	            'url':business['url'],
	            'coordinates':business['coordinates']}
	return restaurant

	# What info do we want to get from businesses 
def get_rainy_activity(neighborhood,outing_type):
	''' Makes Yelp API call to retrieve an indoor activity if raining.'''
	app_id = os.environ.get("YELP_TOKEN")
	app_secret = os.environ.get("YELP_SECRET")

	payload = {'grant_type':'client_credentials',
			   'client_id':app_id,
			   'client_secret':app_secret}
	r = requests.post('https://api.yelp.com/oauth2/token', params=payload).json()

	token = r['access_token']

	headers = {}
	headers['Authorization'] = 'Bearer ' + str(token)

	# Pre determined Yelp categories correlating to outing_type
	categories = {'group': ['active,aquariums', 'arts,arcades', 'arts,galleries', 'arts,jazzandblues', 'arts,museums,artmuseums','arts,observatories', 'arts,planetarium', 'nightlife,bars', 'nightlife,comedyclubs'],
				  'date' : ['active,aquariums', 'arts,arcades', 'arts,galleries', 'arts,jazzandblues', 'arts,museums,artmuseums','arts,observatories', 'arts,planetarium', 'nightlife,bars', 'nightlife,comedyclubs', 'nightlife,musicvenues'],
				  'solo':['active,aquariums', 'arts,arcades', 'arts,galleries', 'arts,jazzandblues', 'arts,museums,artmuseums','arts,observatories', 'arts,planetarium', 'nightlife,bars', 'nightlife,comedyclubs'],
				  'family': ['active,aquariums', 'arts,arcades', 'arts,galleries', 'arts,museums','arts,observatories', 'arts,planetarium']
				 }

	category = random.choice(categories[outing_type])

	# Modify with search params for Yelp call
	search = {}
	search['location'] = neighborhood
	search['open_now'] = True
	search['categories'] = category


	# Yelp API call. Input is search terms, output is a list of businesses 
	url = 'https://api.yelp.com/v3/businesses/search?'
	response = requests.get(url,headers=headers,params=search)

	# Saves list of businesses from Yelp API call
	businesses = response.json()['businesses']
	business = random.choice(businesses)
	activity_location = {'name': business['name'],
                'url':business['url'],
                'coordinates':business['coordinates']}

	return activity_location


def get_sunny_activity(neighborhood):
    """Queries database to get a park for a sunny day outing"""

    activity_location = db.session.query(Park).filter_by(neighborhood=neighborhood).first()

    return activity_location.json


    