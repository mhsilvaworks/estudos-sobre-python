matriz = [['0','0','0'], ['0','0','0'], ['0','0','0']]
for i in range(0,3):
    for j in range(0,3):
        matriz[i][j]= int(input(f'Digite o valor para a posição ({i+1},{j+1})'))
print(matriz[0])
print(matriz[1])
print(matriz[2])