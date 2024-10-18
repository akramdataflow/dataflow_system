<<<<<<< Updated upstream
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
    phone_number INTEGER,
    FOREIGN KEY (order_number) REFERENCES customer_data(order_number),
    FOREIGN KEY (name) REFERENCES customer_data(customer_name),
    FOREIGN KEY (domain) REFERENCES customer_data(domain),
    FOREIGN KEY (amount_received) REFERENCES customer_data(amount_received),
    FOREIGN KEY (discount) REFERENCES customer_data(discount),
    FOREIGN KEY (creation_time) REFERENCES customer_data(creation_time),
    FOREIGN KEY (price) REFERENCES customer_data(price),
    FOREIGN KEY (phone_number) REFERENCES customer_data(phone_number)
)
"""

query_representatives = '''CREATE TABLE IF NOT EXISTS representatives(name TEXT, 
        comapany_name TEXT,
        phone_number INTEGER, 
        price INTEGER, 
        date DATETIME)'''

# Execute the queries
cur.execute(query_amount)
cur.execute(query_customer)
cur.execute(query_income)
cur.execute(query_representatives)


# Commit the changes
con.commit()

# Close the connection
cur.close()
con.close()
=======
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
    phone_number INTEGER,
    FOREIGN KEY (order_number) REFERENCES customer_data(order_number),
    FOREIGN KEY (name) REFERENCES customer_data(customer_name),
    FOREIGN KEY (domain) REFERENCES customer_data(domain),
    FOREIGN KEY (amount_received) REFERENCES customer_data(amount_received),
    FOREIGN KEY (discount) REFERENCES customer_data(discount),
    FOREIGN KEY (creation_time) REFERENCES customer_data(creation_time),
    FOREIGN KEY (price) REFERENCES customer_data(price),
    FOREIGN KEY (phone_number) REFERENCES customer_data(phone_number)
)
"""

query_representatives = '''CREATE TABLE IF NOT EXISTS representatives(name TEXT, 
        comapany_name TEXT,
        phone_number INTEGER, 
        price INTEGER, 
        date DATETIME)'''

# Execute the queries
cur.execute(query_amount)
cur.execute(query_customer)
cur.execute(query_income)
cur.execute(query_representatives)


# Commit the changes
con.commit()

# Close the connection
cur.close()
con.close()
>>>>>>> Stashed changes
