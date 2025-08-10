from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivymd.uix.snackbar import MDSnackbar
import requests

Builder.load_file("login.kv")
Builder.load_file("register.kv")
Builder.load_file("forgot_password.kv")


API_URL = "https://gerenciador-com-flask.onrender.com"

class LoginScreen(Screen):
    def login(self):
        email = self.ids.email_field.text
        senha = self.ids.password_field.text

        try:
            res = requests.post(f"{API_URL}/login", json={"email": email, "senha": senha})
            data = res.json()
            if data.get("Status") == "OK":
                print("Login OK:", data.get("message"))
                self.manager.current = "tasks"
            else:
                print("Erro:", data.get("message"))
        except Exception as e:
            print("Erro ao conectar API:", e)

class RegisterScreen(Screen):
    def register(self):
        email = self.ids.email_field.text
        senha = self.ids.password_field.text

        try:
            res = requests.post(f"{API_URL}/register", json={"email": email, "senha": senha})
            data = res.json()
            if res.status_code == 201:
                print("Registro OK:", data.get("message"))
                self.manager.current = "login"
            else:
                print("Erro:", data.get("message"))
        except Exception as e:
            print("Erro ao conectar API:", e)


def login(self):
    email = self.ids.email.text
    senha = self.ids.senha.text
    url = "https://gerenciador-com-flask.onrender.com/login"
    response = requests.post(url, json={"email": email, "senha": senha})
    data = response.json()
    print(data)
    # trate a resposta, mostre mensagens, etc

class TaskScreen(Screen):
    pass  # Depois a gente implementa

class ForgotPasswordScreen(Screen):
    pass

class GerenciadorApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(RegisterScreen(name="register"))
        sm.add_widget(ForgotPasswordScreen(name="forgot_password"))
        sm.add_widget(TaskScreen(name="tasks"))
        return sm

    def send_reset_email(self):
        email = self.root.get_screen('forgot_password').ids.email_field.text
        if not email:
            snack = MDSnackbar()
            snack.text = "Por favor, insira um e-mail"
            snack.open()
            return
        
        url = 'https://gerenciador-com-flask.onrender.com/request-password-reset'
        response = requests.post(url, json={'email': email})
        if response.status_code == 200:
            snack = MDSnackbar()
            snack.text = "E-mail de recuperação enviado"
            snack.open()
            self.root.current = 'login'
        else:
            snack = MDSnackbar()
            snack.text = "Erro ao enviar e-mail"
            snack.open()

if __name__ == "__main__":
    GerenciadorApp().run()
