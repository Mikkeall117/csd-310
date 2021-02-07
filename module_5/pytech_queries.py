"""
    Title: pytech_queries.py
    Author: Michael McNulty
    Date: 31 January 2021
    Description: This program uses the find method to display all documents in a collection, and then display a single document by student_id.
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
print("\n -- DISPLAYING STUDENTS DOCUMENTS USING THE find() QUERY --\n")

# prints every document from the students collection in a row.
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# finds a single document by student_id and assigns it to the doc variable.
luke = students.find_one({"student_id": "1008"})

# prints the document found by student_id
print("\n -- DISPLAYING STUDENTS DOCUMENT FROM find_one() QUERY --\n")

# prints the single document from the student collection associated with student_id 1007.
print("  Student ID: " + luke["student_id"] + "\n  First Name: " + luke["first_name"] + "\n  Last Name: " + luke["last_name"] + "\n")

# checks for user input to exit the program. 
input("\n End of program, press any key to continue...")