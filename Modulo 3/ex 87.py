matriz = [['0','0','0'], ['0','0','0'], ['0','0','0']]
sp=0
st =0

for i in range(0,3):
    for j in range(0,3):
        matriz[i][j]= int(input(f'Digite o valor para a posição ({i+1},{j+1})'))
        if matriz[i][j]%2 ==0:
            sp += matriz[i][j]
        if j ==2:
            st += matriz[i][j] 
mai = matriz[1][0]
if matriz[1][1]> mai:
    mai= matriz[1][1]
elif matriz[1][2]>mai:
    mai=matriz[1][2]        
        
print(matriz[0])
print(matriz[1])
print(matriz[2])

print(f'A soma de todos os números pares é {sp}')
print(f'A soma de todos os números da terceira coluna é {st}')
print(f'O maior número da segunda linha é {mai}')