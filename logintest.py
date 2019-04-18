from flask import Flask, request, Response, render_template, redirect, url_for
from functools import wraps

app = Flask(__name__)

def check(username, password):
    return username == 'admin' and password == '1234'

def auth():
    return Response('Please login', 401, {'WWW-Authenticate': 'Basic real="Login Required"'})


def requires_auth(f):
    @wraps(f)
    def deco(*args, **kwargs):
        autho = request.authorization
        if not autho or not check(autho.username, autho.password):
            return auth()
        return f(*args, **kwargs)
    return deco

@app.route('/')
@requires_auth
def site():
    return render_template('index.html', iwas="Wie möchtest du dich anmelden")

@app.route('/login', methods=['POST', 'GET'])
def login():
    return redirect('https://www.googleapis.com/auth')

if __name__ == '__main__':
    app.run(port=1247, debug=False)