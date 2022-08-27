from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button as bt
from kivy.uix.label import Label as lbl


class Tela(App):
    def build(self):
        caixa = BoxLayout(orientation='vertical')
        botao = bt(text="hello", on_press=self.add)
        self.lbl = lbl(text='1')
        caixa.add_widget(self.lbl)
        caixa.add_widget(botao)
        return caixa

    def add(self, lbl):
        if int(self.lbl.text) == 10:
            self.lbl.text = str(int(self.lbl.text) - 10)
        self.lbl.text = str(int(self.lbl.text) + 1)


if __name__ == "__main__":
    Tela().run()
