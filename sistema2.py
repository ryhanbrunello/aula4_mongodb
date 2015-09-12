# coding: UTF-8
# !/usr/bin/python

import sys
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient(host='localhost', port=27017)
db = client['treinamento']

#########################################################################################
#print list(db.tabela1.find())
#print list(db.tabela1.find({'nome': {'$regex': '.*R|y.*'}}))
#print list(db.tabela1.find({'idade': {'$gt': 25, '$lt': 30}}))
#print list(db.tabela1.find({'idade': {'$in': [3,24,25,30]}}))
#print list(db.tabela1.find({'idade': {'$in': [3,24,25,30]}}).sort('nome',-1))
#print list(db.tabela1.find({'$or':[{'nome': {'$regex':'.*L.*'}}, {'idade': 25}]}))
#print list(db.tabela1.find({'$and':[{'nome': {'$regex':'.*R.*'}}, {'idade': 25}]}))
#########################################################################################

#########################################################################################
#objeto = db.tabela1.find()
#objeto = db.tabela1.find({'$or':[{'nome': {'$regex':'.*L.*'}}, {'idade': 25}]})
#print objeto.count()
#########################################################################################

#########################################################################################
#chave = ['idade']
#condicao = {'idade':{'$gte': 24}}
#inicial = {'contador': 0, 'soma': 0}
#funcao = 'function(doc, out) {out.contador++; out.soma += doc.idade;}'
#print list(db.tabela1.group(chave, condicao, inicial, funcao))
#########################################################################################

#########################################################################################
#objetos = db.tabela1.aggregate(
#	[{
#		'$group':{
#			'_id': '$nome', 
#			'idade': {'$sum': '$idade'},
#			'media': {'$avg': '$idade'},
#			'contador':{'$sum': 1}
#		}
#	}]
#)

#for objeto in objetos:
#	print objeto

#for objeto in objetos:
#	print objeto['_id'] + ' = ' + str(objeto['idade'])
#########################################################################################

#########################################################################################
#db.tabela1.remove({'idade':{'$gte':3}},True)
#db.tabela1.remove({'_id': ObjectId('55f46fa05521911c4774cea4')})

#print list(db.tabela1.find())
#########################################################################################

#########################################################################################
#print list(db.tabela1.update({'nome': 'Ryhan'}, {'$set':{'idade':15}}, multi=True))
print list(db.tabela1.update({'_id': ObjectId('55f46fa05521911c4774cea4'}, {'$set':{'idade':15}}, multi=True))
#print list(db.tabela1.update({'nome': {'$regex':'.*R|r.*'}}, {'$set':{'idade':16}}, multi=True))

#print list(db.tabela1.find())
#########################################################################################