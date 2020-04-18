#rename it as main.py while using

import requests
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


URL = "http://nithusv.pythonanywhere.com"



class MyGrid(Widget):
    uid = ObjectProperty(None)
    passwd = ObjectProperty(None)
    result = ObjectProperty(None)


    def btn(self):
        a  = self.uid.text
        b = self.passwd.text
        url = f"{URL}/api/auth/"
        try:
            response = requests.post(url,data={'username': a, 'password': b})

            if response.status_code == 200:
                self.result.text = "Success"
            elif response.status_code == 400:
                self.result.text = "Invalid Credentials"
                
        except:
            self.result.text = "No Internet"

        
        #print("username:", self.uid.text , "password:",  self.passwd.text)
        #self.result.text = "Username "+a+"  "+"Password " +b
        self.uid.text = ""
        self.passwd.text = ""
        



class MainApp(App):
    def build(self):
        return MyGrid()
















if __name__ == '__main__':
    app = MainApp()
    app.run()
































    '''label = Label(text='Hello from Kivy',
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5})
                      
                      
                      
                      
                      
                      class LoginScreen(GridLayout):
        
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.rows = 3
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)
        self.label = Label(text='Hello from Kivy',size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5})
        self.add_widget(self.label)
'''
