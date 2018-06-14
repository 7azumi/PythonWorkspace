from pymongo import MongoClient

conn = MongoClient("localhost",27017)

db = conn.mydb

collection = db.student

collection.insert(({"name":"Mike", "age":25, "gender":1, "address":"上海", "isDelete":0}))

conn.close()

