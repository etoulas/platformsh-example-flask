from flask import Flask
from werkzeug.contrib.fixers import ProxyFix


app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_world():
    return 'Hello, platform.sh!'


app.wsgi_app = ProxyFix(app.wsgi_app)
