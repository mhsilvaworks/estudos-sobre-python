matriz = []
m = []
for c in range(1,4):
    for i in range(1,4):
        n= int (input(f'Digite o valor da posição ({c},{i}): '))
        m.append(n)
    matriz.append(m[:])
    m.clear()
print(matriz[0])
print(matriz[1])
print(matriz[2])

