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


#ezek a REGISTER osztalyok
class RegisterWindow(BoxLayout):
    tiUsername = ObjectProperty()
    tiEmail = ObjectProperty()
    tiPassword = ObjectProperty()
    tiConfirmPassword = ObjectProperty()

    def submitUser(self, app):
        #a regisztralas ellenorzest az adatbazissal itt kell csinalni
        if len(self.tiUsername.text) != 0 and len(self.tiPassword.text) != 0 and \
        len(self.tiConfirmPassword.text) != 0 and len(self.tiEmail.text) != 0 and self.tiPassword.text == self.tiConfirmPassword.text:
            app.switchScreenSelect()
        print(False)


class RegisterScreen(Screen):
    def __init__(self):
        super(RegisterScreen, self).__init__()


    # def textInputCheck(self):












