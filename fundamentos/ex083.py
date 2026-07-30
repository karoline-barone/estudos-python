'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a
expressão passada está com os parênteses abertos e fechados na ordem correta.'''
exp = str(input('Digite sua expressão: '))
lista = []
for i in exp:
    if i == '(':
        lista.append(i)
    elif i == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(i)
            break
if len(lista) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está invalida!')
