[ PHASE 1: FOUNDATION ]
         │
         ▼
 ┌───────────────┐
 │   config.py   │ ◄─── Establish Global Variable Namespace (In-Memory DB)
 └───────┬───────┘
         │
         ▼
 ┌───────────────┐
 │  database.py  │ ◄─── Build File I/O Logic (Read/Write JSON & Append Logs)
 └───────┬───────┘
         │
         ▼
[ PHASE 2: CORE LOGIC ]
         │
         ▼
 ┌───────────────┐
 │   engine.py   │ ◄─── Implement Business Rules (SKU Registry & Stock Verifications)
 └───────┬───────┘
         │
         ▼
 ┌───────────────┐
 │ analytics.py  │ ◄─── Add Financial Calculators (Valuations & Deficit Alerts)
 └───────┬───────┘
         │
         ▼
[ PHASE 3: INTERFACE ]
         │
         ▼
 ┌───────────────┐
 │    main.py    │ ◄─── Land the Terminal UI Engine (Continuous Input Menu Loop)
 └───────────────┘





Analytics flow chart 

                ┌──────────────────────────────┐
                │          config.py           │
                │  (Global In-Memory Storage)  │
                └──────────────┬───────────────┘
                               │
            Pulls Raw          │          Pulls Raw
          Inventory Data       │        Invoice Data
                               ▼
     ┌──────────────────────────────────────────────────┐
     │                   analytics.py                   │
     └─────────┬──────────────────────────────┬─────────┘
               │                              │
               ▼                              ▼
  ┌─────────────────────────┐    ┌─────────────────────────┐
  │     VALUATION ENGINE    │    │      SALES ENGINE       │
  │  (inventory_valuation)  │    │    (sales_summary)      │
  └────────────┬────────────┘    └────────────┬────────────┘
               │                              │
               ▼                              ▼
     Loops through SKUs to          Loops through Invoices
     calculate Total Cost,          to aggregate revenue,
     Retail, and Margins            tax, and unit volumes
               │                              │
               ▼                              ▼
  ┌─────────────────────────┐    ┌─────────────────────────┐
  │ RETURN: Data Dictionary │    │ RETURN: Data Dictionary │
  │ {cost, retail, profit}  │    │ {gross, net, tax, qty}  │
  └─────────────────────────┘    └─────────────────────────┘