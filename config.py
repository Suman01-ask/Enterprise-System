# * config.py (The Central Filing Cabinet / Memory): This is a shared filing cabinet in the center of the office. It holds active data like who is logged in (CURRENT_USER) and the live inventory list (GLOBAL_INVENTORY). Any department can walk up, read from it, or update it instantly.

# This file is the central hub for shared data across the system. It contains variables that represent the current state of the system, such as who is logged in and what items are in the inventory. Other modules can import this file to access or modify this shared data.

#version of the application can be useful for logging and debugging purposes:
# lets define the version of the applocation, to keep track of updates and changes over the time. this can be useful to identify when centain features were added for the system and to esure compatibiltity with different modules of the systems.
#for now we wills set the version to 1.0 and we can update it as we add new featues and improvements to then systrms over thg periood of time. 

VERSION = "1.0" 


# Current logged-in user (None if no one is logged in)
CURRENT_USER = None

# Global inventory list (starts empty, will be populated from data.json)
GLOBAL_INVENTORY = []



