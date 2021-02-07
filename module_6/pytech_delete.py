"""
    Title: pytech_delete.py
    Author: Michael McNulty
    Date: 7 February 2021
    Description: This program prints all the documents in the students collection, adds a new student to the collection with the student_id 1010, 
    then deletes that student from the collection and re-prints the list of documents from the collection again. 
"""

# imports pymongo and MongoClient
from pymongo import MongoClient

# url for connecting to my MongoDB database
url = "mongodb+srv://admin:admin@cluster0.uu0gn.mongodb.net/pytech?retryWrites=true&w=majority"

# creates the variable client and sets it equal to the imported MongoClient that is running through the variable url. 
client = MongoClient(url)

# sets db equal to the client using the pytech database
db = client.pytech

# Mace Windu data document
mace = {
    "student_id": "1010",
    "first_name": "Mace",
    "last_name": "Windu",
    "enrollments": [
        {
            "term": "spring",
            "gpa": "3.2",
            "start_date": "1/31/2021",
            "end_date": "4/3/2021",
            "courses": [
                {
                    "course_id": "INFO 222",
                    "description": "Network Infrastructure",
                    "instructor": "Professor Bruce Willis",
                    "grade": "4"
                },
                {
                    "course_id": "INFO 232",
                    "description": "Introduction to VoIP",
                    "instructor": "Professor Anakin Skywalker",
                    "grade": "3"
                }
            ]
        }
    ]
}

# gets the students collection from the database.
students = db.students

# this finds all the students in the collection.
student_list = students.find({})

# displays a header for this section of the assignment.
print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# prints every document from the students collection.
for doc in student_list:
    print(" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

# prints a header for this section of the assignment.
print("\n -- INSERT STATEMENTS --")

# inserts the mace document into the database.
mace_student_id = students.insert_one(mace).inserted_id

# prints the document_id for the mace document submitted to the database.
print(" Inserted student record into the students collection with the document_id " + str(mace_student_id))

# finds a single document by student_id and assigns it to the doc variable.
mace_student_doc = students.find_one({"student_id": "1010"})

# prints a header for this section of the assignment.
print("\n -- DISPLAYING STUDENT TEST DOC --")

# prints the single document from the student collection associated with student_id 1010.
print(" Student ID: " + mace_student_doc["student_id"] + "\n First Name: " + mace_student_doc["first_name"] + "\n Last Name: " + mace_student_doc["last_name"] + "\n")

# calls the delete_one() method and deletes the document associated with student_id 1010.
deleted_student_mace_doc = students.delete_one({"student_id": "1010"})

# this finds all the new/current students in the collection.
new_student_list = students.find({})

# displays a header for this section of the assignment.
print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# prints every document from the students new/current collection in a row.
for doc in new_student_list:
    print(" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

# checks for user input to exit the program. 
input("End of program, press any key to continue...")