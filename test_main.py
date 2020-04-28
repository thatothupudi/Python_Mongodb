from main import create_one_visitor,create_multiple_visitor, update_visitor,list_visitors,one_visitor,visitor_details
from mongodb import MongoDB
import pytest
import json

@pytest.fixture()
def db():
    db = MongoDB("db.collection_visitor")
    yield db
    db.collection_visitor.purge(db)
    # return db.collection_visitor

def test_create_one_visitor(db):
    db.collection_visitor.insert({"name": "Tello Mojela"})
    assert len(db.all()) == 1

def test_create_multiple_visitors(db):
    db.collection_visitor.insert_multiple([
    {"name": "Mthokozisi Shabangu"}, {"name": "Monica Thulo"}])
    assert len(db.all()) == 2
    

