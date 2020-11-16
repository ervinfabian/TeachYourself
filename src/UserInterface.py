from typing import Any
import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from Select import SelectScreen
from Login import LoginScreen
from Register import RegisterScreen, RegisterWindow
from Loading import LoadingScreen
from Select import SelectScreen
from Classes import ClassesScreen
from Home import HomeScreen
from kivy.clock import Clock

kv = Builder.load_file("windowmanager.kv")


class TeachYourselfApp(App):
    def build(self):
        self.screenManager = ScreenManager()
        self.registerScreen = RegisterScreen()
        self.loginScreen = LoginScreen()
        self.loadingScreen = LoadingScreen()
        self.selectScreen = SelectScreen()
        self.classesScreen = ClassesScreen()
        self.homeScreen = HomeScreen()

        self.screenManager.add_widget(self.loadingScreen)
        self.screenManager.add_widget(self.registerScreen)
        self.screenManager.add_widget(self.selectScreen)
        self.screenManager.add_widget(self.loginScreen)
        self.screenManager.add_widget(self.classesScreen)
        self.screenManager.add_widget(self.homeScreen)

        return self.screenManager


    def switchScreenSelect(self):
        self.screenManager.switch_to(self.selectScreen)

    def switchScreenLogin(self):
        self.screenManager.switch_to(self.loginScreen)

    def switchScreenRegister(self, app):
        self.screenManager.switch_to(self.registerScreen)

    def switchScreenHome(self):
        self.screenManager.switch_to(self.homeScreen)
        # if self.homeScreen.textInputCheck():
        #     self.screenManager.switch_to(self.homeScreen)
    def switchScreenLogin(self,app):
        self.screenManager.switch_to(self.loginScreen)

    def on_start(self):
        if True:
            Clock.schedule_once(self.switchScreenLogin, 2)


