import json

import requests


def get_currency(currency_abbreviation: str) -> json:
    currency_abbreviation = currency_abbreviation.upper()
    request = requests.get(f'https://economia.awesomeapi.com.br/all/{currency_abbreviation}-BRL')
    cotacao = request.json()
    return cotacao
