import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
import time
import secrets

def get_page_html():
    url = secrets.url
    headers = secrets.headers
    page = requests.get(url, headers=headers)
    print(page.status_code)
    return page.content

def check_item_in_stock(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    out_of_stock_divs = soup.findAll("div", {"id": "outOfStock"})
    #print(soup.prettify())
    print(len(out_of_stock_divs) == 0)
    return len(out_of_stock_divs) == 0

def setup_twilio_client():
    account_sid = secrets.twilio_sid
    auth_token = secrets.twilio_token
    return Client(account_sid, auth_token)

def send_notification():
    twilio_client = setup_twilio_client()
    twilio_client.messages.create(
        body="Your item is now available!" + secrets.url,
        from_=secrets.twilio_from_number,
        to=secrets.twilio_send_sms_to
    )

def check_inventory():
    if check_item_in_stock(get_page_html()):
        send_notification()
        print("Item is in stock!")
    else:
        print("No Stock Recorded Yet")

while True:
    check_inventory()
    time.sleep(60)
