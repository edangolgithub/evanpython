import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["db2"]
table=db["db2collection"]
data={"name":"ram","roll":"10","address":"khusibu"}
table.insert_one(data)

print(table.find_one())