import kivy
from kivy.app import App
from kivy.uix.button import Button

class SaraApp(App):
    def build(self):
        # একটি সুন্দর বাটন তৈরি করছি
        return Button(
            text='Hello Anif! S.A.R.A. is Running...',
            font_size='20sp',
            background_color=(0, 0.5, 1, 1)
        )

if __name__ == '__main__':
    SaraApp().run()
