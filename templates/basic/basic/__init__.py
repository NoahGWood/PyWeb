"""
PyWeb Basic Starter
"""
# Main imports
import configparser
from flask import Flask

# Set up Jinja
# Import Config handlers
#from config import ConfigClass

#PyWeb Imports
from basic.pages import PageLoader

CONFP = configparser.ConfigParser()
CONFP.read('settings.conf')

APP = Flask(__name__)
APP.jinja_env.globals['site'] = CONFP

# Get flask configs
#conf = ConfigClass()
#app.config.from_object(conf)

def setup():
    """Sets up the flask server"""
    # Load Pages
    PageLoader(APP, root='basic', ignore_bad=CONFP['APP']['ignore_bad_pages'])
    return APP
