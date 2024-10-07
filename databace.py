import sqlite3

# Connect to the SQLite database
con = sqlite3.connect(r"data\data.db")
cur = con.cursor()

# SQL query to create the Amount_data table
query_amount = """
CREATE TABLE IF NOT EXISTS Amount_data (
    id_amount INTEGER PRIMARY KEY AUTOINCREMENT,
    current_time DATETIME NOT NULL,
    name TEXT,
    description TEXT,
    amount INTEGER
)
"""

# SQL query to create the customer_data table
query_customer = """
CREATE TABLE IF NOT EXISTS customer_data (
    order_number INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT,
    domain TEXT,
    description TEXT,
    price INTEGER,
    creation_time DATETIME NOT NULL,
    order_type TEXT,
    completion_time DATETIME NOT NULL,
    discount INTEGER,
    amount_received INTEGER,
    remaining_amount INTEGER,
    phone_number INTEGER
)
"""
# SQL query to create the income_data table
query_income = """
CREATE TABLE IF NOT EXISTS income_data (
    order_number INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    domain TEXT,
    amount_received INTEGER,
    discount INTEGER,
    creation_time DATETIME NOT NULL,
    price INTEGER,
    phone_number INTEGER
)
"""

# Execute the queries
cur.execute(query_amount)
cur.execute(query_customer)
cur.execute(query_income)

# Commit the changes
con.commit()

# Close the connection
cur.close()
con.close()
