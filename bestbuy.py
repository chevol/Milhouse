from bs4 import BeautifulSoup
import secrets
import html_helper
import random
from twilio.rest import Client
import twilio_helper

class BestBuyChecker:
    def getpagehtml(self, url, headers):
        htmlhelper = html_helper.HtmlParser(url, headers)
        return htmlhelper.get_page_html()

    def check_item_in_stock(self, page_html):
        soup = BeautifulSoup(page_html, 'html.parser')
        out_of_stock_divs = soup.findAll("button", {"class": "btn btn-disabled btn-lg btn-block add-to-cart-button"})
        print("Div Found: " + str(len(out_of_stock_divs) == 0))
        return len(out_of_stock_divs) == 0

    def check_inventory(self):
        print("Checking " + str(len(secrets.bestbuy_urls)) + " BestBuy links...")
        for iteration, url in enumerate(secrets.bestbuy_urls):
            print("    ")
            print(str(iteration + 1) + ".) Checking BestBuy link - " + url)
            if self.check_item_in_stock(self.getpagehtml(url, random.choice(list(secrets.universal_headers)))):
                twiliohelper = twilio_helper.twilio()
                twiliohelper.send_notification(url)
                print("Item is in stock at BestBuy! " + url)
            else:
                print("No BestBuy Stock Recorded Yet")
        print("    ")