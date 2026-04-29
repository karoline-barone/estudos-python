'''Leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra 'A'
- Em que posicão ela aparece a primeira vez
- Em que posicão ela aparece a ultima vez'''
frase = str(input('Digite uma frase: ')).strip().upper()
print(f'A letra "A" aparece {frase.count("A")} vezes')
print(f'Aparece pela primeira vez na posicao {frase.find("A")+1}')
print(f'Aparece pela ultima vez na posicao {frase.rfind("A")+1}')