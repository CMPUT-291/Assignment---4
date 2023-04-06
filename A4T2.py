from pymongo import MongoClient
import json
import bson.json_util

client = MongoClient()

db = client.A4dbEmbed
collection = db.SongwritersRecordings

with open('songwriters.json', encoding = "utf8") as fh:
    file_data_song = bson.json_util.loads(fh.read())

with open('recordings.json', encoding = "utf8") as fh:
    file_data_recs = bson.json_util.loads(fh.read())

def recording_finder(rec_id):
    for i in range(len(file_data_recs)):
        if file_data_recs[i]["recording_id"] == rec_id:
            return file_data_recs[i]

# create an embedded collection from songwriters and recordings
for song in range(len(file_data_song)):
    for rec in range(len(file_data_song[song]["recordings"])):
        file_data_song[song]["recordings"][rec] = recording_finder(file_data_song[song]["recordings"][rec])

collection.insert_many(file_data_song)
