# coding: UTF-8
# !/usr/bin/python

import sys
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient(host='localhost', port=27017)
db = client['treinamento']

db.tabela2.update({'nome': {'$regex':'.*.*'}}, {'$set':{'idade':0}}, multi=True)

print list(db.tabela2.find())