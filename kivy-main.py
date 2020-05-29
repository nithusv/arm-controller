import requests
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup


URL = "http://nithusv.pythonanywhere.com"

token = ""

class WindowManager(ScreenManager):
    pass



class MyGrid(Screen):
    

    uid = ObjectProperty(None)
    passwd = ObjectProperty(None)
    result = ObjectProperty(None)

    
    
    

    def btn(self):
        global token
        a  = self.uid.text
        b = self.passwd.text
        
        url = f"{URL}/api/auth/"
        try:
            response = requests.post(url,data={'username': a, 'password': b})
            token = response.json()
            if response.status_code == 200:
                self.result.text = "Login Successful"
            elif response.status_code == 400:
                self.result.text = "Invalid Credentials"
                
        except:
            self.result.text = "No Internet"

        
        #print("username:", self.uid.text , "password:",  self.passwd.text)
        #self.result.text = "Username "+a+"  "+"Password " +b
        self.uid.text = ""
        self.passwd.text = ""
        
        


class Dashboard(Screen):
    pass


class View(Screen):
    global token
    view_modename = ObjectProperty(None)
    view_servo1 = ObjectProperty(None)
    view_servo2 = ObjectProperty(None)
    view_servo3 = ObjectProperty(None)
    view_servo4 = ObjectProperty(None)
    view_led = ObjectProperty(None)
    view_data_number = ObjectProperty(None)
    view_result  = ObjectProperty(None)


    def clearviewbtn(self):
        self.view_modename.text = ""
        self.view_servo1.text = ""
        self.view_servo2.text = ""
        self.view_servo3.text = ""
        self.view_servo4.text = ""
        self.view_led.text = ""
        self.view_result.text = ""

    def viewbtn(self):
        try:
            if self.view_data_number.text == "" :
                raise NameError

            else:
                data = int(self.view_data_number.text)
                url = f"{URL}/api/mode_list/{data}"
                header = {'Authorization': f'Token {token}'}
                view_response = requests.get(url,headers = header)
                if view_response.status_code == 404:
                    self.view_result.text = f"Mode {self.view_data_number.text} not available"
                else:
                    view_data = view_response.json()
                    self.view_modename.text = str(view_data['mode_id'])
                    self.view_servo1.text = str(view_data['servo_1'])
                    self.view_servo2.text = str(view_data['servo_2'])
                    self.view_servo3.text = str(view_data['servo_3'])
                    self.view_servo4.text = str(view_data['servo_4'])
                    self.view_led.text = str(view_data['led'])
                    self.view_result.text = "Success"

        except NameError:
            self.view_result.text = "Please enter a number"


        except:
            print(view_response.status_code)
            self.view_result.text = "No Internet"













class NewMode(Screen):
    global token
    create_modename = ObjectProperty(None)
    create_servo1 = ObjectProperty(None)
    create_servo2 = ObjectProperty(None)
    create_servo3 = ObjectProperty(None)
    create_servo4 = ObjectProperty(None)
    create_led = ObjectProperty(None)
    create_result  = ObjectProperty(None)

    def createbtn(self):
        try:
            if self.create_modename.text == "":
                self.create_result.text = "Mode name required"
            elif self.create_servo1.text == "":
                self.create_result.text = "Servo 1 value required"
            elif self.create_servo2.text == "":
                self.create_result.text = "Servo 2 value required"
            elif self.create_servo3.text == "":
                self.create_result.text = "Servo 3 value required"
            elif self.create_servo4.text == "":
                self.create_result.text = "Servo 4 value required"
            elif self.create_led.text == "":
                self.create_result.text = "led state required"
            else:
                url = f"{URL}/api/mode_list/"
                data = {
                "mode_id": self.create_modename.text,
                "led": self.create_led.text,
                "servo_1": self.create_servo1.text,
                "servo_2": self.create_servo2.text,
                "servo_3": self.create_servo3.text,
                "servo_4": self.create_servo4.text
                }
                header = {'Authorization': f'Token {token}'}
                create_response = requests.post(url,data= data, headers = header)
                if create_response.status_code == 201 :
                    self.create_result.text = "Success"
                elif create_response.status_code == 400 :
                    self.create_result.text = f"{self.create_modename.text} already exists... Choose another name"
                else:
                    raise NameError

        except NameError:
            self.create_result.text = "Error Please try again"
            
        except:
            self.create_result.text = "No Internet"

    def clearcreatebtn(self):
        self.create_modename.text = ""
        self.create_servo1.text = ""
        self.create_servo2.text = ""
        self.create_servo3.text = ""
        self.create_servo4.text = ""
        self.create_led.text = ""
        self.create_result.text = ""






