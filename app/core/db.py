from pymongo import MongoClient

from core.config import settings
from core.exceptions import (MongoAlreadyExist,
                                 MongoNotExist)


class MongoManager:

    client = None

    @classmethod
    def connect(cls):
        if cls.client is not None:
            raise MongoAlreadyExist(f'url: {settings.MONGODB_URL} \
                                    db_name: {settings.DATABASE_NAME}')
        
        cls.client = MongoClient(
                    settings.MONGODB_URL,
                    maxPoolSize=50,
                    serverSelectionTimeoutMS=5000,
                    connectTimeoutMS=10000
                )

        cls.client.admin.command("ping")

        
    @classmethod
    def close(cls):
        if cls.client is None:
            raise MongoNotExist()
        
        cls.client.close()
        

def get_db():
    if MongoManager.client is None:
        raise MongoNotExist()
    
    db_name = settings.DATABASE_NAME  

    return MongoManager.client.get_database(name=db_name)