import json
import pymongo

#establishes connection with mongodb
conn = pymongo.MongoClient("mongodb://localhost")
#create database company
db=conn.company

#create collection project
record = db.project
#open project json file and read json data
file = open("C:/Users/rosha/Desktop/DB2/project.json", 'r')
parsed = json.loads(file1.read())
#insert json data to mongodb project collection
for item in parsed1["prjDetails"]:
    record.insert(item)
cursor = record.find()
for doc in cursor:
	print doc
	
#create collection department
record = db.department
#open department json file and read json data
file = open("C:/Users/rosha/Desktop/DB2/department.json", 'r')
parsed = json.loads(file.read())
#insert json data to mongodb department collection
for item in parsed["DeptDetails"]:
    record.insert(item)
cursor = record.find()
for doc in cursor:
	print doc