#!virt/bin/python3
import json
import urllib.request
import config
import re
from twilio.rest import TwilioRestClient
def get_weather(city):
   api = 'http://api.aerisapi.com/forecasts/%s?from=today&to=today&client_id=%s&client_secret=%s' %(city,config.AERIS_ID,config.AERIS_SECRET)
   response = urllib.request.urlopen(api)
   str_response = response.read().decode('utf-8')
   js = json.loads(str_response)
   ob = js['response'][0]
   day_weather=ob['periods']
   return day_weather

def check_rain(day_weather):
   rainregex = re.compile(r'shower(s)',re.I)
   sunnyregex = re.compile(r'sunny',re.I)
   for element in day_weather:
      if sunnyregex.search(element['weather']):
         return element['weather'] 

def send_message(weather):
   twilioCli=TwilioRestClient(config.SID,config.AUTH_TOKEN)
   if weather != 'None':
      message = twilioCli.messages.create(body=weather, from_=config.twiNumber, to=config.myNumber)

w = get_weather('arlington,va')
send_message(check_rain(w))

