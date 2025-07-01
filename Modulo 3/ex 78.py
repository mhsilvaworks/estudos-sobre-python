lista =[]
p = ('primeiro', 'segundo','terceiro','quarto','quinto')
cont =0
for c in range (0,5):
    lista.append (input(f'Informe o {p[c]} número: '))
print(lista)
print (f'O maior número digitaddo foi {max(lista)} e se encontra', end=' ')
for i, f in enumerate (lista):
    if lista[i] >=max(lista):
        print(f' na {i+1}ª', end='')
        cont+=1
if cont > 1:
    print(' posições.')
else:
    print(' posição')
cont =0
print (f'O menor número digitaddo foi {min(lista)} e se encontra', end='')
for j,k in enumerate (lista):
    if lista[j] <=min(lista):
        print(f' na {j+1}ª', end='')
        cont+=1
if cont > 1:
    print(' posições.')
else:
    print(' posição')