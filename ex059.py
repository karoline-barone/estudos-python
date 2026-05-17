'''Crie um programa que leia dois valores e mostre um menu: [1]somar [2]multiplicar [3]maior [4]novos números [5]sair do programa
Seu programa deverá realizar a operacao solicitada em cada caso'''
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
escolha = 0
while escolha !=5:
    escolha = int(input('''Menu:
     [1]Somar
     [2]Multiplicar
     [3]Maior
     [4]Novos números
     [5]Sair\n'''))
    if escolha == 1:
        print(f'A soma dos números é {valor1 + valor2}.')
    elif escolha == 2:
        print(f'A multiplicação dos números é {valor1 * valor2}.')
    elif escolha == 3:
        if valor1 > valor2:
            print(f'O maior valor é {valor1}.')
        else:
            print(f'O maior valor é {valor2}.')
    elif escolha == 4:
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))
    elif escolha == 5:
        print('Fim.')
    else:
        print('Valor inválido. Tente novamente.')
