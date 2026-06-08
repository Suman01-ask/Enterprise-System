import json
import os
import datetime
import time
import config 



DAT_DIR = "enterprise_data"
def load_date():
    with open(os.path.join(DAT_DIR, "data.json"), ",") as data_file:
        data = json.load(data_file) 

        return data
    
def save_data(data):
    with open(os.path.join(DAT_DIR, "data.json"), "w") as data_file:
        json.dump(data, data_file, indent=4)

def append_log(mesage):
    with open(os.path.join(DAT_DIR, 'system.log'), "a") as enterprise_log:
        timestamp = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
        log_entry = f"[{timestamp}] {mesage}\n"
        enterprise_log.write(log_entry)



