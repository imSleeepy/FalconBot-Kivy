from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.card import MDCard
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
import requests  # Import the requests module
from kivy.core.window import Window
Window.keyboard_anim_args = {'d': .2, 't': 'in_out_expo'}
Window.softinput_mode = "below_target"

class User(MDCard):
    text = StringProperty()
    font_size = NumericProperty()

class Response(MDCard):
    text = StringProperty()
    font_size = NumericProperty()

class ChatScreen(Screen):
    chat_area = ObjectProperty()
    message = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.welcome_message()

    def welcome_message(self):
        self.ids.chat_area.add_widget(
            Response(text="Hey Klasmeyt, I'm here to help you about the student manual!", font_size=17)
        )

    def show_user_input(self):
        user_input = self.ids.message.text
        if user_input:
            # Display user message instantly on button press
            self.ids.chat_area.add_widget(
                User(text=user_input, font_size=17)
            )
            # Clear the input field
            self.ids.message.text = ""  

    def process_bot_response(self):
        user_input = self.ids.chat_area.children[0].text

        # Call the Azure server to get the response based on the user input
        bot_response = self.get_bot_response(user_input)

        # Display bot response on button release
        self.ids.chat_area.add_widget(
            Response(text=bot_response, font_size=17)
        )

    def get_bot_response(self, user_input):
        """Send the user input to the chatbot API and get the response."""
        url = "http://52.184.84.224:5000/get_response"  # The endpoint of your chatbot API on Azure
        try:
            response = requests.post(url, json={"query": user_input})
            if response.status_code == 200:
                return response.json().get("response", "Sorry, I couldn't get an answer.")
            else:
                return "Error: Unable to connect to the server."
        except requests.exceptions.RequestException as e:
            return f"Error: {str(e)}"

class ChatApp(MDApp):   
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ChatScreen(name='chat'))
        return sm

if __name__ == '__main__':
    ChatApp().run()
