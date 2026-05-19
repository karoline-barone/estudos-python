#faca o computador "pensar" em um numero inteiro entre 0 e 5 e peca para o usuário tentar descobrir qual foi o numero escolhido pelo computador
#o programa devera escrever na tela se o usuario venceu ou perdeu
from random import randint
computador = randint(0,5)
num = int(input('Tente adivinhar o número (entre 0 e 5): '))
if num == computador:
    print('Acertou!')
else:
    print(f'Errou! Eu pensei no número {computador}.')