import json_handler as J

def load_database(path="./database.json"):
    return json_handler.read()



json_handler = J.json_handler(key_dir='./encryption/')
