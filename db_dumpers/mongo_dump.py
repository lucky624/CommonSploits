#!/usr/bin/env python
from pymongo import MongoClient

import pymongo, sys

IP = '127.0.0.1'
PORT = 27017


client = pymongo.MongoClient(IP,PORT)

db = client['pcap']#pcap - db name
collection = db.get_collection(name='filesImported')# filesImported - collection name


for raw in collection.find():
    print(raw)
