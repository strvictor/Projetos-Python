import requests
import json
database_cadastro = {}
database_login = {}
while True:
    print('[ 1 ] - Cadastrar no sistema\n'
          '[ 2 ] - Entrar no sistema\n'
          '[ 3 ] - Sair do sistema')
    opc = int(input('Sua opção: '))
    if opc == 1:
        database_cadastro['Usuario'] = input('Usuário: ')
        database_cadastro['Senha'] = input('Senha: ')
        conversao = json.dumps(database_cadastro)
        requisicao = requests.post('https://teste-ce0c3-default-rtdb.firebaseio.com/.json', data=conversao)
    elif opc == 2:
        database_login['Usuario'] = input('Usuário: ')
        requisicao_login = requests.get('https://teste-ce0c3-default-rtdb.firebaseio.com/.json')
        caminho = requisicao_login.json()
        for values in caminho:
            requisicao_login = requests.get('https://teste-ce0c3-default-rtdb.firebaseio.com/'+values+'.json')
            verifica = requisicao_login.json()
            if database_login['Usuario'] == verifica['Usuario']:
                database_login['Senha'] = input('Senha: ')
                if database_login['Senha'] == verifica['Senha']:
                    print('Login bem sucedido :)')
                else:
                    print('Senha incorreta :(')
            else:
                print('Usuario incorreto :(')
    elif opc == 3:
        break
