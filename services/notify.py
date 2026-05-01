import requests


class Notify:

    def __init__(self):
        self.__base_url = 'https://webhook.site'

    def send_event(self, data):
        requests.get(
            url=f'{self.__base_url}/e8230607-7581-4f0d-b12d-5bf0457e1b75',
            json=data
        )
