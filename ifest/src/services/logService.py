from config import get_database
from bson import ObjectId
from bson.json_util import dumps

db = get_database()
logdb = db["log"]
id = None

def inserirLog(msg):
    global id
    log = {'chat': [msg]}
    if id == None:
        result = logdb.insert_one(log)
        id = str(result.inserted_id)
    else:
        findlog = logdb.find_one({"_id": ObjectId(id)})
        findlog['chat'].append(msg)
        logdb.update_one(
            {"_id": ObjectId(id)}, 
            { "$set": 
                { "chat": findlog['chat']}})
    return id
