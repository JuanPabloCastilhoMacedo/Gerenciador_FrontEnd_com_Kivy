from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import requests

Builder.load_file("login.kv")
Builder.load_file("register.kv")

API_URL = "https://gerenciador-com-flask.onrender.com"

class LoginScreen(Screen):
    def login(self):
        email = self.ids.email.text
        senha = self.ids.senha.text

        try:
            res = requests.post(f"{API_URL}/login", json={"email": email, "senha": senha})
            data = res.json()
            if data.get("Status") == "OK":
                print("Login OK:", data.get("mensagem"))
                self.manager.current = "tasks"
            else:
                print("Erro:", data.get("mensagem"))
        except Exception as e:
            print("Erro ao conectar API:", e)

class RegisterScreen(Screen):
    def register(self):
        email = self.ids.email.text
        senha = self.ids.senha.text

        try:
            res = requests.post(f"{API_URL}/register", json={"email": email, "senha": senha})
            data = res.json()
            if data.get("Status") == "OK":
                print("Registro OK:", data.get("mensagem"))
                self.manager.current = "login"
            else:
                print("Erro:", data.get("mensagem"))
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

class GerenciadorApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(RegisterScreen(name="register"))
        sm.add_widget(TaskScreen(name="tasks"))
        return sm

if __name__ == "__main__":
    GerenciadorApp().run()
