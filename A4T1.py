from pymongo import MongoClient
import json
import bson.json_util

client = MongoClient()

db = client.A4dbNorm
songwriters = db.songwriters
recordings = db.recordings

with open('songwriters.json', encoding = "utf8") as fh:
    file_data = bson.json_util.loads(fh.read())
    songwriters.insert_many(file_data)

with open('recordings.json', encoding = "utf8") as fh:
    file_data = bson.json_util.loads(fh.read())
    recordings.insert_many(file_data)

print(client.list_database_names())
print(db.list_collection_names())
print(songwriters.count_documents({}))
print(recordings.count_documents({}))