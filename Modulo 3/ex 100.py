# programa que sorteia 5 números e faz a soma dos números pares, utilizando função.
from random import randint
from time import sleep
def sorteador(v):
    
    print('números sorteados: ',end='')  
    for c in range(0, 5):
        v.append(randint(1,10))
        sleep(0.3)
        print(v[c],end=' ', flush=tuple)
def somapar(v):
    s =0
    for c in v:
        print (c)  
        if c%2==0:
            s +=c
    print (f'Somando os valores pares de {v} temos {s}')
#programa pincipal
v=list()

sorteador(v)
somapar(v)
