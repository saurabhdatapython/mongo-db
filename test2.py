import  pymongo
client = pymongo.MongoClient("mongodb+srv://saurabhdata:Rajbhatta1!#$@saurabhdata.ckhjdot.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client["my_database"]

collection1 = database["table2"]
record = collection1.find()
for i in record :
    print(i)