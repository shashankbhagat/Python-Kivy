import kivy
from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.boxlayout import BoxLayout

class TestButton(App):
    def build(self):
        return #Label(text='Hello World')

class Test(BoxLayout):
    pass


if __name__=='__main__':
    TestButton().run()