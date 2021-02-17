import requests
import logging

logging.basicConfig(filename='milhouse.log',format='%(asctime)s - %(message)s', datefmt='%B %d, %Y %I:%M:%S %p')

class HtmlParser:
    def __init__(self,page_url,headers):
        self.page_url = page_url
        self.site_headers = headers

    def get_page_html(self):
        headers = self.site_headers
        page = requests.get(self.page_url,headers=headers)
        if not str(page.status_code) == '200':
            logging.error(f'Get Page HTML Error - URL ({self.page_url}) Returned a {str(page.status_code)} Status Code')
        print('URL Status: ' + str(page.status_code))
        return page.content
