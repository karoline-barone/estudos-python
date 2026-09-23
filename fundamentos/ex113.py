'''Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de
tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.'''
def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[031mERRO: por favor digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[031mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return num

def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('\033[031mERRO: por favor digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[031mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return num


ni = leiaInt('Digite um número inteiro: ')
nf = leiaFloat('Digite um número real: ')
print(f'O número inteiro digitado foi {ni} e o real foi {nf}')
