"""
    Title: mongodb_test.py
    Author: Michael McNulty
    Date: 31 January 2021
    Description: This program connects to a MongoDB database and prints a list of the collection names in the database.
"""

# imports pymongo and then imports the MongoClient from pymongo.
import pymongo
from pymongo import MongoClient

# creates the variable URL and sets it equal to the URL for the MongoDB database.
url = "mongodb+srv://admin:admin@cluster0.uu0gn.mongodb.net/pytech?retryWrites=true&w=majority"

# creates the variable client and sets it equal to MongoClient connected through the variable url.
client = MongoClient(url)

# creates the variable db and sets it equal to the pytech collection of the client variable. 
db = client.pytech

# prints collection names from the MongoDB database.
print((db.list_collection_names))