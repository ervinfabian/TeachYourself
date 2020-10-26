from typing import Any
import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from Profile import ProfileScreen
from Login import LoginScreen
from Register import RegisterScreen, RegisterWindow

kv = Builder.load_file("windowmanager.kv")


class TeachYourselfApp(App):
    def build(self):
        self.screenManager = ScreenManager()
        self.registerScreen = RegisterScreen()
        self.profileScreen = ProfileScreen()
        self.loginScreen = LoginScreen()
        self.screenManager.add_widget(self.registerScreen)
        self.screenManager.add_widget(self.profileScreen)
        self.screenManager.add_widget(self.loginScreen)
        print("TeachYourselfApp")
        return self.screenManager

    def switchScreenProfile(self):
        self.screenManager.switch_to(self.loginScreen)

    def switchScreenLogin(self):
        self.screenManager.switch_to(self.profileScreen)

