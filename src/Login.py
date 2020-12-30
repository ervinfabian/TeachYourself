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

#ezek a LOGIN osztalyok
class LoginWindow(BoxLayout):
    tiUsername = ObjectProperty()
    tiPassword = ObjectProperty()

    def submitUser(self, app):
        # a bejelentkezes ellenorzest az adatbazissal itt kell csinalni
        rows = App.get_running_app().db.Cursor.execute('Select username from members where username = ? and password = ?',
                                                       (self.tiUsername.text, self.tiPassword.text)).fetchall()
        counter = 0
        for row in rows:
            counter += 1
        print(counter)
        if (len(self.tiUsername.text) != 0 or len(self.tiPassword.text) != 0) and counter == 1:
            app.switchScreenHome(App.get_running_app())

class LoginScreen(Screen):
    pass



