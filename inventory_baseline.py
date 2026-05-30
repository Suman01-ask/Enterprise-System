import json
import os
import datetime
import time


DAT_DIR = "enterprise_data"
def load_date():
    with open(os.path.join(DAT_DIR, "data.json"), ",") as data_file:
        data = json.load(data_file) 

        return data
    
def save_data(data):
    with open(os.path.join(DAT_DIR, "data.json"), "w") as data_file:
        json.dump(data, data_file, indent=4)

        

