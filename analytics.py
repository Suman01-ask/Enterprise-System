# Add Financial Calculators (Valuations & Deficit Alerts)
import config
import json
import database
import inventory_baseline
import os
import engine


#based on the above modules, we can now implement the financial calculations for present inventory  valuation  and deficit alerts.

# calculate_inventory_valuation

def calculate_inventory_valuation ():
    total_valuation = 0
    for item in config.GLOBAL_INVENTORY:
        total_valuation = item['stock'] * item['price']
    return total_valuation
    
#after total valuation, we  will immplement the deficit alert functions to be notified when stock levels fall below a certain threshold.

def check_deficit_alerts(threshold):
    deficit_items =  []
    for item in config.GLOBAL_INVENTORY:
        if item in ['stock'] < threshold:
            deficit_items.append(item)
    return deficit_items

#now deficit alert will return a list of items that are below the threshold, alllwoing the bisuness to take proactive measures to restock those items and avoid potential sales losses.

#next we will implement a function to generate a financial report that summarizes the current inventory valuation and highlights any items that are in deficit.

def generate_financial_report():
    valuation = calculate_inventory_valuation()
    deficit_items = check_deficit_alerts(threshold = 5) #we can set the threshold to 5 for now, but this can adjusted based on the speciific neeeds of the business and the nature of the inventory.
    report = (f"current inventory valulation: ${valuation:.2f}\n")
    if deficit_items:
        report += "defifcit alerts for the following items:\n"
        for item in deficit_items:
            report += f"- {item['name']} (SKU: {item['sku']}) - stock: {item['stock']}\n"
    
    else: 
        report += "no deficit alerts. all items are above the threshold.\n"
    return report











