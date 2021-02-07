"""
    Title: pytech_update.py
    Author: Michael McNulty
    Date: 7 February 2021
    Description: This program prints all the documents in the students database, then updates the last_name of student_id 1007. 
"""

# imports pymongo and MongoClient
from pymongo import MongoClient

# url for connecting to my MongoDB database
url = "mongodb+srv://admin:admin@cluster0.uu0gn.mongodb.net/pytech?retryWrites=true&w=majority"

# creates the variable client and sets it equal to the imported MongoClient that is running through the variable url. 
client = MongoClient(url)

# sets db equal to the client using the pytech database
db = client.pytech

# gets the students collection from the database.
students = db.students

# this finds all the students in the collection.
student_list = students.find({})

# displays a header for this section of the assignment.
print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# prints every document from the students collection in a row.
for doc in student_list:
    print(" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

# calls the update_one method and updates the last_name associated with student_id 1007.
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Caesar"}})

# calls the find_one method and prints the information from the document associated with student_id 1007
marcus = students.find_one({"student_id": "1007"})

# displays a header for this section of the assignment.
print("\n -- DISPLAYING STUDENT DOCUMENT FROM 1007 --")

# prints the single document from the student collection associated with student_id 1007.
print(" Student ID: " + marcus["student_id"] + "\n First Name: " + marcus["first_name"] + "\n Last Name: " + marcus["last_name"] + "\n")

# gets the user's input to end the program.
input("\n\nEnd of program, press any key to continue...")