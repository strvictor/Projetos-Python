from time import sleep
print('=-'*20)
print('Seja bem vindo(a) ao nosso sistema\n** Escolha umas da opções abaixo **')
while True:
    print('=-'*20)
    print('[ 1 ] - Cadastrar no sistema\n'
          '[ 2 ] - Entrar no sistema\n'
          '[ 3 ] - Sair do sistema')
    print('=='*20)
    opcao_usuario = int(input('Qual a sua opção: '))
    if opcao_usuario == 1:
        cad_usuario = str(input('Informe um Usuário: '))
        print(f'Usuário {cad_usuario}, cadastrado com sucesso!')
        cad_senha = input('Informe uma senha com até seis caracteres: ')
        while len(cad_senha) < 6:
            print('Sua senha não cumpriu os critérios exigidos')
            print(' ')
            cad_senha = input('Informe novamente a senha: ')
        print('Senha cadastrada com sucesso!')
    elif opcao_usuario == 2:
        veri_usuario = str(input('Usuário: '))
        if veri_usuario == cad_usuario:
            veri_senha = input('Senha: ')
            if veri_senha == cad_senha:
                print('Logado com Sucesso!')
                break
            else:
                print('Senha Incorreta!')
                while True:
                    print('[ 1 ] - tentar novamente\n[ 2 ] - Sair')
                    opc = int(input('Sua opção: '))
                    if opc == 1:
                        veri_senha = input('Senha: ')
                        if veri_senha == cad_senha:
                            print('Logado com Sucesso!')
                            break
                    elif opc == 2:
                        break
                    else:
                        print('Escolha somente umas das opções abaixo')
        else:
            print('Usuário Incorreto!')
            while True:
                print('[ 1 ] - tentar novamente\n[ 2 ] - Sair')
                opc = int(input('Sua opção: '))
                if opc == 1:
                    veri_usuario = input('Usuário: ')
                    if veri_usuario == cad_usuario:
                        print(f'Usuário {cad_usuario} está correto!')
                        veri_senha = input('Senha: ')
                        if veri_senha == cad_senha:
                            print('Logado com sucesso!')
                            break
                        else:
                            print('Senha Incorreta!')
                            while True:
                                print('[ 1 ] - tentar novamente\n[ 2 ] - Sair')
                                opc = int(input('Sua opção: '))
                                if opc == 1:
                                    veri_senha = input('Senha: ')
                                    if veri_senha == cad_senha:
                                        print('Logado com Sucesso!')
                                        break
                                elif opc == 2:
                                    break
                                else:
                                    print('Escolha somente umas das opções abaixo')
                elif opc == 2:
                    break
                else:
                    print('Escolha somente umas das opções abaixo')
    elif opcao_usuario == 3:
        print('Sistema encerrando em...')
        for c in range(3, 0, -1):
            sleep(1)
            print(c)
        sleep(1)
        break
    else:
        print('Escolha somente umas das opções abaixo')
