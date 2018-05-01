from pymongo import MongoClient
import bson

client = MongoClient('localhost', 27017)
db = client.openhim
transactions = db.transactions
transactions.remove({})

