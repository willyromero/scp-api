import requests
import urllib3
import requests
from pathlib import Path
import glob

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
            # path access for local ssl certificate of url
            curret_path = Path(__file__).parent.resolve()
            # certificate_path = curret_path / "cert" / "_.secap.gob.ec.crt"
            cert_path = curret_path / "cert"
            
            certificate_path = glob.glob(f"{cert_path}/*.crt")[0]
            # certificate_path = curret_path / "cert" / list(curret_path.glob("**/*.crt"))[1]

            request_text = requests.get(
                url=self.get_url(), 
                timeout=(self.get_timeout()),
                verify=certificate_path
            ).text 
            
            request_response = {"success": True, "request_text": request_text}
            
            self.set_web_content(request_response)
        except Exception as err:
            request_response = {"success": False,  "mensaje": err.args}
            self.set_web_content(request_response)
