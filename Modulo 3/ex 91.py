from random import randint
from operator import itemgetter
from time import sleep
lista= {
    'Jogador 1': randint(1,6),
    'Jogador 2': randint(1,6),
    'Jogador 3': randint(1,6),
    'Jogador 4': randint(1,6)}
for n, v in lista.items():
    print(f'O {n} tirou {v}')
    sleep(1)
print('-='*30)
ranking = sorted(lista.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    sleep(0.5+(0.5*i))
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')





