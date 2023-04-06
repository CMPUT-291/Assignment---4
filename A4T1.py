# importing the required libraries
from pymongo import MongoClient
import json
import bson.json_util
import argparse

# setting up parser
parser = argparse.ArgumentParser()
parser.add_argument('port', type=int, nargs='?', default=27017, help='the port number to run the application on')
args = parser.parse_args()
port_number = args.port

# setting up the client
port_data = 'mongodb://localhost:' + str(port_number)
client = MongoClient(port_data)

# accessing the database and collection
db = client.A4dbNorm
songwriters = db.songwriters
recordings = db.recordings

# importing and inserting the data into respective collections from bson files
with open('songwriters.json', encoding = "utf8") as fh:
    file_data_song = bson.json_util.loads(fh.read())
    songwriters.insert_many(file_data_song)

with open('recordings.json', encoding = "utf8") as fh:
    file_data_recs = bson.json_util.loads(fh.read())
    recordings.insert_many(file_data_recs)