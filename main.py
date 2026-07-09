# Land the Terminal UI Engine (Continuous Input Menu Loop)
# ------------------------------
# Now that we have the core logic of our engine implemented we can now build the terminal user interface in main.py.
# This will be a continuous input loop that shows a menu of options to the user, collects theeir input, and calls the appropriate functions in engine.py based on their selections.
# Below is a simple implementation of the main.py file that provides a terminal-based`` user interface for our inventory system.


import config
import engine
import database
import analytics
import os
# import ast from lambda how to import this ? import ast 

# def main_menu(process_transaction, genrate_financialreport, view_inventory):
#     while True:
#         print("\n Welcome to the Inventory Management system!")
#         print("Please select an option:")
#         print("1. View Inventory")
#         print("2. Process a Transaction (checkout)")
#         print("3. Generate financial report")
#         print("4. Exit")
#         choice = input("Enter your choice (1-4): ")
#         if choice == '1':
#             view_inventory()
#         elif choice =='2':
#             process_transaction()
#         elif choice == '3':
#             genrate_financialreport()
#         elif choice == '4':
#             print("Exiting the window. Thank you for using the inventory management system!")
#             break

#         else:
#             print("Invalid choice. please select a valid option")

#         def view_inventory():
#             print("\nCurrent Inventory:")
#             for item in config.GLOBAL_INVENTORY:
#                 print(f"SKU: {item['sku']}, Name: {item['name']}, Stock: {item['stock']}, Price: ${item['price']:.2f}")

#                 def process_transaction():
#                     cart = []
#                     while True:
#                         sku = input ("Enter SKU of the item to add to cart (or 'done to finish): ")
#                         if sku.lower() == 'done':
#                             break
#                         quantity = int(input("Enter quantity: "))
#                         cart.append({'sku': sku, 'quantity': quantity})
#                     invoice = engine.process_transaction(cart)
#                     if isinstance(invoice, str):
#                         print(invoice) # this will print the error message if the transation is rejected
                    
#                     else :
#                         print(f"transaction successful! Invoice ID: {invoice['invoice_id']}, total cost: ${invoice['total_cost']:.2f}")

        
#         def generate_fanacial_report():
#             report = analytics.generate_financial_report()
#             print("\nFinancial Report:")
#             print(report)


#         if __name__ == "__main__":
#             #Load initial data from the database into the global inventory
#             config.GLOBAL_INVENTORY = database.load_data()
#             main_menu()

            
# #let integrate all the modules together in the main.py file, to create a cohesive inventory manaagement system.
# # The main_menu function provides a simple terminal-bases user interface that allow users to interact. 



# # def bootstrap_application():
# #     # load initial data ffrom the database into the global inventory
# #     config.GLOBAL_INVENTORY = database.load_data()
# #     main_menu(engine.process_transaction, analytics.generate_financial_repot, view_inventory= lambda: None)

# #     if __name__ == "__main__":
# #         bootstrap_application()

# print("--- TEST 1: IS PYTHON EVEN ALIVE? ---")

# if __name__ == "__main__":
#     print("--- TEST 2: THE TRIGGER BLOCK WORKS! ---")




#we will create these functions then we will project them to the application functionn in the main menu.


# def view_stock()
# def handle_add_sku()
# def handle_checkout()
# run_business_reports()
# def view_system_logs()
# def bootstrap_application()
#




def display_dashboard():
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

def handle_add_sku():
    sku = input("Enter new SKU code: ").strip().upper()
    name = input("Enter item name: ").strip()
    try:
        stock = int(input("Enter initial stock quantity: ").strip())
        price = float(input("Enter item price: ").strip())
    except ValueError:
        print("Invalid input for stock or price. please enter numeric values.")
        return
        
def handle_checkout():
    cart = []
    while True:
        sku = input("Enter SKU of the item to add to cart (or 'done' to finish): ").strip().upper()
        if sku.lower() == 'done':
            break
        try:
            quantity = int(input("ENter the quantity: ").strip())
        except ValueError:
            print("Invalid input for quantity. Please enter a numeric value.")
            continue
        cart.append({
            "sku": sku,
            "quantity": quantity
    })
        invoice = engine.process_transaction(cart)
        if isinstance(invoice, str):
            print(invoice) # This will print the errot mesage if the transation is rejected
        else:
            print(f"Transaction successfull! Invoicce ID: {invoice['invoice_id']}, total cost: ${invoice['total_cost']:.2f}")

def business_reports():
    report = analytics.generate_financial_report()
    print("\nFinancial Report:")
    print(report)

def view_system_logs():
    log_file_path = os.path.join(database.DAT_DIR, 'system.log')
    if os.path.exists(log_file_path):
        with open(log_file_path, 'r') as log_file:
            logs = log_file.read()
            print("\nsystem logs")
            print (logs)
        
    else:
        print("No system logs found yet")

def view_stock():
    print("\nCurrent Inventory:")
    for item in config.GLOBAL_INVENTORY:
        print(
            f"SKU: {item['sku']}, "
            f"Name: {item['name']}, "
            f"Stock: {item['stock']}, "
            f"Price: ${item['price']:.2f}"
        )

    if not config.GLOBAL_INVENTORY:
        print("Inventory is currently empty. Please restock items.")

def main_application():
    config.GLOBAL_INVENTORY = database.load_data()

    while True:
        display_dashboard()

        choice = input("Select your option: ").strip()

        if choice == "1":
            view_stock()

        elif choice == "2":
            handle_add_sku()

        elif choice == "3":
            print("Checkout functionality is currently unavailable.")

        elif choice == "4":
            business_reports()

        elif choice == "5":
            view_system_logs()

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid option. Please select a number between 1 and 6.")
            
#after imllementing __name__ = "__main__", and then calling main_application(), there should an output 
            
#no output because we have not implemented the main_application function yet, we will implement it in the next steps, and then we will see the output in the terminal when we run the main.py file.

#let's implement the main_application function, which will be the entry point of our application, and it will call the main_menu function to start the user interface loop.

# def main_application():
#     #load initial data from the database into the global inventory
#     config.GLOBAL_INVENTORY = database.load_data()
#     display_dashboard(engine.process_transaction, analytics.generate_financial_report, view_inventory= lambda: None)


# if __name__ == "__main__":
#     main_application()





# print("--- TEST 1: IS logic EVEN ALIVE? ---")

# if __name__ == "__main__":
#     print("--- TEST 2: THE TRIGGER BLOCK WORKS! ---")


# Now that we have call main_application() in the __nAME__"== __main__ block, output should be on terminal when we run the main.py file, and we should see the dashboard with the menu options for the user to interact with.

# We will implement the functions for each menu option in the next steps, and then we will have a fully functional terminal-based inventory management system.

# def main():
#     display_dashboard()



# if __name__ == "__main__":
#     main()


if __name__ == "__main__":
    main_application()