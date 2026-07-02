# Land the Terminal UI Engine (Continuous Input Menu Loop)
# ------------------------------
# This script provides the terminal user interface for the inventory system.

import config
import engine
import database
import analytics
import os
import json
import datetime
import sys




def main_application():
    print("\n=======================================================")
    print(f"      ENTERPRISE INVENTORY CONSOLE v{config.VERSION}   ")
    print(f"      Session Administrator Profile: {config.CURRENT_USER}")
    print("=======================================================")
    print(" 1. View Inventory Status Map Summary")
    print(" 2. Provision / Restock New Item SKU")
    print(" 3. Open Terminal Point-of-Sale Checkout Window")
    print(" 4. Run Corporate Analytical Performance Reporting")
    print(" 5. Monitor System Safety Security Logs")
    print(" 6. Terminate Operational System Instance")
    print("=======================================================")


def view_inventory():
    print("\nCurrent Inventory:")
    if not config.GLOBAL_INVENTORY:
        print("Inventory is currently empty. Please restock items.")
        return
    for item in config.GLOBAL_INVENTORY:
        print(f"SKU: {item['sku']}, Name: {item['name']}, Stock: {item['stock']}, Price: ${item['price']:.2f}")


def view_system_logs():
    log_dir = getattr(database, 'DAT_DIR', 'enterprise_data')
    log_file_path = os.path.join(log_dir, 'system.log')
    if os.path.exists(log_file_path):
        with open(log_file_path, 'r') as log_file:
            logs = log_file.read()
            print("\nSystem logs")
            print(logs)
    else:
        print("No system logs found yet")


def main_application():
    config.GLOBAL_INVENTORY = database.load_data()

    while True:
        main_application()
        choice = input("Select your option (1-6): ").strip()

        if choice == '1':
            view_inventory()
        elif choice == '2':
            print("Provision/restock is not implemented yet.")
        elif choice == '3':
            print("Checkout is not implemented yet.")
        elif choice == '4':
            print("Reporting is not implemented yet.")
        elif choice == '5':
            view_system_logs()
        elif choice == '6':
            print("Exiting the window. Thank you for using the inventory management system!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if "__name__" == "__main__":
    main_application()


# This method is to check errors........
#after compiler respond succeeded, i will comment it in the last logic section 


# try:

#     main_application()
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
#     database.append_log(f"Unexpected error: {e}")
