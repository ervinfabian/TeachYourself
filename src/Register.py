from typing import Any
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.image import Image
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen



class RegisterWindow(BoxLayout):
    print("RegisterWindow")
    tiUsername = ObjectProperty()
    tiEmail = ObjectProperty()
    tiPassword = ObjectProperty()
    tiConfirmPassword = ObjectProperty()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class RegisterScreen(Screen):
    def __init__(self):
        super(RegisterScreen, self).__init__()
    
    def switchToProfile(self):
        if self.manager.current == "RegisterScreen":
            self.manager.transition = SlideTransition(direction="left")
            self.manager.current = "ProfileScreen"

    #def switchToLogin(self):










