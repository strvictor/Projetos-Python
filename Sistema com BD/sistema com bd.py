import requests
import json
database_cadastro = {}
database_login = {}
while True:
    print('')
    print('[ 1 ] - Cadastrar no sistema\n[ 2 ] - Entrar no sistema\n[ 3 ] - Sair do sistema')
    print('')
    opc = int(input('Sua opção: '))
    if opc == 1:
        print("==============================")
        database_cadastro['Usuario'] = input('Usuário: ')
        database_cadastro['Senha'] = input('Senha: ')
        conversao = json.dumps(database_cadastro)
        requisicao = requests.post('https://bancodedados-54d83-default-rtdb.firebaseio.com/.json', data=conversao)
        print("================================")
        print('Cadastro realizado com sucesso!')
        print("================================")
 
    elif opc == 2:
        print("")
        print('Informe seus dados abaixo')
        print("")
        database_login['Usuario'] = input('Usuário: ')
        
        requisicao_login = requests.get('https://bancodedados-54d83-default-rtdb.firebaseio.com/.json') #get no banco de dados
        caminhos = requisicao_login.json() # banco de dados no formato .json
        for caminho in caminhos: # pra percorrer em todo o banco de dados
            
            requisicao_login = requests.get(f'https://bancodedados-54d83-default-rtdb.firebaseio.com/{caminho}.json') # add o parametro pra percorrer o banco de dados
            
            verifica = requisicao_login.json() #mostra todos os usuarios do banco de dados
            
            if database_login['Usuario'] in verifica['Usuario']:
                
               
                database_login['Senha'] = input('Senha: ')
                
                if database_login['Senha'] == verifica['Senha']:
                    print('')
                    print('*'*28)
                    print('Login realizado com sucesso!')
                    print('*'*28)
                    break
                    
                else:
                    print("=======================")
                    print('Senha Incorreta')
                    print("=======================")
                    break
              
        if database_login['Usuario'] not in verifica['Usuario']:
            print("=======================")
            print('Usuário não encontrado!')
            print("=======================")
                
    elif opc == 3:
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        print(f'Sistema encerrado.\nObrigado(a) {database_login["Usuario"]}!')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        break
    else:
        print('Só é permitido um dos valores abaixo!')
