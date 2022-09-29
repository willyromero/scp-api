import requests
import urllib3
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


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
            # session = requests.Session()
            # # session.verify = "C:\\Users\\wrom\\Downloads\\_.secap.gob.ec.crt"
            # retry = Retry(connect=3, backoff_factor=0.5)
            # adapter = HTTPAdapter(max_retries=retry)
            # session.mount('http://', adapter)
            # session.mount('https://', adapter)
            # resp = session.get(self.get_url())


            # s = requests.Session()
            
            print("request", requests.get(url=self.get_url(), verify="C:\\Users\\wrom\\Downloads\\1_.secap.gob.ec.crt").text)

            # request_text = requests.get(
                # self.get_url(), timeout=(self.get_timeout()), verify="C:\\Users\\wrom\\Downloads\\_.secap.gob.ec.crt").text

            request_text = requests.get(url=self.get_url(), verify="C:\\Users\\wrom\\Downloads\\1_.secap.gob.ec.crt").text 
            request_response = {"success": True, "request_text": request_text}
            
            self.set_web_content(request_response)
        except Exception as err:
            request_response = {"success": False,  "mensaje": err.args}
            self.set_web_content(request_response)