class EditMode(Screen):
    global token
    edit_modename = ObjectProperty(None)
    edit_servo1 = ObjectProperty(None)
    edit_servo2 = ObjectProperty(None)
    edit_servo3 = ObjectProperty(None)
    edit_servo4 = ObjectProperty(None)
    edit_led = ObjectProperty(None)
    edit_result  = ObjectProperty(None)
    edit_view_data_number = ObjectProperty(None)
    editviewnow = ObjectProperty(None)

    def vieweditbtn(self):
        try:
            if self.edit_view_data_number.text == "" :
                raise NameError
            else:
                data = int(self.edit_view_data_number.text)
                url = f"{URL}/api/mode_list/{data}"
                header = {'Authorization': f'Token {token}'}
                edit_view_response = requests.get(url,headers = header)
                if edit_view_response.status_code == 404:
                    self.edit_result.text = f"Mode {self.edit_view_data_number.text} not available"
                else:
                    edit_view_data = edit_view_response.json()
                    self.edit_modename.text = str(edit_view_data['mode_id'])
                    self.edit_servo1.text = str(edit_view_data['servo_1'])
                    self.edit_servo2.text = str(edit_view_data['servo_2'])
                    self.edit_servo3.text = str(edit_view_data['servo_3'])
                    self.edit_servo4.text = str(edit_view_data['servo_4'])
                    self.edit_led.text = str(edit_view_data['led'])
                    self.edit_result.text = "Tap Update to update"

        except NameError:
            self.edit_result.text = "Please enter a number"

        except:
            self.edit_result.text = "No Internet"

    def editbtn(self):
        try:
            if self.edit_view_data_number.text == "" :
                raise NameError

            else:
                data = int(self.edit_view_data_number.text)
                url = f"{URL}/api/mode_list/{data}"
                data = {
                        "mode_id": self.edit_modename.text,
                        "led": self.edit_led.text,
                        "servo_1": self.edit_servo1.text,
                        "servo_2": self.edit_servo2.text,
                        "servo_3": self.edit_servo3.text,
                        "servo_4": self.edit_servo4.text
                }
                header = {'Authorization': f'Token {token}'}
                edit_response = requests.put(url,data= data, headers = header)
                if edit_response.status_code == 201 :
                    self.edit_result.text = "Success"
                elif edit_response.status_code == 404 :
                    self.edit_result.text = f"{self.create_modename.text} not available to update"
                else:
                    print(edit_response.status_code)
                    raise AttributeError

        except NameError:
            self.edit_result.text = "Enter a number"
        except AttributeError:
            self.edit_result.text = "Error Try again"  
        except:
            self.edit_result.text = "No Internet"

class Help(Screen):
    pass

class Logout(Screen):
    pass

class DeleteMode(Screen):
    global token
    delete_modename = ObjectProperty(None)
    delete_servo1 = ObjectProperty(None)
    delete_servo2 = ObjectProperty(None)
    delete_servo3 = ObjectProperty(None)
    delete_servo4 = ObjectProperty(None)
    delete_led = ObjectProperty(None)
    delete_result  = ObjectProperty(None)
    delete_view_data_number = ObjectProperty(None)
    deleteviewnow = ObjectProperty(None)

    def viewdeletebtn(self):
        try:
            if self.delete_view_data_number.text == "" :
                raise NameError
            else:
                data = int(self.delete_view_data_number.text)
                url = f"{URL}/api/mode_list/{data}"
                header = {'Authorization': f'Token {token}'}
                delete_view_response = requests.get(url,headers = header)
                if delete_view_response.status_code == 404:
                    self.delete_result.text = f"Mode {self.delete_view_data_number.text} not available"
                else:
                    delete_view_data = delete_view_response.json()
                    self.delete_modename.text = str(delete_view_data['mode_id'])
                    self.delete_servo1.text = str(delete_view_data['servo_1'])
                    self.delete_servo2.text = str(delete_view_data['servo_2'])
                    self.delete_servo3.text = str(delete_view_data['servo_3'])
                    self.delete_servo4.text = str(delete_view_data['servo_4'])
                    self.delete_led.text = str(delete_view_data['led'])
                    self.delete_result.text = "Tap Delete to delete"

        except NameError:
            self.delete_result.text = "Please enter a number"

        except:
            self.delete_result.text = "No Internet"

    def deletebtn(self):
        try:
            if self.delete_view_data_number.text == "" :
                raise NameError
            else:
                data = int(self.delete_view_data_number.text)
                url = f"{URL}/api/mode_list/{data}"
                header = {'Authorization': f'Token {token}'}
                delete_response = requests.delete(url, headers = header)
                if(delete_response.status_code == 410):
                    self.delete_result.text = "Success"
                elif(delete_response.status_code == 404):
                    self.delete_result.text = f"{self.delete_view_data_number.text} not found"
                else:
                    self.delete_view_data_number.text = "Error deletion not done!"

        except NameError:
            self.delete_result.text = "Please enter a number"

        except:
            self.delete_result.text = "No Internet"

    






class MainApp(App):
    def build(self):
        pass
















if __name__ == '__main__':
    app = MainApp()
    app.run()



























