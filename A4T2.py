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
db = client.A4dbEmbed
collection = db.SongwritersRecordings

# importing the data from the bson files
with open('songwriters.json', encoding = "utf8") as fh:
    file_data_song = bson.json_util.loads(fh.read())

with open('recordings.json', encoding = "utf8") as fh:
    file_data_recs = bson.json_util.loads(fh.read())

# function to find the recording in the recordings collection
def recording_finder(rec_id):
    for i in range(len(file_data_recs)):
        if file_data_recs[i]["recording_id"] == rec_id:
            return file_data_recs[i]

# create an embedded collection from songwriters and recordings
for song in range(len(file_data_song)):
    for rec in range(len(file_data_song[song]["recordings"])):
        file_data_song[song]["recordings"][rec] = recording_finder(file_data_song[song]["recordings"][rec])

# inserting the data into the collection
collection.insert_many(file_data_song)