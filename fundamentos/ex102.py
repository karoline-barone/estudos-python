'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular
e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''
def fatorial(num, show=False):
    """
    Calcula o fatorial de um número
    :param num: Número a ser calculado
    :param show: Mostrar ou não o cálculo do fatorial
    :return: Retorna o valor do fatorial do número
    """
    fatorial = 1
    for i in range(num, 0, -1):
        if show:
            if i > 1:
                print(f'{i} x ', end='')
            else:
                print(f'{i} = ', end='')
        fatorial *= i
    return fatorial


num = int(input('Digite o número que deseja saber o fatorial: '))
truefalse = str(input('Deseja ver o cálculo? Responda com True ou False: ')).strip().lower()
if truefalse == 'true':
    print(fatorial(num, show=True))
else:
    print(fatorial(num, show=False))

