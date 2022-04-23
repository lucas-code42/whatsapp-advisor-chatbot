import pyautogui
import requests
import pywhatkit
import time
from datetime import datetime

class Bot:
    """Classe que modula as ações do bot"""
    def __init__(self,):
        self.url = 'https://api.adviceslip.com/advice'
        self.json = None
        self.msg = ''
        self.contacts = None

    @property
    def show_url(self,):
        return self.url

    def get_url(self,):
        self.url = requests.get(self.url)
        return(self.url)

    def verify_url_response(self,):
        if self.url.status_code != 200:
            print(f'Houve uma falha na requisição\nResponse {self.url.status_code}')
            return False
        else:
            return True

    def convert_to_json(self,):
        if self.verify_url_response == False:
            print('Houve uma falha ao tentar converter a requisição em Json.')
            return False
        else:
            self.json = self.url.json()
            return self.json

    def json_to_str(self,):
        self.msg = self.json['slip']
        self.msg = self.msg['advice']
        return self.msg

    def check_number_list(self, arr):
        chars = ['+', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in arr:
            if len(i) != 14:
                return False
            else:
                for x in i:
                    if x in chars:
                        continue
                    else:
                        return False
        self.contacts = arr
        return self.contacts

    def send_msg_to_contacts(self,):
        while len(self.contacts) >= 1:
            for i in range(len(self.contacts)):
                if len(self.contacts) == 0:
                    break
                j = 0
                pywhatkit.sendwhatmsg(self.contacts[j], self.msg, datetime.now().hour, datetime.now().minute + 2)
                del self.contacts[0]
                time.sleep(10)
                pyautogui.FAILSAFE = False
                a, b = pyautogui.size()
                pyautogui.moveTo(a, b)
                pyautogui.press('enter')
                time.sleep(10)

