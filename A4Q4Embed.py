# importing the required libraries
from pymongo import MongoClient
import json
import bson.json_util
import datetime
import pprint

# setting up the pretty printer and client
printer = pprint.PrettyPrinter()
client = MongoClient()

# accessing the database and collection
db = client.A4dbEmbed
collection = db.SongwritersRecordings

# setting up the pipeline
pipeline = [
    {"$unwind" : "$recordings"},
    {"$match" : {"recordings.issue_date" : {"$gt" : datetime.datetime(1950, 1, 1)}}}, 
    {"$project" : {"_id" : 1, "name" : "$name", "r_name" : "$recordings.name", "r_issue_date" : "$recordings.issue_date"}}
]

# executing the pipeline
results = collection.aggregate(pipeline)

# printing the results
for i in results:
    printer.pprint(i)
    print()
