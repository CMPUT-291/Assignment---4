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
db = client.A4dbNorm
recordings = db.recordings

# setting up the pipeline
pipeline = [
    {"$unwind" : "$songwriter_ids"},
    {"$match" : {"issue_date" : {"$gt" : datetime.datetime(1950, 1, 1)}}}, 
    {"$lookup" : {"from" : "songwriters", "localField" : "songwriter_ids", "foreignField" : "songwriter_id", "as" : "songwriter"}}, 
    {"$unwind" : "$songwriter"},
    {"$project" : {"_id" : 1, "name" : "$songwriter.name", "r_name" : "$name", "r_issue_date" : "$issue_date"}}
]

# executing the pipeline
results = recordings.aggregate(pipeline)

# printing the results
for i in results:
    printer.pprint(i)
    print()
