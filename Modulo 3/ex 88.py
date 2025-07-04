from random import randint
lista=list()
jogos= list()
print('       SORTEADOR DE JOGOS')
r = int (input('Você deseja sortear quantos jogos: '))
for c in range (0, r):
    for i in range (0,6):
        jogos.append(randint(1,60))
        jogos.sort()
    lista.append(jogos[:])
    jogos.clear()

for c in range (0,r):
    print(f'\n\033[34m{c+1}º jogo: ',end='')
    for j in range(0,6):
        print(lista[c][j], end=' ')
print('\n\033[mBoa sorte.')