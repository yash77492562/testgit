
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://yashyadavpro:\"Alonecurse\"@cluster0.ejmvwws.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)



d = {
    "name" : "yash",
    "email" : "yashyadavpro@gmail.com",
    "surname" : "yadav"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)

#client=pymongo.MangoClient("mongodb+srv://yashyadavpro:"Alonecurse"@cluster0.ejmvwws.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
#db=client.test