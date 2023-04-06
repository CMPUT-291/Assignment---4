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