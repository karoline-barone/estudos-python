'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um
boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
aluno = []
lista = []
while True:
    aluno.append(str(input('Nome: ')))
    nota1 = float(input('Nota 1: '))
    aluno.append(nota1)
    nota2 = float(input('Nota 2: '))
    aluno.append(nota2)
    media = (nota1 + nota2) / 2
    aluno.append(media)
    lista.append(aluno[:])
    aluno.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'{"Numero":<10}{"Nome":<15}{"Média":<10}')
for i, j in enumerate(lista):
    print(f'{i:<10}{j[0]:<15}{j[3]:<10}')
while True:
    escolha = int(input('Digite o número do aluno que deseja ver as notas (999 interrompe)'))
    if escolha == 999:
        break
    if escolha <= len(lista) - 1:
        print(f'As notas do aluno {lista[escolha][0]} são {lista[escolha][1]} e {lista[escolha][2]}')
