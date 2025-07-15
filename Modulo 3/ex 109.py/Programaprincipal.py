import pasta
x = int(input('Informe algum valor: R$'))
print(f'Se aumentar 10%: {pasta.aumentar(x,10,True)}')
print(f'Se diminuir 10%: {pasta.diminuir(x,10, True)}')
print(f'Se dobrar: {pasta.dobro(x, True)}')
print(f'Se dividir por 2: {pasta.metade(x, True)}')