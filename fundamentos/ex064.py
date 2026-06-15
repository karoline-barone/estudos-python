''' Crie um programa que leia vários números inteiros pelo teclado.  O programa só vai parar quando o usuário digitar o
valor 999, que é a condicão de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles'''
num = int(input('Digite um numero inteiro [999 para parar]: '))
soma = 0
cont = 0
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um numero inteiro [999 para parar]: '))
print(f'Voce digitou {cont} numeros e a soma entre eles foi {soma}.')