#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
            'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for i in range(0, len(palavras)):
    print(f'\nNa palavra {palavras[i]} temos as vogais: ', end = '')
    for letra in palavras[i]:
        if letra in 'aeiou':
            print(letra, end = ' ')
