'''Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante a função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt('Digite um n: ')'''
def leiaInt(msg):
    while True:
        dado = input(msg) #Lê o que o usuário digitou usando a mensagem passada
        if dado.isnumeric(): #Verifica se é um número válido
            return int(dado) #Retorna o número inteiro e encerra o laço
        else:
            print('Erro! Digite um número inteiro válido.')


n = leiaInt('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {n}')