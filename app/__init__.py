# Create application object as instance of class Flask 

from flask import Flask

app = Flask(__name__) # location is used as name

from app import routes # workaround for circular imports