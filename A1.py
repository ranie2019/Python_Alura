print('*' * 20)
print('JOGO DE ADIVINHACAO')
print('*' * 20)

ns = 42
tentativas = 5
rodada = 1

while rodada <= tentativas:
    print(f'voce tem {rodada} de {tentativas} ')
    chute = int(input('DIGITE UM NUMERO: '))
    print(f'voce digitou {chute}')
    if ns == chute:
        print('voce acertou')
    else:
        if chute > ns:
            print('Voce erro seu numero e maior que o secreto')
        else:
            print('voce errou seu numero e menor que o secreto')
    rodada = rodada + 1
print('Acabou')

