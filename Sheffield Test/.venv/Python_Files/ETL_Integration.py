from apscheduler.schedulers.blocking import BlockingScheduler
import requests

scheduler = BlockingScheduler()

@scheduler.scheduled_job('interval', hours=1)
def scheduled_job():
    response = requests.get('http://localhost:5000/customers?status=active')
    active_customers = response.json()
    for customer in active_customers:
        customer['name'] = f"{customer['firstname']} {customer['surname']}"
        payload = {'customer': customer}
        target_response = requests.post('https://postman-echo.com/post', json=payload)
        print(target_response.status_code)

scheduler.start()
