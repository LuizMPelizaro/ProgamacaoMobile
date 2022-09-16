from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


class Gerenciador(ScreenManager):
    pass


class Menu(Screen):
    pass


class Screen_1(Screen):
    def on_checkbox_Active(self, checkboxInstance, isActive):
        if isActive:
            self.ids.lbl.text = "BORA BILL !!"
        else:
            self.ids.lbl.text = "BILL"


class Screen_2(Screen):
    def addSpiner(self):
        txt = self.ids.spn.values
        txt.append(self.ids.texto.text)
        self.ids.spn.values = txt
        self.ids.texto.text = ''

    def spinner_Clicado(self, value):
        self.ids.escolha.text = value


class main(App):
    def build(self):
        return Gerenciador()


if __name__ == '__main__':
    main().run()
