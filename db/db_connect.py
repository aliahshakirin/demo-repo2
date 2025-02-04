"""
This file contains some common MongoDB code.
"""
import os
import json
import pymongo as pm
import bson.json_util as bsutil

# all of these will eventually be put in the env:
user_nm = "aliahjefree"
cloud_db = "@cluster0.bslxs.mongodb.net"
passwd = os.environ.get("MONGO_PASSWD", '')
cloud_svc = "mongodb+srv"
db_params = "retryWrites=true&w=majority"
db_nm = "chatDB"

if os.environ.get("TEST_MODE", ''):
    db_nm = "test_chatDB"

REMOTE = 0
LOCAL = 1

client = None


def get_client():
    """
    This provides a uniform way to get the client across all uses.
    Returns a mongo client object... maybe we shouldn't?
    Also set global client variable.
    """
    global client
    if os.environ.get("LOCAL_MONGO", False):
        client = pm.MongoClient()
    else:
        print("Connecting to Mongo remotely.")
        client = pm.MongoClient(f"mongodb+srv://aliahjefree:{passwd}\
@cluster0.bslxs.mongodb.net/{db_nm}?retryWrites=true&w=majority")
    return client


def fetch_one(collect_nm, filters={}):
    """
    Fetch one record that meets filters.
    """
    return client[db_nm][collect_nm].find_one(filters)


def del_one(collect_nm, filters={}):
    """
    Delete one record that meets filters.
    """
    return client[db_nm][collect_nm].delete_one(filters)


def fetch_all(collect_nm, key_nm):
    all_docs = []
    for doc in client[db_nm][collect_nm].find():
        all_docs.append(json.loads(bsutil.dumps(doc)))
    return all_docs


def fetch_all_as_dict(collect_nm, key_nm):
    all_list = fetch_all(collect_nm, key_nm)
    all_dict = {}
    for doc in all_list:
        all_dict[doc[key_nm]] = doc[key_nm]
    return all_dict


def insert_doc(collect_nm, doc):
    client[db_nm][collect_nm].insert_one(doc)
