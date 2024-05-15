import requests
import json
from abc import ABC,abstractmethod

class Request():

    def __init__(self,url):
        self.url = url

    def make_request(self, serch_query):
        params = {'text': serch_query, 'area' : "113", 'per_page': 100}
        response = requests.get(self.url,params=params)
        print(response.status_code)
        #print(response.text)
        data = response.json()
        print(data['items'])

        #print(response.json())


first_popitka= Request('https://api.hh.ru/vacancies')
first_popitka.make_request("Python")
