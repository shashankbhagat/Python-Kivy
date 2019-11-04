from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line

class TouchInput(Widget):
    def on_touch_down(self, touch):
        
        with self.canvas:
            touch.ud['line']=Line(points=(touch.x,touch.y))
            touch.ud['shape']=Line(points=(touch.x,touch.y))
        print('Down:',touch,touch.x,touch.y,type(touch.x),type(touch.ud['line'].points),type(touch),type(touch.ud))
        
        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        print('Move:',touch,touch.ud['line'].points)
        touch.ud['shape'].points+=[touch.x,touch.y]
        #touch.ud['line'].points+=[touch.x,touch.y]
        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        print('Released!',touch)
        return super().on_touch_up(touch)

class SimpleKivy4(App):
    def build(self):
        return TouchInput()

if __name__=='__main__':
    SimpleKivy4().run()