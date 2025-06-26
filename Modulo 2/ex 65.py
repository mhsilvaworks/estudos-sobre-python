res = 'S'
cont = 0
media =0.0
while res =='S':
    n= int (input('Informe um número: '))
    res= (input ('Deseja informar outro número[S][N]? ')).upper()
    if cont ==0:
        maior=n
        menor =n
        
    if n < menor:
        menor=n
    if n > maior:
        maior =n
    cont+=1
    media += n
media = media/cont
print('Você digitou {} números e a média foi {}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
