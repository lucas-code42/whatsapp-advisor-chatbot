# escrever códigos de teste...
import requests
from class_bot import Bot

def test_get_url():
    url = requests.head('https://api.adviceslip.com/advice')
    status = url.status_code
    obj = Bot()
    obj_url = obj.get_url()
    if status == obj_url.status_code:
        return True
    else:
        return False

def test_convert_to_json():
    pass

bot = Bot()
print(bot.show_url)

