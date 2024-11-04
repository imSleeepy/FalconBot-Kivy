from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.card import MDCard
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from chatbot import query_pinecone, generate_answer_t5, format_query_t5

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
            Response(text= "Hey Klasmeyt, I'm here to help you about the student manual!", font_size=17)
        )

    def send_message(self):
        user_input = self.ids.message.text
        if user_input:
            # Display user message
            self.ids.chat_area.add_widget(
                User(text= user_input, font_size=17)
            )
            self.ids.message.text = ""  

            # Fetch bot response
            result = query_pinecone(user_input)
            formatted_query = format_query_t5(user_input, result["matches"])
            bot_response = generate_answer_t5(formatted_query, result["matches"])

            # Display bot response
            self.ids.chat_area.add_widget(
                Response(text= bot_response, font_size=17)
            )

class ChatApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ChatScreen(name='chat'))
        return sm

if __name__ == '__main__':
    ChatApp().run()
