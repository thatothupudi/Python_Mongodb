from pymongo import MongoClient
from pymongo import ReturnDocument
from pprint import pprint
from bson.objectid import ObjectId

client = MongoClient("mongodb://root:pass@localhost:27017/")
db = client["umuziprospect"]
visitor = db["visitor"] 

        
def create_one_visitor(visitor):
    db.collection_visitor.insert_one({
    "name": "Tello Mojela",
    "age": 26,
    "date_of_visit": "2020-01-01",
    "time_of_visit": "13h43",
    "name_of_assistor": "Juliet Simpson",
    "comments": "I got the best assistance"
    })
visitor = create_one_visitor('')
print(visitor)


def create_multiple_visitor(visitor):
    db.collection_visitor.insert_many(
    [
    {
    "name": "Mthokozisi Shabangu",
    "age": 27,
    "date_of_visit": "1993-04-21",
    "time_of_visit": "08h12",
    "name_of_assistor": "Susan Khoza",
    "comments": "I didn't get the best service"
    },
    {
    "name": "Monica Thulo",
    "age": 45,
    "date_of_visit": "2020-02-10",
    "time_of_visit": "19h01",
    "name_of_assistor": "Jessica Kraver",
    "comments": "It wasn't that bad"
    }                            
    ]                        
    )
visitor = create_multiple_visitor('')
print(visitor)


def update_visitor(visitor):
    db.collection_visitor.update_one(
    {"name": "Tello Mojela"},
     {"$set": { "age": 18 } }
    )
visitor = update_visitor('')
print(visitor)

   
def list_visitors(visitor):

    for every_visitor in db.collection_visitor.find({}):
        print(every_visitor)
visitor = list_visitors('') 
      

def one_visitor(visitor):
    
    for each_visitor in db.collection_visitor.find({"name": "Monica Thulo"}):
        print(each_visitor)
visitor = one_visitor('')
print(visitor)        


def visitor_details(visitor):
    
    details = { "_id" : ObjectId("5ea7b4f204eddfc782e58b0b") }
    visitor = db.collection_visitor.find(details)
    return visitor
    print(visitor)

visitor = visitor_details('')


def delete_one_visitor(visitor):
    db.collection_visitor.delete_one({"name": "Tello Mojela"})

visitor = delete_one_visitor('')
print(visitor)


def delete_all_visitors(visitor):
    db.collection_visitor.drop()

visitor = delete_all_visitors('')
print(visitor)