import db_connect as dbc
import pymongo as pm

COLLECT_NAME = "users"

print("not using db_connect")
DB_NAME = "chatDB"
client = pm.MongoClient("mongodb+srv://aliahjefree:VNOAxCoN35OhdcE4\
@cluster0.bslxs.mongodb.net/chatDB?retryWrites=true&w=majority")
print(f"{client=}")

docs = client[DB_NAME][COLLECT_NAME].find()
print(f"{docs=}")

for doc in docs:
    print(f"{doc=}")

print("using db_connect")
client = dbc.get_client()
print(f"{client=}")

docs = client[dbc.db_nm][COLLECT_NAME].find()
print(f"{docs=}")
for doc in docs:
    print(f"{doc=}")
