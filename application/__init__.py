from flask import Flask
from config import Config
from pymongo import MongoClient

app = Flask(__name__)
app.config.from_object(Config)

db_client = MongoClient(app.config['MONGODB_URL'])
db = db_client[app.config['MONGODB_DB']]

from application import routes