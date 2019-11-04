from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.button import Button

class LoginScreen(GridLayout):
    def __init__(self):
        #super(LoginScreen,self).__init__(**kwargs)
        super().__init__()
        self.cols=2
        self.rows=5
        self.add_widget(Label(text='UserName:'))        
        self.username=TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text='Password:'))
        self.password=TextInput(multiline=False,password=True)
        self.add_widget(self.password)

        self.add_widget(Label(text='Two Factor Auth:'))
        self.tfa=TextInput(multiline=False)
        self.add_widget(self.tfa)

        self.add_widget(Button(text='test',color=(0,1,0,0.5),font_size=40))


class SimpleKivy1(App):
    def build(this):
        #return Label(text='Hello World!!!')
        return LoginScreen()

if __name__=='__main__':
    SimpleKivy1().run()
