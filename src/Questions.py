from typing import Any
import kivy
from kivy.app import App
from kivy.uix.recycleview import RecycleView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

#ezek a QUESTIONS osztalyok
#ide a ChatApp-bol lehet segitseget kerni
class AnswersList(RecycleView):
    def __init__(self, **kwargs):
        super(AnswersList, self).__init__(**kwargs)
        #ezt az attributumot kell valtoztatni a valaszokhoz
        self.data = [{'text': str(x)} for x in range(4)]

class QuestionsWindow(BoxLayout):
    def __init__(self,**kwargs):
        super(QuestionsWindow, self).__init__(**kwargs)
        #ezt az attributomot kell valtoztatgatni folyamatosan amikor a kepernyo ujratoltodik
        #az ujratoltes meg nincs meg
        self.question = 'fasza'

class QuestionsScreen(Screen):
    pass