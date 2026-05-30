# * config.py (The Central Filing Cabinet / Memory): This is a shared filing cabinet in the center of the office. It holds active data like who is logged in (CURRENT_USER) and the live inventory list (GLOBAL_INVENTORY). Any department can walk up, read from it, or update it instantly.

# This file is the central hub for shared data across the system. It contains variables that represent the current state of the system, such as who is logged in and what items are in the inventory. Other modules can import this file to access or modify this shared data.

# Current logged-in user (None if no one is logged in)
CURRENT_USER = None

# Global inventory list (starts empty, will be populated from data.json)
GLOBAL_INVENTORY = []


