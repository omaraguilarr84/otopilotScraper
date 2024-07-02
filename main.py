from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class LoginScreen(Screen):
    pass

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        return sm

    def login(self, username, password):
        if username == 'user' and password == 'pass':
            self.show_popup('Login Success', 'Welcome!')
        else:
            self.show_popup('Login Failed', 'Invalid credentials')

    def show_popup(self, title, message):
        layout = BoxLayout(orientation='vertical')
        popup_label = Label(text=message)
        close_button = Button(text='Close')
        layout.add_widget(popup_label)
        layout.add_widget(close_button)

        popup = Popup(title=title, content=layout, size_hint=(None, None), size=(300, 200))
        popup.open()
        close_button.bind(on_press=popup.dismiss)

if __name__ == '__main__':
    MyApp().run()
