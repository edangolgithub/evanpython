import pymongo

client = pymongo.MongoClient("mongodb+srv://edangol:97ni%40123Ui@cluster0-xrtz3.mongodb.net/test?retryWrites=true")
db = client["db2"]
table=db["db2collection"]
data={"name":"shyam","roll":"18","address":"thamel"}
table.insert_one(data)

print(table.find_one())