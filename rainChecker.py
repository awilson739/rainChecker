#!/usr/bin/python3
import json
import urllib.request
from twilio.rest import TwilioRestClient
accountSID=''
authToken=''
api = 'http://api.aerisapi.com/forecasts/arlington,va?from=today&to=today&client_id=client_secret='
response = urllib.request.urlopen(api)
str_response = response.read().decode('utf-8')
w = json.loads(str_response)
twilioCli=TwilioRestClient(accountSID,authToken)
myTwilioNumber=''
myNumber=''
#print(str_response)
#print(w)
#print(ob['periods'])
ob = w['response'][0]
day_weather = ob['periods']
#print(type(day_weather))
for element in day_weather:
   print(element['weather'])
   message = twilioCli.messages.create(body=element['weather'], from_=myTwilioNumber, to=myNumber)

