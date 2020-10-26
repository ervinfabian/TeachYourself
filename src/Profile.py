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


class ProfileWindow(BoxLayout):
    print("ProfileWindow")
    pass


class ProfileScreen(Screen):
    pass

class ProfileWindowApp(App):
    def build(self):
        print("ProfileWindowApp")
        return ProfileWindow()
