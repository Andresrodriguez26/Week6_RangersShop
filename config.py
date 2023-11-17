# This is our configuration folder to configure Flask to our app location & variables needed to run Flask


from datetime import timedelta
import os # Operating system
from dotenv import load_dotenv # Allows us to load our environment variables (variables needed to run application)


# Establish our base directory so whenever we use "." to reference any locaion in our app it knows we are referencing
# rangers_shop folder
basedir = os.path.abspath(os.path.dirname(__file__))


# Need to establish where our environment variables are coming from (this file will be hidden from github)
load_dotenv(os.path.join(basedir, ".env"))



# Create our Config Clas
class Config():

    """
    Create Config class which will setup our configuration variables.
    Using Enviroment variables where available other create config variables.
    """

# Regular configuration for Flask App
    FLASK_APP = os.environ.get("FLASK_APP") # Looking for key of FLASK_APP in our enviroment variable location (.env)
    FLASK_ENV = os.environ.get("FLASK_ENV") 
    FLASK_DEBUG = os.environ.get("FLASK_DEBUG")

# Configuration if you are connecting a database 
    SECRET_KEY = os.environ.get("SECRET_KEY") or "Literally whatever you want as long as is a String. Cool Beans"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False # We don't want a message everytime our database is changed
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=365)

