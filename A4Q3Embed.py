# importing the required libraries
from pymongo import MongoClient
import json
import bson.json_util
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
    {"$match" : {}}, 
    {"$group" : {"_id" : "$songwriter_id", "total_length" : {"$sum" : "$recordings.length"}}}, 
    {"$project" : {"_id" : 1, "total_length" :  1, "songwriter_id" : "$_id"}}
]

# executing the pipeline
results = collection.aggregate(pipeline)

# printing the results
for i in results:
    printer.pprint(i)
    print()
