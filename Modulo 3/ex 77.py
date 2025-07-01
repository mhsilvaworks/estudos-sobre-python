
cruzeiro = ('Celeste', 'Copa do Brasil', 'Guerreiro', 'Libertadores', 'Mineirao', 'Mineiro', 'Paixao', 'Raposa', 'Rivalidade', 'Ronaldo', 'Titulos', 'Tríplice Coroa')

for palavra in range (0,12):  
    print(f'\n{cruzeiro[palavra]}', end=': ')

    for x in range(len(cruzeiro[palavra])): 

        if cruzeiro[palavra][x] in 'aeiou':
            print(cruzeiro[palavra][x], end=' ')
        