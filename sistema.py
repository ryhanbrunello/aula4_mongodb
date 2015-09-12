# coding: UTF-8
# !/usr/bin/python

import sys
from pymongo import MongoClient

client = MongoClient(host='localhost', port=27017)
db = client['treinamento']

db.tabela1.insert({'nome':'Ryhan', 'idade':25})
db.tabela1.insert({'nome':'Mufasa', 'idade':3})
db.tabela1.insert({'nome':'Wander', 'idade':25})
db.tabela1.insert({'nome':'Thalys', 'idade':26})
db.tabela1.insert({'nome':'Lucas', 'idade':24})
db.tabela1.insert({'nome':'Olivaldo', 'idade':33})

#print list(db.tabela1.find())
print list(db.tabela1.find())