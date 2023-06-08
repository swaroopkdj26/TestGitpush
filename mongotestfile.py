import pymongo



client = pymongo.MongoClient("mongodb+srv://swaroopkdj26:Ignite@cluster0.oeivlla.mongodb.net/?retryWrites=true&w=majority")

db=client.test
print(db)

d = {
    "name":"swrp",
    "email":"sdj26@gmail.com",
    "surname":"Jadhao"
}
d = {
    "name":"swrp",
    "email":"sdj26@gmail.com",
    "surname":"Jadhao"
}

d = {
    "name":"swrp",
    "email":"sdj26@gmail.com",
    "surname":"Jadhao"
}

d = {
    "name":"swrp",
    "email":"sdj26@gmail.com",
    "surname":"Jadhao"
}

db1= client['mongotest']
coll =db1['test']
coll.insert_one(d )