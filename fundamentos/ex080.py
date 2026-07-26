'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''
valores = []
for i in range (0,5):
    novovalor = int(input(f'Digite um valor:'))
    if i == 0:
        valores.append(novovalor)
    elif novovalor > valores[-1]:
        valores.append(novovalor)
    else:
        for c in range(0,len(valores)):
            if novovalor <= valores[c]:
                valores.insert(c,novovalor)
                break
print(f'Os valores digitados em ordem foram {valores}')
