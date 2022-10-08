from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

from function.gets import get_currency


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
        coin_value = float(coin[coin_get]['bid'])
        convert_value = value_to_convert * coin_value
        self.ids.convert_value.text = f'Valor em R$ : {convert_value: .2f}'

    @staticmethod
    def back():
        return Manager()


class main(App):
    @staticmethod
    def build():
        return Manager()


if __name__ == '__main__':
    main().run()
