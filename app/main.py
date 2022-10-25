from datetime import datetime
import sqlite3
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp

from function.gets import get_currency, get_five_day_cotation, multiple_quote


class Manager(ScreenManager):
    pass


class Menu(Screen):
    pass


class Price(Screen):
    def press(self):
        coin = get_currency(self.ids.name_coin.text)
        coin_get = self.ids.name_coin.text.upper()
        coin_name = coin[coin_get]['name']
        coin_data = coin[coin_get]['create_date']
        currency_value = float(coin[coin_get]['bid'])
        self.ids.lbl_coin.text = f'Moeda : {coin_name}'
        self.ids.lbl_date.text = f'Data : {coin_data}'
        self.ids.lbl_value.text = f'Valor : {currency_value: .2f} R$'

    @staticmethod
    def back():
        return Manager()


class Convert(Screen):
    def convert(self):
        coin = get_currency(self.ids.name_coin.text)
        value_to_convert = float(self.ids.value_coin.text)
        coin_get = self.ids.name_coin.text.upper()

        coin_name = coin[coin_get]['name']
        coin_data = coin[coin_get]['create_date']
        coin_value = float(coin[coin_get]['bid'])

        convert_value = value_to_convert * coin_value
        self.ids.convert_value.text = f'Valor em R$ : {convert_value: .2f}'
        self.ids.lbl_coin.text = f'Moeda : {coin_name}'
        self.ids.lbl_date.text = f'Data : {coin_data}'

    @staticmethod
    def back():
        return Manager()


class QuoteOfWeek(Screen):
    def quote_of_week(self):
        coin = get_five_day_cotation(self.ids.name_coin.text)

        coin_name = coin[0]['name']
        coin_data_1 = str(datetime.fromtimestamp(int(coin[0]['timestamp'])))
        currency_value_1 = float(coin[0]['bid'])

        coin_data_2 = str(datetime.fromtimestamp(int(coin[1]['timestamp'])))
        currency_value_2 = float(coin[1]['bid'])

        coin_data_3 = str(datetime.fromtimestamp(int(coin[2]['timestamp'])))
        currency_value_3 = float(coin[2]['bid'])

        coin_data_4 = str(datetime.fromtimestamp(int(coin[3]['timestamp'])))
        currency_value_4 = float(coin[3]['bid'])

        coin_data_5 = str(datetime.fromtimestamp(int(coin[4]['timestamp'])))
        currency_value_5 = float(coin[4]['bid'])

        self.ids.lbl_coin.text = f'Moeda : {coin_name}'
        self.ids.lbl_date_1.text = f'Data : {coin_data_1}'
        self.ids.lbl_value_1.text = f'Valor : {currency_value_1: .2f} R$'

        self.ids.lbl_date_2.text = f'Data : {coin_data_2}'
        self.ids.lbl_value_2.text = f'Valor : {currency_value_2: .2f} R$'

        self.ids.lbl_date_3.text = f'Data : {coin_data_3}'
        self.ids.lbl_value_3.text = f'Valor : {currency_value_3: .2f} R$'

        self.ids.lbl_date_4.text = f'Data : {coin_data_4}'
        self.ids.lbl_value_4.text = f'Valor : {currency_value_4: .2f} R$'

        self.ids.lbl_date_5.text = f'Data : {coin_data_5}'
        self.ids.lbl_value_5.text = f'Valor : {currency_value_5: .2f} R$'

    @staticmethod
    def back():
        return Manager()


class MultipleConvert(Screen):
    def multiple_convert_press(self):
        coin = multiple_quote(self.ids.name_coin_1.text, self.ids.name_coin_2.text, self.ids.name_coin_3.text)
        value_to_convert = float(self.ids.value_coin.text)

        coin_get_1 = self.ids.name_coin_1.text.upper()
        coin_get_2 = self.ids.name_coin_2.text.upper()
        coin_get_3 = self.ids.name_coin_3.text.upper()

        coin_value_1 = float(coin[f'{coin_get_1}BRL']['bid'])
        coin_value_2 = float(coin[f'{coin_get_2}BRL']['bid'])
        coin_value_3 = float(coin[f'{coin_get_3}BRL']['bid'])

        convert_value_1 = value_to_convert * coin_value_1
        convert_value_2 = value_to_convert * coin_value_2
        convert_value_3 = value_to_convert * coin_value_3

        self.ids.convert_value_1.text = f'Valor em R$ : {convert_value_1: .2f}'
        self.ids.convert_value_2.text = f'Valor em R$ : {convert_value_2: .2f}'
        self.ids.convert_value_3.text = f'Valor em R$ : {convert_value_3: .2f}'

    @staticmethod
    def back():
        return Manager()


class main(MDApp):
    @staticmethod
    def build():
        return Manager()


if __name__ == '__main__':
    main().run()
