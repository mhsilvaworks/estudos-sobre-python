import pasta
x = int(input('Informe algum valor: R$'))
print(f'Se aumentar 10%: \n{pasta.moeda(pasta.aumentar(x,10))}')
print(f'Se diminuir 10%: \n{pasta.moeda(pasta.diminuir(x,10))}')
print(f'Se dobrar: \n{pasta.moeda(pasta.dobro(x))}')
print(f'Se dividir por 2: \n{pasta.moeda(pasta.metade(x))}')