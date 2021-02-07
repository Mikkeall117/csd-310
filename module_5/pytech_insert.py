"""
    Title: pytech_insert.py
    Author: Michael McNulty
    Date: 31 January 2021
    Description: This program inserts new student documents to the MongoDB Database.
"""

# imports pymongo and MongoClient
from pymongo import MongoClient

# url for connecting to my MongoDB database
url = "mongodb+srv://admin:admin@cluster0.uu0gn.mongodb.net/pytech?retryWrites=true&w=majority"

# creates the variable client and sets it equal to the imported MongoClient that is running through the variable url. 
client = MongoClient(url)

# sets db equal to the client using the pytech database
db = client.pytech

# the Marcus Aurelius data document
marcus = {
    "student_id": "4041",
    "first_name": "Marcus",
    "last_name": "Aurelius",
    "enrollments": [
        {
            "term": "spring",
            "gpa": "3.8",
            "start_date": "1/31/2021",
            "end_date": "4/3/2021",
            "courses": [
                {
                    "course_id": "INFO 230",
                    "description": "Computer Repair and Troubleshooting",
                    "instructor": "Professor Dave Matthews",
                    "grade": "3"
                },
                {
                    "course_id": "INFO 260",
                    "description": "Software Development Methodologies",
                    "instructor": "Professor Taylor Swift",
                    "grade": "2"
                }
            ]
        }
    ]
}

# Luke Skywalker data document
luke = {
    "student_id": "2008",
    "first_name": "Luke",
    "last_name": "Skywalker",
    "enrollments": [
        {
            "term": "summer",
            "gpa": "3.9",
            "start_date": "5/5/2021",
            "end_date": "8/1/2021",
            "courses": [
                {
                    "course_id": "INFO 250",
                    "description": "Intro to Networking",
                    "instructor": "Professor Gene Simmons",
                    "grade": "4"
                },
                {
                    "course_id": "INFO 200",
                    "description": "Intro to Database Administration",
                    "instructor": "Professor Eddie Van Halen",
                    "grade": "2"
                }
            ]
        }
    ]
}

# Darth Vader data document
darth = {
    "student_id": "3007",
    "first_name": "Darth",
    "last_name": "Vader",
    "enrollments": [
        {
            "term": "winter",
            "gpa": "4.0",
            "start_date": "11/1/2020",
            "end_date": "3/1/2021",
            "courses": [
                {
                    "course_id": "INFO 370",
                    "description": "Network Troubleshooting",
                    "instructor": "Professor Adam Levine",
                    "grade": "3"
                },
                {
                    "course_id": "INFO 440",
                    "description": "Intro to Machine Learning",
                    "instructor": "Professor Billy Ray Cyrus",
                    "grade": "1"
                }
            ]
        }
    ]
}

# get information from the student collection of the database.
students = db.students

print("\n -- INSERT STATEMENTS --")
marcus_student_id = students.insert_one(marcus).inserted_id
print(" Inserted student record Marcus Aurelius into the students collection with the document_id " + str(marcus_student_id))

luke_student_id = students.insert_one(luke).inserted_id
print("Inserted student record Luke Skywalker into the students collection with the document_id" + str(luke_student_id))

darth_student_id = students.insert_one(darth).inserted_id
print("Inserted student record Darth Vader into the students collection with the document_id" + str(darth_student_id))

input("\n\n End of program, press any key to exit...")