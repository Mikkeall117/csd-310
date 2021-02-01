"""
    Title: pytech_insert.py
    Author: Michael McNulty
    Date: 31 January 2021
    Description: This program inserts new student documents to the MongoDB Database.
"""

# creates the variable david and assigns it a database entry
david = {
    "first_name": "David"
}

# displays the returned student_id from inserted method call
1007 = students.insert_one(david).inserted_id

# prints the information from student_id 1007
print(1007)

# creates the variable amy and assigns it a database entry
amy = {
    "first_name": "Amy"
}

# displays the returned student_id from inserted method call
1008 = students.insert_one(amy).inserted_id

# prints the information from student_id 1008
print(1008)

# creates the variable toby and assigns it a database entry
toby = {
    "first_name": "Toby"
}

# displays the returned student_id from inserted method call
1009 = students.insert_one(toby).inserted_id

# prints the information from student_id 1009
print(1009)