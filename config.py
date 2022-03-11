import os

basedir = os.path.abspath(os.path.dirname(__name__))
# base directory creation for entire application - helps computer figure out file system and where to find diff pieces of project
# sets up file org and enables us to find file paths when needed, which helps with imports & other linking

class Config:
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY')