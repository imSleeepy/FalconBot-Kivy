from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.card import MDCard
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.uix.button import Button
import random
from kivy.utils import get_color_from_hex
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
import requests 

from kivy.core.window import Window
Window.keyboard_anim_args = {'d': .2, 't': 'in_out_expo'}
Window.softinput_mode = "below_target"

class User(MDCard):
    text = StringProperty()
    font_size = NumericProperty()

class Response(MDCard):
    text = StringProperty()
    font_size = NumericProperty()

class Suggestion(Button):
    text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.halign = 'center'
        self.valign = 'middle'
        self.font_size = '13sp'
        self.height = 50
        self.background_normal = '' 
        self.background_color = (122/255, 153/255, 215/255, 1) 

def list_suggestions():
    return [
        "How do I enroll?",
        "What actions are considered major offenses?",
        "What are the Core Values of Adamson University?",
        "How can students request an exemption from the uniform policy?",
        "When are students allowed to wear civilian clothing?",
        "What version of the Manual is used here?",
        "What proof do I need if I missed an exam due to illness?",
        "What is the grading system?",
        "What is the Mission of the Adamson University?",
        "What is the pledge of conformity?",
        "Who is the president of Adamson Univeristy",
        "Who is the founder of Adamson Univeristy"
    ]

def rule_based_process(user_input):
    # Existing response logic for general queries
    if "help" in user_input.lower():
        return get_help_response()
    elif "wear" in user_input.lower():
        if "civilian" in user_input.lower():
            return get_clothing_policy_response()
    elif "who" in user_input.lower():
        if "founder" in user_input.lower():
            return get_founder_info_response()
        elif "president" in user_input.lower():
            return get_president_info_response()
    elif "grading" in user_input.lower():
        return get_grading_response()
    elif "how" in user_input.lower():
        if "enroll" in user_input.lower():
            return how_to_enroll()
    elif "enroll" in user_input.lower():
        if "freshman" in user_input.lower():
            return get_freshman_enroll_response()
        elif "old" in user_input.lower():
            return get_old_enroll_response()
        elif "transfer" in user_input.lower():
            return get_transfer_enroll_response()
    
def get_help_response():
    return "Sure Klasmeyt! What do you need help with?"

def get_clothing_policy_response():
    return "Students are allowed to wear decent civilian clothes during Washday (Wednesday) and Activity Days."

def get_founder_info_response():
    return (
        """Adamson University was founded as the Adamson School of Industrial Chemistry (ASIC) 
        by George Lucas Adamson and his cousins, Alexander Adamson and George Athos, and began 
        as a 42-student night class at the Paterno Building in Santa Cruz, Manila."""
    )

def get_president_info_response():
    return (
        """Fr. Daniel Franklin E. Pilario, CM, Ph.D., S.Th.D., is the 7th President and 3rd alumnus 
        President of Adamson University."""
    )

def get_grading_response():
    return (
        """The university uses a numerical grading system with corresponding Grade Point Equivalents 
        and letter grades. The grading scale is as follows:

        97-100 = 1.00  (A)  = Excellent
        93-96  = 1.25  (A-) = Superior
        89-92  = 1.50  (B+) = Superior
        85-88  = 1.75  (B)  = Average
        82-84  = 2.00  (B-) = Average
        79-81  = 2.25  (C+) = Average
        76-78  = 2.50  (C)  = Passed
        73-75  = 2.75  (C-) = Passed
        70-72  = 3.00  (D)  = Passed
        <70    = 5.00  (F)  = Failed

        Dropped courses have a grade of 6.00 (DR), and No Grade (NG) has a grade point equivalent of 0.00."""
    )

def get_freshman_enroll_response():
    return (
        """FRESHMEN ENROLLMENT PROCEDURE

            1. Student shall apply and pass the University Entrance Examination (UEE) and submit the 
            original copy of the following requirements upon enrollment:

            1.1. Copy of the UEE result
            1.2. Form 138 (Senior High School Report Card)
            1.3. 2 pcs. 2x2 ID picture
            1.4. Certificate of Good Moral Character signed by the Principal or Guidance Counselor
            1.5. Authenticated Birth Certificate from the Philippine Statistics Authority (PSA)
            1.6. Letter of Application for students who did not enroll for a period of one year or 
                    more after Senior High School Graduation.

            2. Present original credentials and UEE result to Admissions and Student Recruitment Office.
            3. Proceed to respective college/department chair for an interview.
            4. Submit the original compulsory requirements with the approval of the college/department to 
            the Admissions Office. In case of incomplete or lacking requirements, the applicant must 
            accomplish a Letter of Undertaking and submit it to the Admissions and Student Recruitment 
            Section.
            5. If passed in the interview, proceed to 6. If not, proceed to the Admissions Office to 
            secure another endorsement for a new program as advised by the department chair/dean.
            6. Submit UEE result and original credentials to the Admissions Office with college/department 
            approval.
            7. Pay the assessed fees at the Cashier.
            8. Proceed to the Admissions Office ID room for ID processing.
            9. Proceed to the Computer Laboratory for encoding of other Student Information Data into the 
            Student Information System.
            10. Proceed to the University store for the purchase of school uniform."""
    )       

def get_old_enroll_response():
    return (
            """OLD STUDENTS ENROLLMENT PROCEDURE

            1. Regular Student
            1.1. Print or view the pre-advised subjects in Learning Management System (LMS) or e-Learning.
            1.2. Pay at the Cash Management Office or any accredited banks or any Bayad Center.
            1.3. Print Certificate of Enrollment.

            2. Irregular Student
            2.1. Print or view the pre-advised subjects in Learning Management System (LMS) or e-Learning.
            2.2. Pay at the Cash Management Office, accredited banks, or any Bayad Center.
            2.3. Choose subject/s online.
            2.4. Print Certificate of Enrollment.

            3. Re-admission/Returning Student
            3.1. Apply for True Copy of Grades (TCG).
            3.2. Get the re-admission form from the respective department.
            3.3. Submit the processed re-admission form at the program window.
            3.4. Once the account is generated, follow the enrollment procedure for old students."""
        )

def get_transfer_enroll_response():
    return (
            """TRANSFEREES ENROLLMENT PROCEDURE

            A student seeking admission must pass the University Entrance Examination (UEE) and submit 
            the original copy of the following requirements upon enrollment:
            1. Honorable Dismissal/Transfer Credentials
            2. Certificate of Good Moral Character from the institution last attended
            3. Certificate of true copy of Grades
            4. Letter of Application addressed to the Registrar
            5. 4 pcs. 2x2 ID pictures
            6. Authenticated Birth Certificate from the Philippine Statistics Authority (PSA)
            7. Original copy of the UEE result

            Present all original credentials to the Admissions Office for verification.
            Proceed to the respective college/dean for an interview.
            If passed in the interview, submit the UEE results with the Subject Accreditation Form approval 
            from the college/department to the Admissions Office along with the original credentials.
            If requirements are complete, get your generated/assigned student number.
            Pay the corresponding fees at the Cashier.
            Follow the enrollment procedure for subject enlistment as provided by the Registrar's Office.
            Go to the Admissions Office ID Section for ID processing.
            Purchase school uniform at the University Store.
            Attend the scheduled orientation with parent/guardian."""
        )

def how_to_enroll():
    return {
        "text": "Are you an old student, a freshman, or a transferee?",
        "followUp": True,
        "options": [
            {"label": "Old Student", "value": get_old_enroll_response()},
            {"label": "Freshman", "value": get_freshman_enroll_response()},
            {"label": "Transferee", "value": get_transfer_enroll_response()},
        ],
    }

class ChatScreen(Screen):
    chat_area = ObjectProperty()
    message = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.welcome_message()

    def welcome_message(self):
        self.ids.chat_area.clear_widgets()  # Clear any existing messages
        self.ids.chat_area.add_widget(
            Response(text= "Hey Klasmeyt, I'm here to help you about the student manual!", font_size=17)
        )

        # Add suggestion messages
        self.add_suggestions()

    def add_suggestions(self):
        suggestions = list_suggestions() if callable(list_suggestions) else list_suggestions
        random_suggestions = random.sample(list(suggestions), 3)
        for suggestion in random_suggestions:
            suggestion_button = Suggestion(
                text=suggestion,
                size_hint_y=None,
                height=40,
                md_bg_color=get_color_from_hex("#7099d7"),
                theme_text_color="Custom",
                text_color=(1, 1, 1, 1)
            )
            suggestion_button.bind(on_release=lambda btn, text=suggestion: self.handle_suggestion_click(text))
            self.ids.chat_area.add_widget(suggestion_button) 

    def handle_enrollment_click(self, enrollment_type):
        self.ids.chat_area.add_widget(User(text=enrollment_type, font_size=17))
        # Call rule_based_process with the selected enrollment type
        self.rule_based_response(f"enroll {enrollment_type}")

    def handle_suggestion_click(self, suggestion):
        self.ids.chat_area.parent.scroll_to(self.ids.chat_area.children[0])
        
        # Pass the suggestion to show_user_input with a slight delay
        Clock.schedule_once(lambda dt: self.show_user_input(suggestion), 0.3)

    def reset_chat(self):
        self.ids.chat_area.clear_widgets()
        self.welcome_message()
        self.ids.chat_area.parent.scroll_y = 1

    def show_user_input(self, suggestion=None):
        user_input = self.ids.message.text if not suggestion else suggestion
        
        if user_input:
            # Display the user message
            self.ids.chat_area.add_widget(User(text=user_input, font_size=17))
            self.ids.message.text = ""  # Clear the input field
            
            
            Clock.schedule_once(lambda dt: self.rule_based_response(user_input), 0.3)

    def rule_based_response(self, user_input):
        response = rule_based_process(user_input)
        if response:
            if isinstance(response, dict):
                if response.get("followUp"):
                    self.ids.chat_area.add_widget(
                        Response(text=response["text"], font_size=17)
                    )
                    for option in response["options"]:
                        option_button = Suggestion(
                            text=option["label"],
                            size_hint_y=None,
                            height=40,
                            md_bg_color=get_color_from_hex("#37426F"),
                            theme_text_color="Custom",
                            text_color=(1, 1, 1, 1)
                        )
                        option_button.bind(on_release=lambda btn, text=option["label"]: self.handle_enrollment_click(text))
                        self.ids.chat_area.add_widget(option_button)
                else:
                    # Display plain text response if no follow-up is required
                    self.ids.chat_area.add_widget(
                        Response(text=response["text"], font_size=17)
                    )
            # If response is a string, display it directly
            elif isinstance(response, str):
                self.ids.chat_area.add_widget(
                    Response(text=response, font_size=17)
                )
        else:
            # Call main bot response if no rule-based response is found
            self.process_bot_response(user_input)
            
    def process_bot_response(self, user_input):
        # Call chatbot.py to get the response based on the user input
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
