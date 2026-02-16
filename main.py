from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class SaraApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        self.lbl = Label(text="S.A.R.A. is initializing...", font_size='24sp')
        btn = Button(text="Activate S.A.R.A.", size_hint=(1, 0.2), background_color=(0, 0.6, 0.9, 1))
        btn.bind(on_press=self.on_activate)
        
        layout.add_widget(self.lbl)
        layout.add_widget(btn)
        return layout

    def on_activate(self, instance):
        self.lbl.text = "Shadow Anywhere Reset Anything\nMode: Super User Activated"

if __name__ == '__main__':
    SaraApp().run()
