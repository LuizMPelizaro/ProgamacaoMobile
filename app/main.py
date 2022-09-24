from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

from function.gets import get_currency


class Gerenciador(ScreenManager):
    pass


class Menu(Screen):
    pass


class Cotacao(Screen):
    def press(self):
        coin = get_currency(self.ids.name_coin.text)
        coin_get = self.ids.name_coin.text.upper()
        coin_name = coin[coin_get]['name']
        coin_data = coin[coin_get]['create_date']
        currency_value = coin[coin_get]['bid']
        self.ids.lbl_moeda.text = f'Moeda : {coin_name}'
        self.ids.lbl_data.text = f'Data : {coin_data}'
        self.ids.lbl_valor.text = f'Valor : {currency_value} R$'

    @staticmethod
    def back():
        return Gerenciador()


class Screen_2(Screen):
    pass

    @staticmethod
    def back():
        return Gerenciador()


class main(App):
    @staticmethod
    def build():
        return Gerenciador()


if __name__ == '__main__':
    main().run()
