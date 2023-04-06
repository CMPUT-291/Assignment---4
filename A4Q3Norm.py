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
songwriters = db.songwriters

# setting up the pipeline
pipeline = [
    {"$unwind" : "$recordings"},
    {"$lookup" : {"from" : "recordings", "localField" : "recordings", "foreignField" : "recording_id", "as" : "recording"}},
    {"$match" : {}}, 
    {"$unwind" : "$recording"},
    {"$group" : {"_id" : "$songwriter_id", "total_length" : {"$sum" : "$recording.length"}}}, 
    {"$project" : {"_id" : 1, "total_length" :  1, "songwriter_id" : "$_id"}}
]

# executing the pipeline
results = songwriters.aggregate(pipeline)

# printing the results
for i in results:
    printer.pprint(i)
    print()