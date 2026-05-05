'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestacão mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.'''
casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salario? R$'))
anos = int(input('Em quantos anos vai pagar?'))
prestacao = casa / (anos * 12)
if prestacao > salario * 0.3:
    print(f'Empréstimo negado! O valor da prestacão R${prestacao:.2f} ultrapassa 30% de seu salário')
else: print(f'Empréstimo aprovado! Sua prestacão é R${prestacao:.2f}')
