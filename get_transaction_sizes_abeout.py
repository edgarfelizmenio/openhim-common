from pymongo import MongoClient
import bson
import re

client = MongoClient('localhost', 27017)
db = client.openhim
transactions = db.transactions
txn_list = list(transactions.find())

transaction_sizes_bins = {
    'user': [],
    'patient': [],
    'provider': [],
    'location': [],
    'encounters': []
}

for txn in txn_list:
    path = re.sub('[^a-z]+', '',txn['request']['path'])
    if path in transaction_sizes_bins:
        transaction_sizes_bins[path].append(len(bson.BSON.encode(txn)))

num_txns = len(txn_list)
for k in transaction_sizes_bins.keys():
    bin_size = len(transaction_sizes_bins[k])
    if bin_size == 0:
        del transaction_sizes_bins[k]
    else:
        num_txns = min(num_txns, bin_size)
    print(k, bin_size)

txn_sizes = []
for i in range(num_txns):
    txn_size = 0
    for k in transaction_sizes_bins.keys():
        txn_size += transaction_sizes_bins[k][i]
    txn_sizes.append(txn_size)

with open("abeout_txn_sizes.txt", "w") as txn_sizes_file:
    txn_sizes_file.writelines([str(txn_size) + "\n" for txn_size in txn_sizes])


