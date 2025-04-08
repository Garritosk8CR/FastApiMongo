from pymongo import MongoClient

client = mongo.MongoClient("mongodb+srv://emiliogarrorangelpc:1A0b2C9d3E@cluster0.nkufong.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.todo_db

collection_name = db["todo_collection"]