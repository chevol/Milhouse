import requests
import random
from bs4 import BeautifulSoup
from twilio.rest import Client
import time
import secrets

def get_page_html(page_url,site_headers):
    headers = site_headers
    page = requests.get(page_url, headers=headers)
    print(page.status_code)
    return page.content

def check_item_in_stock_amazon(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    out_of_stock_divs = soup.findAll("div", {"id": "outOfStock"})
    #print(soup.prettify())
    print(len(out_of_stock_divs) == 0)
    return len(out_of_stock_divs) == 0

def check_item_in_stock_bestbuy(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    out_of_stock_divs = soup.findAll("button", {"class": "btn btn-disabled btn-lg btn-block add-to-cart-button"})
    #print(soup.prettify())
    print(len(out_of_stock_divs) == 0)
    return len(out_of_stock_divs) == 0

def setup_twilio_client():
    account_sid = secrets.twilio_sid
    auth_token = secrets.twilio_token
    return Client(account_sid, auth_token)

def send_notification(url):
    twilio_client = setup_twilio_client()
    twilio_client.messages.create(
        body="Your item is now available!" + url,
        from_=secrets.twilio_from_number,
        to=secrets.twilio_send_sms_to
    )

def check_inventory():
    #AMAZON STOCK CHECK
    # if check_item_in_stock_amazon(get_page_html(secrets.amazon_url)):
    #     send_notification()
    #     print("Item is in stock at Amazon! " + secrets.url)
    # else:
    #     print("No Amazon Stock Recorded Yet")

    #BESTBUY STOCK CHECK
    print("Checking " + str(len(secrets.bestbuy_urls)) + " BestBuy links...")
    for iteration, url in enumerate(secrets.bestbuy_urls):
        print(str(iteration + 1) + ".) Checking BestBuy link - " + url)
        if check_item_in_stock_bestbuy(get_page_html(url,random.choice(list(secrets.bestbuy_headers)))):
            send_notification(url)
            print("Item is in stock at BestBuy! " + url)
        else:
            print("No BestBuy Stock Recorded Yet")
    print("   ")

while True:
    print("----------------------------------------------")
    try:
        check_inventory()
        time.sleep(165)
    except:
        print("An error occured trying to check inventory")
