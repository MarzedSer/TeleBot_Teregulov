import json
import requests
from config import keys

class APIException (Exception):
    pass

class get_price:
    @staticmethod
    def get(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException (f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException (f'Не удалось обработать валюту{quote}')

        try:
            bae_ticker = keys[base]
        except KeyError:
            raise APIException (f'Не удалось обработать валюту{base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException (f'Не удалось обработать кол-во{amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
        total_base = json.loads(r.content)[keys[base]]
        total_base=total_base*amount

        return total_base