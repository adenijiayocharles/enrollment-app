from application import db

class User:
    def save(self):
        users = db['user']
        my_dict = {"name": "John", "age": 30, "city": "New York", "mopde": "ssdd"}
        users.insert_one(my_dict)