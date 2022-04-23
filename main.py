from class_bot import Bot
from test_class_bot import main

if __name__ == '__main__':

    while True:

        test_integration = main()
        validation = None

        for key, returns_value in test_integration.items():
            if returns_value == True:
                continue
            else:
                print(f'{key}: {returns_value}')
                validation = False
                break

        if validation == False:
            print("encerrando aplicação...")
            break
        else:
            print("Todos os testes obtiveram exito, aplicação irá iniciar.")

        bot_obj = Bot()
        bot_obj.get_url()
        bot_obj.verify_url_response()
        bot_obj.convert_to_json()
        msg = bot_obj.json_to_str()

        print()
        print('Bem vindo ao chatbot conselheiro para WhatsApp!')
        print()
        print('Antes de continuar precisamos de algumas informações...')
        print()
        print('Adcione quantos contatos precisa a lista de contatos, assim que não quiser mais adicionar mais nenhum contato, aperte "xxx".\n Não se esqueça de manter o formato adequado, "+{cod pais}{cod cidade}{numero}".')

        number_list = []

        finish = ''
        while True:
            if finish == 'xxx':
                break
            contact_number = str(input("Número: "))
            number_list.append(contact_number)
            finish = str(input('Para finalizar digite xxx, continuar tecle "enter": '))

        number_list = bot_obj.check_number_list(number_list)
        if number_list == False:
            print(number_list)
        else:
            send_msg = bot_obj.send_msg_to_contacts()