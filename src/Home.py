from typing import Any
import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.recycleview import RecycleView
import Classes

#ezek a HOME osztalyok
class HomeList(RecycleView):
    def __init__(self, **kwargs):
        super(HomeList, self).__init__(**kwargs)
        self.data = [{'text': x} for x in Classes.classes]

class HomeWindow(BoxLayout):
    pass

class HomeScreen(Screen):
    pass