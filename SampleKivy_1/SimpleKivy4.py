from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
class SimpleKivy4(App):
    
    def build(self):
        return setWidgets()

class setWidgets(FloatLayout):
    def __init__(self):
        self.add_widget(Button(text='Kivy'))
        #self.add_widget(Button(text='Tutorial',pos_hint={'right':0.5,'top':1},color=(1,1,0,1),size_hint=(0.3,0.2)))
        
    
if __name__=='__main__':
    SimpleKivy4().run()
