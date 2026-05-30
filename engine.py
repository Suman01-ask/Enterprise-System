# Implement Business Rules (SKU Registry & Stock Verifications)

# In this section, we will write the core operations logic for our inventory system. This is where we enforce business rules like SKU validation and stock checks.
# The main function we will implement is process_transaction(cart), which takes a shopping cart (a list of items and quantities) and processes it according to the following rules:

# 1. SKU Validation: For each item in the cart, we check if the SKU exists in our GLOBAL_INVENTORY. If any SKU is invalid, we reject the entire transaction and return an error message.    
# 2. Stock Verification: If all SKUs are valid, we then check if the requested quantity for each item is available in stock. If any item does not have enough stock, we reject the transaction and return an error message indicating which item is out of stock.
# 3. If all items pass validation and stock checks, we proceed to calculate the total cost, generate an invoice, and update the GLOBAL_INVENTORY accordingly.       

# ------------------------------
# ## 🧱 3. Implementing the Engine (The Back Office Logic
# The engine.py file is where we will implement the core business logic of our inventory system. This includes functions for processing transactions, validating SKUs, checking stock levels, and updating the inventory.
# Below is a step-by-step implementation of the process_transaction(cart) function, along with helper functions for SKU validation and stock verification.

import config
import database
import json
import os

# lets now build the logic now

def process_transaction(cart):
    #the first step is to validate the SKU in the cart
    for item in cart:
        sku_item = item['sku']
        quantity = item['quantity']
        if not validate_sku(sku_item):
            return f"Error: SKU {sku_item} is invalid. Transation  rejected."
        if not check_stock{sku_item}, {qauntity}:
            return f"Error: Not enouth stock for SKU {sku_item}. Transation rejected."
        
        #If all ites are valaid and in stock, we proceed to calculate the total cost and update the inventory
        total_cost = calculate_total(cart)
        invoice = generate_invoice(cart, total_cost) # genrate_invoice will be defined in next module of inventory data
        update_inventory(cart)  # update_inventory will be defined the cnfog data
        database.append_log(f"Transaction processed successfully. Invoice: {invoice['invoice_id']}, Total_cost: {total_cost}")
        return invoice
    
    def validate_sku(sku):
        for item in config.GLOBAL_INVENTORY:
            if item['sku'] == sku:
                return True
        return False
    

# now we will implement the check_stock function to verify if the requested quantity for each item is available in stock.

def check_stock(sku, quanity):
    for item in config.GLOBAL_INVENTORY:
        if item['sku'] == sku:
            return item['stock'] >= quanity
        return False
    
#next we  will impleyment the calculate_total function to compute the total cost of the transaction based on the items in the cart and their prices.


# this will calculate the total cost of the transactions based on the items in the cart and their corresponding prices.
def calculate_total(cart):
    total_cost = 0 
    for item in cart: 
        sku_item = item['sku']
        quantity = item['quantity']
        for inventoey_item in  config.GLOBAL_INVENTORY:
            if inventoey_item ['sku'] == sku_item :
                total_cost += inventoey_item['price'] * quantity #pricre will be defined in the inventory data.
    return total_cost


        