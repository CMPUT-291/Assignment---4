# importing the required libraries
from pymongo import MongoClient
import json
import bson.json_util
import pprint

# setting up the pretty printer and client
printer = pprint.PrettyPrinter()
client = MongoClient()

# accessing the database and collection
db = client.A4dbNorm
recordings = db.recordings

# setting up the pipeline
pipeline = [
    {"$match" : { "recording_id": {"$regex": "^70"}}}, 
    {"$group": {"_id": "", "avg_rhythmicality": {"$avg": "$rhythmicality"}}}
]

# executing the pipeline
results = recordings.aggregate(pipeline)

# printing the results
for i in results:
    printer.pprint(i)
    print()
