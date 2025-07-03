p=[]
i=[]
n=[]
while True:
    
    num = int(input('Digite um valor: '))
    n.append(num)
    if num%2==0:
        p.append(num)
    else:
        i.append(num)
    a = str(input('Deseja informar outro número?[S/N] ')).strip().upper()[0]
    if a in 'N':        
        print('Indo para o menu de resultados...')
        break
print(f'Os números informados foram: {n}')
print(f'Os números pares informados foram: {p} ')
print(f'Os valores impares informados foram: {i}')