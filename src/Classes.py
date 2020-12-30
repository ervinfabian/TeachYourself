from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.recycleview import RecycleView
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior

from Questions import QuestionsScreen


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''


class SelectableLabel(RecycleDataViewBehavior, Label):
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        self.index = index
        return super(SelectableLabel, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        if super(SelectableLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        self.selected = is_selected
        if self.selected:
            App.get_running_app().db.classname = self.text
            questionsScreen = QuestionsScreen(name=str(App.get_running_app().db.counter))
            App.get_running_app().screenManager.add_widget(questionsScreen)
            App.get_running_app().screenManager.switch_to(questionsScreen)


#ezek a CLASSES osztalyok
class ClassesList(RecycleView):
    def __init__(self, **kwargs):
        super(ClassesList, self).__init__(**kwargs)
        self.data = [{'text': x} for x in App.get_running_app().db.all_classes]

class ClassesWindow(BoxLayout):
    pass

class ClassesScreen(Screen):
    pass


