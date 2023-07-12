import schedule
import time
import requests
from credentials import mobile_no


def send_message():
    resp =requests.post('https://textbelt.com/', {
        'phone': mobile_no,
        "message": 'hey, goood moorning  ',
        'key': 'textbelt'
    })
    print(resp.json())

#schedule.every().day.at('06.00').do(send_message())

schedule.every(10).seconds.do(send_message())

while True:
    schedule.run_pending()
    time.sleep(1)
