from random import randint
valor_aleatorio = int(randint(0,50))
tentativas = 0
while True:
    print('=' * 30)
    resp_usuario = int(input('Chute um número em 0 e 50: '))
    print('=' * 30)
    if resp_usuario > valor_aleatorio:
        print('')
        print(f'Seu ultimo chute foi {resp_usuario}, chute um valor mais baixo')
        print('')
    elif resp_usuario < valor_aleatorio:
        print('')
        print(f'Seu ultimo chute foi {resp_usuario}, chute um valor mais alto')
        print('')
    elif resp_usuario == valor_aleatorio:
        print('')
        print(f'Parabéns voce acertou!\nao todo foram {tentativas} tentativas')
        print('')
    tentativas += 1
