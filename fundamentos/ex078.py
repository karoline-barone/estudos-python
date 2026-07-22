''' Faça um programa que leia 5 valores e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor
digitado e as suas respectivas posições na lista.'''
valores = []
for i in range (0,5):
    valores.append(int(input(f'Digite o valor da posição {i}:')))
maior = max(valores)
menor = min(valores)
print(f'O maior valor é {maior} e foi encontrado nas posições: ', end = '')
for j, i in enumerate(valores):
    if i == maior:
        print(j, end = ' ')
print(f'\nO menor valor é {menor} e foi encontrado nas posições: ', end = '')
for j, i in enumerate(valores):
    if i == menor:
        print(j, end = ' ')
