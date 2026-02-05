import json
import os

from core.db import get_db
from core.config import settings

def load_init_data():
    file_path = settings.DATA_PATH

    if not os.path.exists(file_path):
        print(f"Data file not found at path: {file_path}")
        return
    
    coll = settings.EMPLOYEES_COOL

    db = get_db()
    cool = db[coll]

    with open(file_path) as file:
        file_data = json.load(file)

    ins_result = cool.insert_many(file_data)

    print(f"Data inserted to MongoDB. Documents \
          inserted: {len(ins_result.inserted_ids)}")

