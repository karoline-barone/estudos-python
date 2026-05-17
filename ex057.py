#leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peca a digitacao novamente até ter um valor correto
sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados inválidos. Digite o sexo [M/F]: ')).strip().upper()
print(f'Sexo {sexo} registrado com sucesso!')