from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.cwsth.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
print(db.list_collection_names())

import getch

students = db["students"]

nick = {"student_id": "1007", 
    "first_name": "Nick",
    "last_name": "Cosentino"
    }


new_student_Id = students.insert_one(nick).inserted_id 
print("  Student ID: " + nick["student_id"] + "\n  First Name: " + nick["first_name"] + "\n  Last Name: " + nick["last_name"] + "\n")


cris ={"student_id": "1008", 
    "first_name": "Cris",
    "last_name": "Cosentino",

    }


new_student_Id2 = students.insert_one(cris).inserted_id 
print("  Student ID: " + cris["student_id"] + "\n  First Name: " + cris["first_name"] + "\n  Last Name: " + cris["last_name"] + "\n")


gabe = {"student_id": "1009", 
    "first_name": "Gabe",
    "last_name": "Martins"
    }


new_student_Id3 = students.insert_one(gabe).inserted_id 
print("  Student ID: " + gabe["student_id"] + "\n  First Name: " + gabe["first_name"] + "\n  Last Name: " + gabe["last_name"] + "\n")
from getch import pause_exit

pause_exit(status=0, message='Press any key to exit.')
