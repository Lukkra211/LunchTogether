import json
import requests


class Query:
    def __init__(self):
        self.url = "https://developers.zomato.com/api/v2.1/"
        self.usery_key = "7f2ad3893cfa728e2d322e4e8f34e0e6"

    def search_restaurant(self, **kwargs):
        self.url += "search?"
        for index,item in enumerate(kwargs):
            self.url += item + "=" + str(kwargs[item])
            if index!=len(kwargs)-1:
                self.url+="&"
        response=self.execute()
        return response

    def execute(self):
        data = requests.get(self.url,
                            headers={'Accept': 'application/json', "user-key": self.usery_key})
        return json.loads(data.text)
