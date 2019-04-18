from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json
import oauthlib
import requests
from oauth2client.client import flow_from_clientsecrets





'''client_id = "nhu9-XjyF1vQ9aPqA6IbeZ2W"
client_secret = "833074025603-3hv5odth3abrd0rk3jndjpmud4676kjf.apps.googleusercontent.com"
redirect_uri = "http://localhost"
scope = ['https://www.googleapis.com/auth/calendar.readonly']

oauth = oau'''
def main():


    flow = flow_from_clientsecrets('C:/Users/jansu/Desktop/dev/credentials.json',
                                scope='https://www.googleapis.com/auth/calendar',
                                redirect_uri='http://localhost')

    auth_uri = flow.step1_get_authorize_url()
    code = requests.post(auth_uri)
    credentials = flow.step2_exchange()

'''creds = json.loads(credentials.json)
service = build('calendar', 'v3', credentials=creds)'''

# Call the Calendar API
'''now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
print('Getting the upcoming 10 events')
events_result = service.events().list(calendarId='primary', timeMin=now,
                                    maxResults=10, singleEvents=True,
                                    orderBy='startTime').execute()
events = events_result.get('items', [])    

for event in events:
    start = event['start'].get('dateTime', event['start'].get('date'))
    print(start, event['summary'])'''

if __name__ == '__main__':
    main()