lista = [[],[]]
for c in range(1,8):
    n = int (input(f'Digite o {c}º número: '))
    if n%2==0:
        lista[0].append(n)
    else:
        lista[1].append(n)


print(f'Números pares: {lista[0]}')
print(f'Números impares: {lista[1]}')