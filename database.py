# Build File I/O Logic (Read/Write JSON & Append Logs)
import json
import os
import datetime
import time
import config


DAT_DIR = "enterprise_data"
def load_data():
    with open(os.path.join(DAT_DIR, "data.json"), "r") as data_file:
        data = json.load(data_file)

        return data
    
# append log file with timestamp and message

def append_log(mesage):
    with open(os.path.join(DAT_DIR, 'system.log'), "a") as enterprise_log:
        timestamp = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
        log_entry = f"[{timestamp}] {mesage}\n"
        enterprise_log.write(log_entry)

