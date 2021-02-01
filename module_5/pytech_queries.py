"""
    Title: pytech_queries.py
    Author: Michael McNulty
    Date: 31 January 2021
    Description: This program uses the find method to display all documents in a collection, and then display a single document by student_id.
"""

# creates the docs variable and sets it equal to all the documents in the students collection.
docs = db.students.find({})

# prints every document from the students collection in a row.
for doc in docs:
    print(doc)

# finds a single document by student_id and assigns it to the doc variable.
doc = db.students.find_one({"student_id": "1008"})

# prints the document found above assigned to the doc variable to terminal.
print(doc["student_id"])