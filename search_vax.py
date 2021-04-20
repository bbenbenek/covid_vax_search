import requests
import urllib.request
import threading
import smtplib
import ssl
import os
from twilio.rest import Client
from datetime import datetime
import time


account_sid = twilio_acct_id
auth_token = twilio_auth_token
client = Client(account_sid, auth_token)

my_cities = ['MY CITY1',
             'MY CITY 2',
             'MY CITY 3',
            ] 

def Search_Vax(client, my_cities):
        
    headers = {'referer': 'https://www.cvs.com/immunizations/covid-19-vaccine?icid=coronavirus-lp-nav-vaccine'}

    req = requests.get('https://www.cvs.com/immunizations/covid-19-vaccine.vaccine-status.VA.json?vaccineinfo', headers=headers)
    req = req.json()

    counter = 0
    city_avail = []
    for city_dict in req['responsePayloadData']['data']['VA']:
        if (city_dict['city'] in my_cities) & (city_dict['status']=='Available'):

            city_avail.append(city_dict['city'])
        
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    if len(city_avail) > 0:
        message = 'COVID-19 vaccine available in ' + (' & ').join(city_avail) + '. Go to https://www.cvs.com/vaccine/intake/store/covid-screener/covid-qns to sign up.'

        # Send Twilio Text Message
        # My Number
        client.messages.create(body=message, from_='+0001112222',to='+15555555555')

        
        print(current_time, 'Appointment found! Sent text message.')
    else:
        print(current_time, 'No appointments available')
        
while True:
    Search_Vax(client, my_cities)
    time.sleep(300)
