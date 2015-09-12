# coding: UTF-8
# !/usr/bin/python

import sys
from pymongo import MongoClient
from bson.objectid import ObjectId

# CLIENTE API
import requests
from requests.auth import HTTPDigestAuth
# FIM CLIENTE API

########################################################################################

r = requests.get('http://apiryhan.herokuapp.com/api/pessoa/', 
        auth=('admin','admin'))
    
objetos = r.json()['results']

########################################################################################

client = MongoClient(host='localhost', port=27017)
db = client['treinamento']

db.tabela2.drop()

for objeto in objetos:
    db.tabela2.insert({'id': objeto['id'], 'nome':objeto['nome'], 'idade':objeto['idade']})

print list(db.tabela2.find())