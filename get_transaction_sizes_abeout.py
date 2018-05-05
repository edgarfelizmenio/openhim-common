from pymongo import MongoClient
import bson

client = MongoClient('localhost', 27017)
db = client.openhim
transactions = db.transactions
txn_list = list(transactions.find())
txn_sizes = [len(bson.BSON.encode(txn)) for txn in txn_list]

with open("abeout_txn_sizes.txt", "w") as txn_sizes_file:
	txn_sizes_file.writelines([str(txn_size) + "\n" for txn_size in txn_sizes])


