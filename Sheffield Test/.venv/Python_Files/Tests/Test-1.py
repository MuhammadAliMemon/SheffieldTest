import unittest
import sqlite3


class Test_Database_Creation(unittest.TestCase):

    def setUp(self):
        self.connection = sqlite3.connect(":memory:")
        self.cursor = self.connection.cursor()

        self.cursor.execute('''
                            CREATE TABLE Customers(
                            customer_id INTEGER PRIMARY KEY,
                            firstname TEXT ,
                            surname TEXT ,
                            email TEXT ,
                            address TEXT ,
                            zip_code TEXT ,
                            region TEXT ,
                            status TEXT   
                                        )''')

        self.cursor.execute('''
                        CREATE TABLE Orders(
                        order_id INT PRIMARY KEY,
                        date TEXT,
                        customer_id INTEGER,
                        amount REAL
                        )''')

    def test_table_creation(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Customers'")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)

        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Orders'")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)

    def tearDown(self):
        self.connection.close()


if __name__ == '__main__':
    unittest.main()
