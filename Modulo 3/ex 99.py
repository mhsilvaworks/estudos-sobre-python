# Analizador de números para ver qual é o maior utilizando funções
from time import sleep
def maior(* num):
    cont = maior =0
    print('\nAnalizando os valores passsados...')
    if len(num)==0:
        maior = 0
    else:
        for v in num:
            sleep(0.3)
            print(v, end=' ', flush= tuple) 
            if cont >0:
                maior = v
            if v > maior:
                maior =v
    print(f'\nO maior valor é o número {maior}')
# Programa principal
maior (3,3,4,52,3,6)
maior(5, 67,7,5)
maior(1,2)
maior(6)
maior()