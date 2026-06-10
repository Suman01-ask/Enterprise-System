# The entire understanding of this system;
# To understand how this enterprise system works, think of it like a real-world physical retail store or warehouse.
# Instead of treating code as a single script, we treat it like a business with separate departments. Each file (module) represents a specific department in your company.
# Here is the exact blueprint of how data flows, how the modules talk to each other, and why this design is "enterprise-grade."
# ------------------------------
# ## 1. The Department Breakdown (The Architecture)
# Imagine your business has four main departments and a manager's office:

# [ main.py ]  <--->  [ engine.py ]  <--->  [ analytics.py ]
#     ^                     ^                      |
#     |                     v                      v
#     +---------------> [ config.py ] <------------+
#                           ^
#                           v
#                     [ database.py ]


# * config.py (The Central Filing Cabinet / Memory): This is a shared filing cabinet in the center of the office. It holds active data like who is logged in (CURRENT_USER) and the live inventory list (GLOBAL_INVENTORY). Any department can walk up, read from it, or update it instantly.

# * main.py (The Front Counter / User Interface): This is the cashier's terminal. It does no math and saves no files. It only talks to the customer (terminal user), shows menus, collects inputs, and passes them to the back office.

# * engine.py (The Back Office / Operations): This is where business rules are enforced. If the front counter asks to sell 10 items, the engine checks: "Do we actually have 10 items in stock?" or "Are prices positive numbers?" If yes, it creates an invoice and updates the inventory.

# * analytics.py (The Accountant): This department looks at raw data and calculates business metrics. It figures out tax collection, profit margins, and scans for low stock.
# * database.py (The Security Vault / Permanent Storage): This handles physical files. When the system boots up, it reads data from your hard drive (.json files) and puts it in the central cabinet (config.py). When you close the app, it locks everything down onto the hard drive so data isn't lost.

# ------------------------------
# ## 2. The Lifecycle of a Action (How Data Flows)
# Let’s trace exactly what happens behind the scenes when a user selects Option 3: Process a Transaction (Checkout).
# ## Phase A: Verification (The Engine Check)

#    1. You type a SKU code and quantity into main.py.
#    2. main.py calls a function inside engine.py: process_transaction(cart).
#    3. engine.py looks inside the central filing cabinet (config.py) to see if that SKU exists and checks if the warehouse has enough physical stock.
#    4. If there isn't enough stock, engine.py instantly sends a rejection warning back to main.py to show on screen.

# ## Phase B: Mutation (The Global State Update)

#    1. If stock is available, engine.py subtracts the sold items directly from the live GLOBAL_INVENTORY inside config.py.
#    2. engine.py automatically generates a unique invoice tracking number, calculates the 8% tax rate, and appends the final transaction sheet to GLOBAL_INVOICES.

# ## Phase C: Durability (The Database & Logging Flush)

#    1. engine.py alerts database.py that a change occurred.
#    2. database.py takes the new records and writes them out into physical files on your computer (inventory.json and invoices.json).
#    3. Simultaneously, database.py logs a timestamped security record to system.log:
#    * [2026-05-29 16:57:00] [SALES_DEAL] (Guest_Admin) -> Invoice INV-1716... closed.
#    4. Finally, main.py prints a beautiful clean terminal receipt for the user.

# ------------------------------
# ## 🚀 Why This Approach Matters (Enterprise Concepts)

# * No "Spaghetti Code": If your math is wrong, you only fix analytics.py. If you want to switch from text menus to a visual desktop application later, you only rewrite main.py—your business logic, databases, and configuration code remain entirely untouched.
# * Global State Pattern: By importing config across multiple files, different modules safely read and mutate the exact same in-memory dataset simultaneously without passing dozens of chaotic arguments through functions.
# * Crash Prevention: Enterprise programs should never abruptly crash. Because processing logic is separated from file loading, if a file fails to read, database.py flags an error safely while main.py keeps the system running smoothly.

# ------------------------------
