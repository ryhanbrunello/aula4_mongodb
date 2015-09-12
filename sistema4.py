# coding: UTF-8
# !/usr/bin/python

import sys
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient(host='localhost', port=27017)
db = client['treinamento']

objeto = db.tabela2.find().sort('idade', -1).limit(1)

for obj in objeto:
	db.tabela2.remove({'idade': obj['idade']}, multi=True)

#print list(db.tabela2.find({ 'idade':85}))
print list(db.tabela2.find())