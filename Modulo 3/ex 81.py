n = []
x =0
c = []
a =''
while True:
    
    num = int(input('Digite um valor: '))
    n.append(num)
    if n[x] ==5:
        c.append(x)
   
    x += 1
    a = str(input('Deseja informar outro número?[S/N] ')).strip().upper()[0]
    if a in 'N':        
        print('Indo para o menu de resultados...')
        break
            
    
n.sort(reverse=True)
print('-='*30)
print(f'Foram digitados {x} números.')
print(f'Você digitou {len(c)} números')
print(f'Os números que você digitou em ordem decrescente é {n}')
