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
    # stage - 1
    {"$unwind": "$recordings"},
    # stage - 2
    {"$match" : { "recordings.recording_id": {"$regex": "^70"}}}, 
    # stage - 3
    {"$group": {"_id": "", "avg_rhythmicality": {"$avg": "$recordings.rhythmicality"}}}
]

# executing the pipeline
results = collection.aggregate(pipeline)

# printing the results
for i in results:
    printer.pprint(i)
    print()
