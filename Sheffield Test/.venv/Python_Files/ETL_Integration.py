import requests


def modify_and_post_customers():
    response = requests.get('http://127.0.0.1:5000/customers')
    customer_data = response.json()

    for customer in customer_data:
        customer['name'] = customer['firstname'] + ' ' + customer['surname']
        del customer['firstname']
        del customer['surname']

    target_url = 'https://postman-echo.com/post'

    for customer in customer_data:
        response = requests.post(target_url, json=customer)
        if response.status_code == 200:
            print(f'Success: HTTP Response Code - {response.status_code}')
        else:
            print(f'Failed: HTTP Response Code - {response.status_code}')
            print(response.text)


modify_and_post_customers()
