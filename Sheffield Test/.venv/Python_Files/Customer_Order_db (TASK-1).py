import pandas as pd
import sqlite3

customers = pd.read_csv('../CSV_Files/customers.csv')

orders = pd.read_csv('../CSV_Files/orders.csv')

connection = sqlite3.connect("Customer_Order.db")
cursor = connection.cursor()

cursor.execute('''CREATE TABLE Customers (
                customer_id INTEGER PRIMARY KEY,
                firstname TEXT ,
                surname TEXT ,
                email TEXT ,
                address TEXT ,
                zip_code TEXT ,
                region TEXT ,
                status TEXT
                )''')

cursor.execute('''CREATE TABLE Orders (
                order_id INT PRIMARY KEY,
                date TEXT,
                customer_id INTEGER,
                amount REAL
                )''')

customers.to_sql(name="Customers", con=connection, if_exists='replace', index=False)

orders.to_sql(name='Orders', con=connection, if_exists='replace', index=False)

connection.commit()
connection.close()
