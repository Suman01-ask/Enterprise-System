# Build File I/O Logic (Read/Write JSON & Append Logs)
import json
import os
import datetime
import config


DAT_DIR = "enterprise_data"
ROOT_DATA_FILE = "data.json"
ALT_DATA_FILE = os.path.join(DAT_DIR, "data.json")


def _resolve_data_path():
    if os.path.exists(ALT_DATA_FILE):
        return ALT_DATA_FILE
    if os.path.exists(ROOT_DATA_FILE):
        return ROOT_DATA_FILE
    if os.path.isdir(DAT_DIR):
        return ALT_DATA_FILE
    return ROOT_DATA_FILE


def _initialize_data(path):
    payload = {"GLOBAL_INVENTORY": []}
    directory = os.path.dirname(path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
    with open(path, "w") as data_file:
        json.dump(payload, data_file, indent=4)
    return payload


def load_data():
    path = _resolve_data_path()

    try:
        with open(path, "r") as data_file:
            data = json.load(data_file)
    except (FileNotFoundError, json.JSONDecodeError):
        if path != ROOT_DATA_FILE and os.path.exists(ROOT_DATA_FILE):
            path = ROOT_DATA_FILE
            try:
                with open(path, "r") as data_file:
                    data = json.load(data_file)
            except (FileNotFoundError, json.JSONDecodeError):
                data = _initialize_data(ROOT_DATA_FILE)
        else:
            data = _initialize_data(path)

    if isinstance(data, dict) and "GLOBAL_INVENTORY" in data:
        return data["GLOBAL_INVENTORY"]
    if isinstance(data, list):
        return data
    return []


def append_log(message):
    log_path = os.path.join(os.path.dirname(_resolve_data_path()) or ".", 'system.log')
    with open(log_path, "a") as enterprise_log:
        timestamp = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
        enterprise_log.write(f"[{timestamp}] {message}\n")


def save_data(inventory):
    path = _resolve_data_path()
    if isinstance(inventory, list):
        payload = {"GLOBAL_INVENTORY": inventory}
    else:
        payload = inventory

    directory = os.path.dirname(path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

    with open(path, "w") as data_file:
        json.dump(payload, data_file, indent=4)


