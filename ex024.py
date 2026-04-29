#leia o nome de uma cidade e diga se ela comeca ou nao com o nome "Santo"
nome = str(input('Digite o nome da sua cidade: ')).strip()
print(nome[:5].capitalize() == 'Santo')

