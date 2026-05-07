''' Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais'''
valor1 = int(input('Informe o primeiro valor: '))
valor2 = int(input('Informe o segundo valor: '))
if valor1 == valor2:
    print('Não existe valor maior, os dois são iguais.')
elif valor1 > valor2:
    print('O primeiro valor é maior.')
else:
    print('O segundo valor é maior.')
