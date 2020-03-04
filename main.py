import requests
import easygui
import sys,os


#use 127.0.0.1:8000 for localhost

URL = "http://yoururl.com" 



def obtain_token():
    user = easygui.enterbox("Enter Username","Authentication")
    if(user== None):
        sys.exit(0)

    passwd = easygui.passwordbox("Password","Authentication")
    if(passwd== None):
        sys.exit(0)

    print(user)
    print(passwd)

    

    url = f"{URL}/api/auth/"
    response = requests.post(url,data={'username': user, 'password': passwd})
    if response.status_code == 400:
        easygui.msgbox("Invalid Credentials...","Oops!!")
        os.system('python3 main.py')
        sys.exit(0)
    #print(response.status_code)
    return response.json()

def get_data():
    url = f"{URL}/api/mode_list/"
    header = {'Authorization': f'Token {obtain_token()}'}
    response = requests.get(url,headers = header)
    mode_data = response.json()
    #print(mode_data)
    for m in mode_data:
       print(m)

def create_new():
    url = f"{URL}/api/mode_list/"
    data = {
        "mode_id": "liquid_4",
        "led": "off",
        "servo_1": 11,
        "servo_2": 2,
        "servo_3": 8,
        "servo_4": 9
    }
    header = {'Authorization': f'Token {obtain_token()}'}
    response = requests.post(url,data= data, headers = header)
    print(response.text)


def edit_data(mode_id):
    url = f"{URL}/api/mode_list/{mode_id}"
    data = {
        "mode_id": 'liquid_4',
        "led": 'off',
        "servo_1": 11,
        "servo_2": 11,
        "servo_3": 9,
        "servo_4": 9
    }
    header = {'Authorization': f'Token {obtain_token()}'}
    response = requests.put(url,data= data, headers = header)
    print(response.text, response.status_code)


def delete_data(mode_id):
    url = f"{URL}/api/mode_list/{mode_id}"
    header = {'Authorization': f'Token {obtain_token()}'}
    response = requests.delete(url, headers = header)
    if(response.status_code == 410):
        print('Done')
    elif(response.status_code == 404):
        print('Data does not exist')
    else:
        print('Error deletion not done!')


def specific_data(id):
    url = f"{URL}/api/mode_list/{id}"
    header = {'Authorization': f'Token {obtain_token()}'}
    response = requests.get(url,headers = header)
    mode_data = response.json()
    print(mode_data)
    #print(mode_data['servo_2'])



if __name__ == "__main__":
    #get_data()
    #create_new()
    #edit_data(3)
    #delete_data(3)
    specific_data(2)
    
