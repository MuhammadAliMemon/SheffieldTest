import unittest
import requests


class Test_API(unittest.TestCase):

    def test_customers_route(self):
        response = requests.get('http://127.0.0.1:5000/customers')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['content-type'], 'application/json')

    def test_customers_by_id_route(self):
        response = requests.get('http://127.0.0.1:5000/customers/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['content-type'], 'application/json')

    def test_orders_route(self):
        response = requests.get('http://127.0.0.1:5000/orders')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['content-type'], 'application/json')

    def test_nonexistent_customer_route(self):
        response = requests.get('http://127.0.0.1:5000/customers/1010')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
