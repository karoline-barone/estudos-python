''' Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
Adicione também as docstrings dessa função para consulta pelo desenvolvedor.'''
def notas(* num, sit = False):
    dicionario = {}
    dicionario['total'] = len(num)
    dicionario['maior'] = max(num)
    dicionario['menor'] = min(num)
    dicionario['media'] = sum(num) / len(num)
    if sit == True:
        if dicionario['media'] >= 7:
            dicionario['situação'] = 'Boa'
        elif dicionario['media'] >= 5:
            dicionario['situação'] = 'Razoável'
        else:
            dicionario['situação'] = 'Ruim'
    return dicionario


resp = notas(5.5, 2.5, 10, 8.6, sit = True)
print(resp)