c = ('\033[m',        # 0: RESET - Reseta para as cores padrão do terminal
     '\033[1;97;41m', # 1: BRANCO sobre VERMELHO (para erros ou alertas)
     '\033[1;97;44m', # 2: BRANCO sobre AZUL (para o título principal)
     '\033[1;97;42m', # 3: BRANCO sobre VERDE (alternativa para sucesso)
     '\033[1;30;43m', # 4: PRETO sobre AMARELO (para títulos de informação)
     '\033[1;97;45m', # 5: BRANCO sobre MAGENTA (outra opção)
     '\033[1;97m'     # 6: BRANCO BRILHANTE (para o texto da ajuda)
    )


def ajuda(com):
    título(f'Acessando o manual do comando\'{com}\'',4)
    print(c[5], end='')
    help(com)
    print(c[0], end='')

def título(msg, cor=0):
    tam =len(msg)+4
    print(c[cor], end='')
    print('~'* tam)
    print(f'  {msg}')
    print('~'* tam)
    print(c[0], end='')
    
# Programa princpal
comando  = ''
while True:
    título('Sistema de ajuda Pyhelp', 2)
    comando =str(input("função ou biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)   
título('ATÉ LOGO!', 4)     