''' Melhore o jogo do ex028 onde o computador vai pensar em um número inteiro entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''
from random import randint
computador = randint(0,10)
print('Tente adivinhar o número entre 0 e 10')
num = int(input('Qual é o seu palpite? '))
contador = 1
while num != computador:
    if num < computador:
        print('Mais... tente novamente')
    else:
        print('Menos... tente novamente')
    num = int(input('Qual é o seu palpite? '))
    contador += 1
print('Você acertou!')
print(f'Precisou de {contador} tentativas.')
