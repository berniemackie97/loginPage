from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from datetime import datetime

Builder.load_file('design.kv')


class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"

    def login(self, uname, pword):
        with open("user.json") as file:
            users = json.load(file)
        if uname in users and users[uname]['password'] == pword:
            self.manager.current = 'login_screen_success'
        else:
            self.ids.login_wrong.text = "Wrong Username or Password"


class RootWidget(ScreenManager):
    pass


class SignUpScreen(Screen):
    def add_user(self, user, pasw):
        with open("user.json") as file:
            users = json.load(file)

        users[user] = {'username': user, 'password': pasw,
                       'created': datetime.now().strftime("%Y-%m-%d-%H-%M-%s")}
        with open("user.json", 'w')as file:
            json.dump(users, file)
        self.manager.current = "sign_up_screen_success"


class SignUpScreenSuccess(Screen):
    def go_to_login(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"


class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()
