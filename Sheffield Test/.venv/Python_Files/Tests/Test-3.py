import unittest
from unittest.mock import patch, Mock
from requests.models import Response
from .. import ETL_Integration


class Test_Modify_And_Post_Customers(unittest.TestCase):

    @patch('requests.get')
    @patch('requests.post')
    def test_modify_and_post_customers(self, mock_post, mock_get):
        mock_get_response = Mock(spec=Response)
        mock_get_response.status_code = 200
        mock_get_response.json.return_value = [
            {'customer_id': 1, 'firstname': 'Alice', 'surname': 'Smith'},
            {'customer_id': 2, 'firstname': 'Bob', 'surname': 'Jones'}
        ]
        mock_get.return_value = mock_get_response

        mock_post_response = Mock(spec=Response)
        mock_post_response.status_code = 200
        mock_post.return_value = mock_post_response

        ETL_Integration.modify_and_post_customers()

        mock_get.assert_called_once_with('http://127.0.0.1:5000/customers')

        expected_data = [
            {'customer_id': 1, 'name': 'Alice Smith'},
            {'customer_id': 2, 'name': 'Bob Jones'}
        ]
        for customer_data in expected_data:
            mock_post.assert_any_call('https://postman-echo.com/post', json=customer_data)

        expected_call_count = len(expected_data)
        self.assertEqual(mock_post.call_count, expected_call_count)


if __name__ == '__main__':
    unittest.main()
