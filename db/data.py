"""
This file will manage interactions with our data store.
At first, it will just contain stubs that return fake data.
Gradually, we will fill in actual calls to our datastore.
"""

import os

import db.db_connect as dbc

DEMO_HOME = os.environ["DEMO_HOME"]
TEST_MODE = os.environ.get("TEST_MODE", 0)

if TEST_MODE:
    # this one should be changed!
    DB_NAME = "chatDB"
else:
    DB_NAME = "chatDB"

ROOMS = "rooms"
USERS = "users"

# field names in our DB:
USER_NM = "userName"
ROOM_NM = "roomName"
NUM_USERS = "num_users"

OK = 0
NOT_FOUND = 1
DUPLICATE = 2

# we'll begin cutting over to mongo!
client = dbc.get_client()
print(client)


def get_rooms():
    """
    A function to return a dictionary of all rooms.
    """
    return dbc.fetch_all(ROOMS, ROOM_NM)


def room_exists(roomname):
    rooms = get_rooms()
    return roomname in rooms


def del_room(roomname):
    """
    Delete roomname from the db.
    """
    if not room_exists(roomname):
        return NOT_FOUND
    return OK


def add_room(roomname):
    """
    Add a room to the room database.
    """
    rooms = get_rooms()
    if rooms is None:
        return NOT_FOUND
    elif roomname in rooms:
        return DUPLICATE
    else:
        rooms[roomname] = {"num_users": 0}
        dbc.insert_doc(ROOMS, {ROOM_NM: roomname, NUM_USERS: 0})
        return OK


def get_users():
    """
    A function to return a dictionary of all users.
    """
    return dbc.fetch_all(USERS, USER_NM)


def add_user(username):
    """
    Add a user to the user database.
    Until we are using a real DB, we have a potential race condition here.
    """
    users = get_users()
    if users is None:
        return NOT_FOUND
    elif username in users:
        return DUPLICATE
    else:
        dbc.insert_doc(USERS, {USER_NM: username})
        return OK
