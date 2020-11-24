import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.image import Image
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen

class LoginWindow(BoxLayout):
    tiUsername = ObjectProperty()
    tiPassword = ObjectProperty()

    def submitUser(self, app):
        # a bejelentkezes ellenorzest az adatbazissal itt kell csinalni
        if len(self.tiUsername.text) != 0 or len(self.tiPassword.text) != 0:
            app.switchScreenSelect()

class LoginScreen(Screen):
    pass



