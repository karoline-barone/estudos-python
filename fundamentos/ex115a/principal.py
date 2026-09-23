'''Ex115 - Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto
simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
Parte a - Criar um menu em python usando modularização'''
from ex115a.biblioteca.interface import *
from time import sleep

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    match resposta:
        case 1:
            cabecalho('Opção 1')
        case 2:
            cabecalho('Opção 2')
        case 3:
            cabecalho('Saindo do sistema...')
            break
        case _:
            print('\033[31mErro! Digite uma opção válida\033[m')
    sleep(2)
