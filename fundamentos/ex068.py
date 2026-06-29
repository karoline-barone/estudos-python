'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
from random import randint
vitorias = 0
while True:
    pc = randint(0,10)
    pessoa = int(input('Digite um número: '))
    soma = pc + pessoa
    opcao = input('Digite P para par ou I para ímpar: ').upper()
    print(f'Você jogou {pessoa} e o computador {pc}. Total de {soma}.')
    if opcao == 'P':
        if soma % 2 == 0:
            print('Você venceu!')
            vitorias += 1
        else:
            print('Você perdeu!')
            break
    elif opcao == 'I':
        if soma % 2 == 0:
            print('Você perdeu!')
            break
        else:
            print('Você venceu!')
            vitorias += 1
    else:
        print('Opção invalida! Reiniciando jogada.')
print(f'Fim! Você conseguiu um total de {vitorias} vitórias consecutivas.')
