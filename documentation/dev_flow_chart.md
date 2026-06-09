

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





  Main.py (user interface)

  The primary rule of Phase 3 is separation of concerns: the interface file should only handle printing strings, collecting keyboard inputs, and calling functions from your backend modules. It should contain no calculations or direct file writing.🗺️ System Control Flow for Phase 3This flowchart maps how the execution loop starts, routes user choices to your Phase 2 modules, and loops indefinitely until a clean exit is triggered.  
  
  
  
                  ┌─────────────────────────┐
                  │    START: main.py       │
                  └────────────┬────────────┘
                               │
                               ▼
                  ┌─────────────────────────┐
                  │  database.load_all_data │ ◄── Read JSON files into memory 
                  └────────────┬────────────┘
                               │
                               ▼
                    ┌─────────────────────┐
             ┌─────►│  CORE TERMINAL LOOP │
             │      │    (while True)     │
             │      └──────────┬──────────┘
             │                 │
             │                 ▼
             │      ┌─────────────────────┐
             │      │  Display Menu &     │
             │      │  Capture input()    │
             │      └──────────┬──────────┘
             │                 │
             │                 ▼
             │       Evaluate User Choice (1-6)
             │                 │
    [Loop Back]       ┌────────┴────────┬─────────────────┐
             │        │ (Choice 1-5)    │ (Choice 6)      │ (Invalid)
             │        ▼                 ▼                 ▼
             │  ┌───────────┐    ┌─────────────┐   ┌─────────────┐
             │  │ Call Core │    │ Save Memory │   │ Print Error │
             │  │ Engine/   │    │ to Disk     │   └──────┬──────┘
             │  │ Analytics │    └──────┬──────┘          │
             │  └─────┬─────┘           │                 │
             │        │                 ▼                 │
             └────────┴─────────── [EXIT SYSTEM] ◄────────┘


