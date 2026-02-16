import kivy
from kivy.app import App
from kivy.uix.button import Button

# S.A.R.A. Project Version 1.1
class SaraApp(App):
    def build(self):
        return Button(text='Hello S.A.R.A. is Online!')

if __name__ == '__main__':
    SaraApp().run()
