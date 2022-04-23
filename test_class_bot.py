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
    obj = Bot()
    obj.get_url()
    teste = obj.convert_to_json()
    if (type(teste) == dict):
        return True
    else:
        False

def test_json_to_str():
    obj = Bot()
    obj.get_url()
    obj.convert_to_json()
    teste = obj.json_to_str()
    if (type(teste == str)):
        return True
    else:
        return False


def test_check_number_list(arr):
    obj = Bot()
    teste = obj.check_number_list(arr)
    validate_this = ['+', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    trash_list = []
    clean_list = []
    if teste == False:
        return True
    else:
        for array in teste:
            for item in array:
                if item not in validate_this:
                    trash_list += item
                else:
                    clean_list += item
        return_dict = {
            'ok_values': clean_list,
            'trash_values': trash_list,
        }
        return return_dict


def main():    
    test_1 = test_get_url()
    test_2 = test_convert_to_json()
    test_3 = test_json_to_str()
    test_4 = test_check_number_list(['teste', '9999', '+5511941064901'])

    list_returns = {
        'test_1': test_1,
        'test_2': test_2, 
        'test_3': test_3,
        'test_4': test_4,
    }
    return list_returns
