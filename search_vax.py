#!/usr/bin/env python
# coding: utf-8

# In[14]:


import requests
import urllib.request
import threading
import smtplib
import ssl
import os
from twilio.rest import Client


account_sid = 'AC401d2651c1120a18028f3449a5f3adc1'
auth_token = '4a8eb2ec670d16088a25be5fecadff32'
client = Client(account_sid, auth_token)

my_cities = ['ALEXANDRIA',
          'ANNANDALE',
          'ARLINGTON',
          'ASHBURN',
          'BAILEYS CROSSROADS',
          'CHANTILLY',
          'DUMFRIES',
          'DALE CITY',
          'GREAT FALLS',
          'HERNDON',
          'LEESBURG',
          'MANASSAS',
          'MANASSAS PARK',
          'RESTON',
          'ROSSLYN',
          'STERLING',
          'VIENNA',
          'WARRENTON',
          'WOODBRIDGE',
          #'RICHLANDS' #TEST
            ] 

UPDATE = 300.0 # 5 minute intervals

def Search_Vax():
    
    threading.Timer(UPDATE, sendit).start()
    
    headers = {'referer': 'https://www.cvs.com/immunizations/covid-19-vaccine?icid=coronavirus-lp-nav-vaccine'}

    req = requests.get('https://www.cvs.com/immunizations/covid-19-vaccine.vaccine-status.VA.json?vaccineinfo', headers=headers)
    req = req.json()

    for city_dict in req['responsePayloadData']['data']['VA']:
        if (city_dict['city'] in my_cities) & (city_dict['status']=='Available'):

            message = 'COVID-19 vaccine available in ' + city_dict['city'] + ', VA. Go to https://www.cvs.com/vaccine/intake/store/covid-screener/covid-qns to sign up.'

            # Send Twilio Text Message
            # Brian
            client.messages.create(body=message,from_='+17604630254',to='+14845475276')
            # Nikki
            #client.messages.create(body=message, from_='+17604630254',to='+14845154869')
            
Search_Vax()

