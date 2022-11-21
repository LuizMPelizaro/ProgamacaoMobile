import json

import requests


def get_currency(currency_abbreviation: str) -> json:
    currency_abbreviation = currency_abbreviation.upper()
    request = requests.get(f'https://economia.awesomeapi.com.br/all/{currency_abbreviation}-BRL')
    cotacao = request.json()
    return cotacao


def get_five_day_cotation(currency_abbreviation: str) -> json:
    currency_abbreviation = currency_abbreviation.upper()
    request = requests.get(f'https://economia.awesomeapi.com.br/json/daily/{currency_abbreviation}/5')
    cotacao = request.json()
    return cotacao


def multiple_quote(currency_abbreviation_1: str, currency_abbreviation_2: str, currency_abbreviation_3: 3) -> json:
    currency_abbreviation_1 = currency_abbreviation_1.upper()
    currency_abbreviation_2 = currency_abbreviation_2.upper()
    currency_abbreviation_3 = currency_abbreviation_3.upper()
    request = requests.get(
        f'https://economia.awesomeapi.com.br/json/last/{currency_abbreviation_1}-BRL,{currency_abbreviation_2}-BRL,'
        f'{currency_abbreviation_3}-BRL'
    )
    cotacao = request.json()
    return cotacao
