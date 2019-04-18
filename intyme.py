from flask import Flask, redirect, url_for
import requests
from oauth2client.client import flow_from_clientsecrets
import json
import oauthlib



app = Flask(__name__)


# Das wird die Loginseite von intyme
@app.route('/')
def login():
    
    return 'Hallo'




# Hier wird zum google login geroutet
@app.route('/googlelogin', methods=['POST', 'GET'])
def googlelogin():
    flow = flow_from_clientsecrets('C:/Users/jansu/Desktop/dev/credentials.json',
                                scope='https://www.googleapis.com/auth/calendar',
                                redirect_uri='http://localhost')

    auth_uri = flow.step1_get_authorize_url()
    return    

if __name__ == "__main__":
    app.run(port=1247, debug=False, thread=True)