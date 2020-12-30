from typing import Any
import kivy
from kivy.app import App
from kivy.properties import BooleanProperty
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from Result import ResultScreen

#ezek a QUESTIONS osztalyok


answer = ''
class SelectableLabelAnswer(RecycleDataViewBehavior, Label):
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        self.index = index
        return super(SelectableLabelAnswer, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        if super(SelectableLabelAnswer, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        self.selected = is_selected
        if self.selected is True:
            global answer
            answer = self.text
            App.get_running_app().db.counter = App.get_running_app().db.counter + 1
            q = QuestionsScreen(name=str(App.get_running_app().db.counter))
            App.get_running_app().screenManager.add_widget(q)
            if App.get_running_app().db.counter != 0:
                App.get_running_app().screenManager.switch_to(q)

class AnswersList(RecycleView):
    def __init__(self, **kwargs):
        super(AnswersList, self).__init__(**kwargs)
        #ezt az attributumot kell valtoztatni a valaszokhoz
        X = ['Igen', 'Nem']
        self.data = [{'text': x} for x in X]

class QuestionsWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(QuestionsWindow, self).__init__(**kwargs)


class QuestionsScreen(Screen):
    def __init__(self, **kwargs):
        self.question = ''
        rows = App.get_running_app().db.Cursor.execute('Select question, question_correct_answer from questions where class_name=?', (App.get_running_app().db.classname,)).fetchall()
        try:
            self.question = (rows[App.get_running_app().db.counter])[0]
            self.right_answer = (rows[App.get_running_app().db.counter])[1]
            super(QuestionsScreen, self).__init__(**kwargs)
            if answer == self.right_answer:
                App.get_running_app().points += 1
        except:
            if App.get_running_app().db.counter != 0:
                App.get_running_app().db.counter = 0
                self.resultScreen = ResultScreen()
                App.get_running_app().screenManager.add_widget(self.resultScreen)
                App.get_running_app().screenManager.switch_to(self.resultScreen)
                App.get_running_app().points = 0



