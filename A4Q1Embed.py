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
    {"$match" : {"recordings.0" : {"$exists" : 1}}}, 
    # stage - 2
    {"$project" : {"_id" : 1, "songwriter_id" : 1, "name" : 1, "num_recordings" : {"$size" : "$recordings"}}}
]

# executing the pipeline
results = collection.aggregate(pipeline)

# printing the results
for i in results:
    printer.pprint(i)
    print()
