import json
import requests

class API:

    def get_token(self, email, pwd):

        if not email or not pwd:
            raise Exception("Need both email and pwd")

        payload = {'email': email, 'password': pwd}
        r = requests.post(
            self.base + self.login_path,
            verify=False,
            json=payload
        )
        if r.status_code != 200:
            r.raise_for_status()
 
        return json.loads(r.text) 

    def plain_request(self, url):

        if not url:
            raise Excepion("Need url")

        r = requests.get(
            self.base + url,
            verify=False
        )
        if r.status_code != 200:
            r.raise_for_status()
        return json.loads(r.text)

    def __init__(self):
        self.base = "https://api.xg.football"
        self.login_path = '/user/login'
        return

