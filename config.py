import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Q.]KUO<8O`x&LpwXum?VGU"~eAl2jr'
    MONGODB_URL = 'mongodb://localhost:27017/'
    MONGODB_DB = 'enrollment'