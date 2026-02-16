import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
import threading
import time
from datetime import datetime
import random

class SaraApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.header = Label(
            text='🤖 S.A.R.A. (Shadow Anywhere Reset Anything)',
            font_size='20sp',
            size_hint=(1, 0.2)
        )
        layout.add_widget(self.header)
        
        self.chat_display = Label(
            text='Welcome Anif! Ask me anything...',
            size_hint=(1, 0.5),
            halign='left',
            valign='top',
            text_size=(400, None)
        )
        layout.add_widget(self.chat_display)
        
        self.user_input = TextInput(
            text='',
            hint_text='Type your message...',
            multiline=False,
            size_hint=(1, 0.1)
        )
        layout.add_widget(self.user_input)
        
        btn_layout = BoxLayout(size_hint=(1, 0.1), spacing=5)
        
        self.send_btn = Button(text='Send', on_press=self.send_message)
        btn_layout.add_widget(self.send_btn)
        
        self.clear_btn = Button(text='Clear', on_press=self.clear_chat)
        btn_layout.add_widget(self.clear_btn)
        
        layout.add_widget(btn_layout)
        
        return layout
    
    def send_message(self, instance):
        msg = self.user_input.text.strip()
        if not msg:
            return
        
        self.chat_display.text += f"\nYou: {msg}"
        self.user_input.text = ''
        
        t = threading.Thread(target=self.generate_response, args=(msg,))
        t.daemon = True
        t.start()
    
    def clear_chat(self, instance):
        self.chat_display.text = 'Chat cleared...'
    
    def generate_response(self, user_msg):
        time.sleep(random.uniform(0.5, 1.5))
        
        user_msg_lower = user_msg.lower()
        
        if 'hello' in user_msg_lower or 'hi' in user_msg_lower:
            reply = f"S.A.R.A.: Hello Anif! 😊 How can I assist you?"
        elif 'time' in user_msg_lower:
            current = datetime.now().strftime('%I:%M %p')
            reply = f"S.A.R.A.: The current time is {current}."
        elif 'who are you' in user_msg_lower:
            reply = "S.A.R.A.: I am S.A.R.A. — Shadow Anywhere Reset Anything. Your adaptive AI collaborator, always listening, always ready. 🛡️"
        elif 'emotion' in user_msg_lower:
            emotions = ['happy', 'sad', 'surprised', 'angry']
            chosen = random.choice(emotions)
            reply = f"S.A.R.A.: I sense you might be feeling {chosen}. Let's talk about it."
        elif 'exit' in user_msg_lower or 'bye' in user_msg_lower:
            reply = "S.A.R.A.: Goodbye Anif! Remember, I'm always here when you need me. 👋"
        else:
            reply = f"S.A.R.A.: I'm still learning, Anif. But I've stored '{user_msg}' in my long‑term memory for future reference. 🧠"
        
        Clock.schedule_once(lambda dt: self.update_chat(reply), 0)
    
    def update_chat(self, reply):
        self.chat_display.text += f"\n{reply}"

if __name__ == '__main__':
    SaraApp().run()
