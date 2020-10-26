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

class MyLabel(Label):
    def __init__(self, **kwargs):
        Label.__init__(self, **kwargs)
        self.register_event_type('on_double_press')
        if kwargs.get("on_double_press") is not None:
            self.bind(on_double_press=kwargs.get("on_double_press"))

    def on_touch_down(self, touch):
        if touch.is_double_tap:
            self.dispatch('on_double_press', touch)
            return True
        return Label.on_touch_down(self, touch)

    def on_double_press(self, *args):
        pass

class LoginWindow(BoxLayout):
    tiUsername = ObjectProperty()
    tiPassword = ObjectProperty()


class LoginScreen(Screen):
    pass

class LoginWindowApp(App):
    def build(self):
        print("LoginWindowApp")
        return LoginWindow()

