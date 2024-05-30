import pymongo
client=pymongo.MongoClient("mongodb+srv://yashyadavpro:\"Alonecurse\"@cluster0.ejmvwws.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db=client.test
print(db)

d = {
    "name" : "yash",
    "email" : "yashyadavpro@gmail.com",
    "surname" : "yadav"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)