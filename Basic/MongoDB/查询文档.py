from pymongo import MongoClient

conn = MongoClient("localhost",27017)

db = conn.mydb

collection = db.student

res = collection.find({"age":{"$gt":20}})
for row in res:
    print(row)

conn.close()