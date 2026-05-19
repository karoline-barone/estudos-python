''' Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas
- Quantas letras ao todo (sem considerar espacos)
- Quantas letras tem o primeiro nome'''
nome = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem {len(nome)-nome.count(' ')} letras')
print(f'Seu primeiro nome tem {len(nome.split()[0])} letras')
# outra forma: print(f'Seu primeiro nome tem {nome.find(' ')} letras')

