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
songwriter = db.songwriters

# setting up the pipeline
pipeline = [
    # stage - 1
    {"$match" : {"recordings.0" : {"$exists" : 1}}}, 
    # stage - 2
    {"$project" : {"_id" : 1, "songwriter_id" : 1, "name" : 1, "num_recordings" : {"$size" : "$recordings"}}}
]

# executing the pipeline
results = songwriter.aggregate(pipeline)

# printing the results
for i in results:
    printer.pprint(i)
    print()
