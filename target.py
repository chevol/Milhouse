from bs4 import BeautifulSoup
import secrets
import html_helper
import random
from twilio.rest import Client
import twilio_helper

class TargetChecker:
    def getpagehtml(self,url,headers):
        htmlhelper = html_helper.HtmlParser(url,headers)
        return htmlhelper.get_page_html()

    def check_item_in_stock(self, page_html):
        print("Location in Script: " + str(page_html.decode("utf-8").find('available_to_purchase_date_display')))
        return int(str(page_html.decode("utf-8").find('available_to_purchase_date_display'))) >= 0

    def check_inventory(self):
        print("Checking " + str(len(secrets.target_urls)) + " Target links... ")
        for iteration, url in enumerate(secrets.target_urls):
            print("    ")
            print(str(iteration + 1) + ".) Checking Target link - " + url)
            if self.check_item_in_stock(self.getpagehtml(url,random.choice(list(secrets.universal_headers)))):
                twiliohelper = twilio_helper.twilio()
                twiliohelper.send_notification(url)
                print("Item is in stock at Target! " + url)
            else:
                print("No Target Stock Recorded Yet")
        print("    ")