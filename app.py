from pymongo import MongoClient

MONGO_URI = 'mongodb://localhost'

client = MongoClient(MONGO_URI)

db = client['teststore'] #COLLECTION 
collection = db['products'] # BASE DE DADOS

#INSERIR UM 
#collection.insert_one({"name": "teclado", "price": 300})

#INSERIR UM VETOR OU LISTA
#product_one = {"name": "mouse"}
#product_two = {"name":"monitor"}
#collection.insert_many([product_one, product_two])

#PROCURAR PELO NOME 
#results = collection.find()
#for r in results:
#   print(r['name'])

#PROCURAR POR APENAS UM NOME
#results = collection.find({"price":300})
#for r in results:
#   print(r)

#PROCURAR UM
#result = collection.find_one({"name": "mouse"})
#print (result)

#DELETAR MUITOS
#collection.delete_many({"price": 300})

#DELETAR UM
#collection.delete_one({"name": "monitor"})

#ATUALIZAR 
collection.update_one({"name":"mouse"}, {"$set": {"name":"keyboard"}})