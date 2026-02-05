class MongoAlreadyExist(Exception):
    def __init__(self, message: str = ''):
        self.message = f"There is already a connection to Mongo. {message}"
        super().__init__(self.message)


class MongoNotExist(Exception):
    def __init__(self, message: str = ''):
        self.message = f"No connection to Mongo. {message}"
        super().__init__(self.message)