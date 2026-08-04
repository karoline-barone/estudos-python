'''Faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''
from random import randint
jogo = []
total = []
qtdd = int(input('Quantos jogos deseja gerar? '))
for i in range(qtdd):
    for j in range(0, 6):
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
    jogo.sort()
    total.append(jogo[:])
    jogo.clear()
for i, j in enumerate(total):
    print(f'Jogo {i+1}: {j}')
