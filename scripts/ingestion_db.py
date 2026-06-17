import sqlite3
import pandas as pd
import os

# Files ke sahi paths set karein
db_path = "inventory.db"
csv_path = "vendor_sales_summary.csv"

# Agar file data folder ke andar hai toh aise path set karein:
if not os.path.exists(csv_path) and os.path.exists("data/vendor_sales_summary.csv"):
    csv_path = "data/vendor_sales_summary.csv"
    db_path = "data/inventory.db"

try:
    print("CSV file read ho rahi hai...")
    df = pd.read_csv(csv_path)
    
    print("SQLite Database se connect ho rahe hain...")
    conn = sqlite3.connect(db_path)
    
    print("Data ko 'vendor_sales_summary' table mein load kiya ja raha hai...")
    df.to_sql("vendor_sales_summary", conn, if_exists="replace", index=False)
    
    print("🔥 Data Ingestion Successful! Aapki 'inventory.db' wapas taiyar hai bhai.")
    
except Exception as e:
    print(f"Error aaya hai bhai: {e}")
    
finally:
    if 'conn' in locals():
        conn.close()