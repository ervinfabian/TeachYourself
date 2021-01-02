from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen


#ezek a REGISTER osztalyok
class RegisterWindow(BoxLayout):
    tiUsername = ObjectProperty()
    tiEmail = ObjectProperty()
    tiPassword = ObjectProperty()
    tiConfirmPassword = ObjectProperty()

    def submitUser(self, app):
        counter = 0
        rows = App.get_running_app().db.Cursor.execute('Select username from members where username = ?', (self.tiUsername.text,)).fetchall()
        for row in rows:
            counter = counter + 1
        if len(self.tiUsername.text) != 0 and len(self.tiPassword.text) != 0 and \
        len(self.tiConfirmPassword.text) != 0 and len(self.tiEmail.text) != 0 and self.tiPassword.text == self.tiConfirmPassword.text and counter != 1:
            App.get_running_app().db.Cursor.execute('INSERT INTO members (username, email, password) VALUES (?,?,?)', (self.tiUsername.text, self.tiEmail.text, self.tiPassword.text))
            App.get_running_app().db.connection.commit()
            app.switchScreenSelect()
        print(False)


class RegisterScreen(Screen):
    def __init__(self):
        super(RegisterScreen, self).__init__()


    # def textInputCheck(self):












