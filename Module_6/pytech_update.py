from unittest import result
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.cwsth.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
print(db.list_collection_names())

import dbm


students = db["students"]
#print(students[1].last_name)
docs = db.collection.students.find([])
#docs = students.find([])
#for doc in docs:
      #print (doc)
result = db.students.find_one_and_update({"student_id": "1007"}, {"$set": {"last_name": "Smith"}})
#abc = students.find_one({"student_id": "1007"})
print(result)