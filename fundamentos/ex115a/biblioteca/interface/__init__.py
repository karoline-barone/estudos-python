def linha(tam = 40):
    return '\033[33m-\033[m' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())


def menu(lista):
    cabecalho('\033[34mMENU PRINCIPAL\033[m')
    i = 1
    for item in lista:
        print(f'\033[32m{i} -\033[m {item}')
        i+=1
    print(linha())
    escolha = leiaInt('\033[32mEscolha sua opção: \033[m')
    return escolha

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