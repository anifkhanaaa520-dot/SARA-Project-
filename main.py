import kivy
from kivy.app import App
from kivy.uix.button import Button

class SaraApp(App):
    def build(self):
        return Button(text='Hello Anif! S.A.R.A. is Running...')

if __name__ == '__main__':
    SaraApp().run()
