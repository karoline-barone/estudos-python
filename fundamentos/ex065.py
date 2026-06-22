'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a
digitar valores'''
num = int(input('Digite um número inteiro: '))
cont = 1
soma = num
maior = num
menor = num
resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
while resp == 'S':
    num = int(input('Digite um número inteiro: '))
    cont += 1
    soma += num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
media = soma / cont
print(f'Você digitou {cont} números e a média deles é {media:.2f}.')
print(f'O maior número foi {maior} e o menor foi {menor}.')


