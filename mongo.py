import pymongo

client = pymongo.MongoClient("mongodb+srv://edangol:97ni%40123Ui@cluster0-xrtz3.mongodb.net/test?retryWrites=true")
db = client.test
#mydb = client["mydatabase"]
print(client.list_database_names())

mydb = client["evanmongo"]
mycol = mydb["evan collection"]

x = mycol.find_one()

print(x)