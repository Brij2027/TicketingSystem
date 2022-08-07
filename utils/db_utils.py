import pymongo
from decouple import config

my_client = pymongo.MongoClient(config("DB_CONNECTION_STRING"))