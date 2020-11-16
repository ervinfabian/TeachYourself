from typing import Any
import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.recycleview import RecycleView
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior

class HomeList(RecycleView):
    def __init__(self, **kwargs):
        super(HomeList, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in range(15)]

class HomeWindow(BoxLayout):
    pass

class HomeScreen(Screen):
    pass