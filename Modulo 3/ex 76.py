print('-'*27)
print('LLISTAGEEM DE PRODUTOS')
print('-'*27)
listagem =('Lápis', 1.75,
'Borracha', 2,
'Caderno', 15.90,
'Estojo', 25,
'Transferidor', 4.20,
'Compasso', 9.99,
'Mochila', 120.32,
'Canetas', 22.30,
'Livro', 34.90)
for pos in range (len(listagem)):
    if pos%2 ==0:
        # Se o pos for par ele vai se referir ao nome do produto
        print(f'{listagem[pos]:.<30}', end='' )
        # Ao usar o :.<30 siginifica que vai usar 30 espaços e o que não for prenchido será adicionado '.' e o < é para formatar para a esquerda.
    else:
        print(f'R$ {listagem[pos]}')