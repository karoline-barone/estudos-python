'''Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.'''
def ajuda(comando):
    print("\033[30;44m", end="")
    help(comando)
    print("\033[0m")


comando = ''
while True:
    comando = str(input("\033[30;43mDigite o comando que você deseja ajuda:\033[0m "))
    if comando == 'FIM':
        break
    else:
        ajuda(comando)
