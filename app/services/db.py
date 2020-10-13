from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['microcontroller-project']
collection = db['MCU-data-1']

def insert_records_to_db(records):
    print(records)
    record_ids = collection.insert_many(records).inserted_ids
    print(record_ids)
    if record_ids:
        return True
    return False