# Programa com função de conferir se o dado informado é um número inteiro
def leiaint(n):
    while True:
        if n.isnumeric():
            break
        else:
            print('\033[31mErro: Digite um número inteiro válido.\033[m')
            n = str (input('Digite um número n: '))
    return n

#programa principal
n = str (input ('DIgite o número n: '))
print(f'Você acabou de digitar o número {leiaint(n)}')