from typing import Any
import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from Login import LoginScreen
from Register import RegisterScreen, RegisterWindow
from Loading import LoadingScreen
from Select import SelectScreen
from Classes import ClassesScreen
from Home import HomeScreen
from Questions import QuestionsScreen
from kivy.clock import Clock
from database_conf import Database
from Result import ResultScreen

#ebben van a GUI nagyreszt deklaralva


kv = Builder.load_file("windowmanager.kv")

#maga az app
#a metodusait, attributumait az osztalyokban a App.get_running_app()
#segitsegevel lehet elerni
#a windowkra a screenek childrenjeikent lehet hivatkozni de kell indexelni a childreneket
#exp: App.get_running_app().loginScreen.children[0] - ez a LoginWindow
class TeachYourselfApp(App):
    def build(self):
        self.points = 0
        self.db = Database()
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

    #ezek itt a screenvaltoztatgato metodusok
    def switchScreenSelect(self):
        self.screenManager.switch_to(self.selectScreen)

    def switchScreenLogin(self):
        self.screenManager.switch_to(self.loginScreen)

    def switchScreenLogin(self, app):
        self.screenManager.switch_to(self.loginScreen)

    def switchScreenRegister(self, app):
        self.screenManager.switch_to(self.registerScreen)

    def switchScreenHome(self):
        self.screenManager.switch_to(self.homeScreen)

    def switchScreenHome(self, app):
        self.screenManager.switch_to(self.homeScreen)

    def switchScreenClasses(self):
        self.screenManager.switch_to(self.classesScreen)

    def switchScreenResult(self):
        self.screenManager.switch_to(self.resultScreen)

    def exit(self, app):
        self.stop()

    def on_start(self):
        if True:
            Clock.schedule_once(self.switchScreenLogin, 2)

