from flask import Flask
from config import Config

app = Flask(__name__) # 'app' will be the name of the flask app, 'Flask' is the name of the module imported from flask package we installed, '__name__' tells Flask object what we've named the app, in this case, 'app'

app.config.from_object(Config) 

from . import routes