import requests
from os import environ

class alpha_vantage_base:

    def __init__(self):
        self._API_KEY =  environ.get("AV_API_KEY")
        pass

    def time_series(self, ticker : str) -> str:
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={ticker}&apikey={self._API_KEY}'
        return requests.get(url)
