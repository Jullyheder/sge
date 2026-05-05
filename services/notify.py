import requests


class Notify:

    def __init__(self):
        self.__base_url = 'http://127.0.0.1:8001/'
        self.__path = 'api/v1/webhooks/order/'

    def send_order_event(self, data):
        requests.post(
            url=f'{self.__base_url}{self.__path}',
            json=data
        )
