# Contador usando funções.
from time import sleep
def contador(a,b, c):
    print(f'\nContagem de {a} a {b} pulando de {c} em {c}:')
    if a <b:
        for i in range(a, b+1,c ):
            sleep(1.0)
            print(i,end=' ',flush= tuple )
    else:
        for i in range(a,b,-c):
            sleep(1.0)
            print(i,end=' ', flush= tuple)
contador(1,10,1)

contador(10,1,1)
print('-=')
print('Agora é a sua vez...')
a =int (input('Informe o número inicial: '))
b =int (input('Informe o número final: '))
c =int (input('Informe de quantos em quantos passos: '))
contador(a,b,c)
