import requests
import urllib3

urllib3.disable_warnings()


# Class for request web content
class SecapScraper:

    def __init__(self, url, to):
        self.url = url
        self.timeout = to
        self.web_content = {}

    def get_url(self):
        return self.url

    def set_url(self, url):
        self.url = url

    def get_web_content(self):
        return self.web_content

    def set_web_content(self, web_content):
        self.web_content = web_content

    def get_timeout(self):
        return self.timeout

    def extract_web_content(self):
        try:
            request_text = requests.get(
                self.get_url(), verify=False, timeout=(self.get_timeout())).text
            request_response = {"success": True, "request_text": request_text}
            
            self.set_web_content(request_response)
        except:
            request_response = {"success": False}
            self.set_web_content(request_response)
