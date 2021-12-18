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
        print('Cadastro realizado com sucesso!')
    elif opc == 2:
        print('Informe seus dados abaixo')
        database_login['Usuario'] = input('Usuário: ')
        requisicao_login = requests.get('https://teste-ce0c3-default-rtdb.firebaseio.com/.json')
        caminhos = requisicao_login.json()
        for caminho in caminhos:
            requisicao_login = requests.get(f'https://teste-ce0c3-default-rtdb.firebaseio.com/{caminho}.json')
            verifica = requisicao_login.json()
            if database_login['Usuario'] in verifica['Usuario']:
                while True:
                    database_login['Senha'] = input('Senha: ')
                    if database_login['Senha'] == verifica['Senha']:
                        print('Login realizado com sucesso!')
                        break
                    else:
                        print('Senha incorreta, quer tentar novamente ?\n[ 1 ] - para tentar novamente [ 2 ] - para sair')
                        opc2 = int(input('Sua opção: '))
                        if opc2 == 2:
                            break
    elif opc == 3:
        print('Sistema encerrado.\nObrigado(a)!')
        break
    else:
        print('Só é permitido um dos valores abaixo!')
