import requests

class HtmlParser:
    def __init__(self,page_url,headers):
        self.page_url = page_url
        self.site_headers = headers

    def get_page_html(self):
        headers = self.site_headers
        page = requests.get(self.page_url,headers=headers)
        print("URL Status: " + str(page.status_code))
        return page.content