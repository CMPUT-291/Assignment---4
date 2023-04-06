# importing the required libraries
from pymongo import MongoClient
import json
import bson.json_util
import pprint
import argparse

# setting up parser
parser = argparse.ArgumentParser()
parser.add_argument('port', type=int, nargs='?', default=27017, help='the port number to run the application on')
args = parser.parse_args()
port_number = args.port

# setting up the pretty printer and client
port_data = 'mongodb://localhost:' + str(port_number)
printer = pprint.PrettyPrinter()
client = MongoClient(port_data)

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
