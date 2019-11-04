from kivy.app import App
import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.videoplayer import VideoPlayer
from kivy.core.audio import SoundLoader

class mainVideo(App):
    def build(self):
        return super().build()

class VideoPlayerApp(BoxLayout):
    def loadAudio(self):
        sound=SoundLoader.load('batman.mp3')
        sound.play()
        return

    pass

if __name__=='__main__':
    mainVideo().run()
