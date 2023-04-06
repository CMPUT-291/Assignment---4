# importing the required libraries
from pymongo import MongoClient
import json
import bson.json_util

# setting up the client
client = MongoClient()

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