from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap

app = Flask(__name__) # set name of the module flask will be used in
app.config.from_object(Config) # tell flask to read and apply config file
bootstrap = Bootstrap(app)

from app import routes # need to import routes module here as a workaround to circular imports
