from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder



class Widgets(Widget):
    pass

class ScatterSample(FloatLayout):
    pass

presentation=Builder.load_file('SimpleKivy.kv')

class SimpleKivy(App):
    def build(self):
        return presentation

        #f=FloatLayout()
        #s=Scatter()
        #l=Label(text='Hello World....',font_size=45)
        #f.add_widget(s)
        #s.add_widget(l)
        #return f

class SimpleKivy3(App):
    def build(this):
        return Widgets()
        

if __name__=='__main__':
    SimpleKivy().run()
    #SimpleKivy3().run()