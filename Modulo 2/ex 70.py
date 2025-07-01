print('-'*20)
print('    LOJA BARATÃO')
print('-'*20)
menor =''
menorp= 0
cont = 0
total = 0.0
x =0
while True:
    x +=1
    nome = str(input('Informe o nome do produto: '))
    preco = float(input('Informe o preço do produto '))
    total += preco
    if preco > 1000:
        cont +=1
    if preco <menorp or x==1:
        menorp = preco
        menor = nome
    
    
    print('-'*25)
    o =''
    while o != 'S' and o !=  'N':
        o = str (input('Você deseja infomar mais um produto?[S/N] ')).strip().upper()[0]
        if o != 'S' and o !=  'N':
            print('Informação inválida. \n Tente novamente ...')
    if o == 'N':
        break
print(f'O total gasto na compra é {total}')
print(f'temos {cont} produtos custam mais de R$1000.')
print(f'O nome do produto mais barato é {menor}')

