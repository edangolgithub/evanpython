import pymongo
#client = pymongo.MongoClient("mongodb+srv://edangol:97ni%40123Ui@cluster0-xrtz3.mongodb.net/test?retryWrites=true")
client=pymongo.MongoClient("mongodb://localhost:27017")
db=client["db2"]
table=db["db2collection"]
for x in table.find().limit(1):
    print(x)
    print("xyz")

for x in table.find({},{ "name": 1,  "address": 1 }):
  print(x)    

  myquery = { "name": { "$regex": "^r" } }

  for x in table.find(myquery):
      print(x['name'])

#myquery = { "address": "Mountain 21" }
#mycol.delete_one(myquery)

#myquery = { "address": {"$regex": "^S"} }
#x = mycol.delete_many(myquery)
#x = mycol.delete_many({})
#mycol.drop()

#myquery = { "address": "thamel" }
newvalues = { "$set": { "address": "Canyon 123" } }

#table.update_one(myquery, newvalues)
table.update_many({"address":{"$regex":"^n"}},newvalues)