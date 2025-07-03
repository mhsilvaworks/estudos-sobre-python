pessoa= list()
galera= list()
x='fdsgfg'
while True:
    nome =str(input('\033[mNome: ')).strip()
    peso= int(input('Peso: '))
    pessoa.append(nome)
    pessoa.append(peso)
    galera.append(pessoa[:])
    pessoa.clear()
    x='ee'
    while x not in 'SN':
        x= str(input('Você deseja informar mais dados?[S/N] ')).upper().strip()[0] 
        if x not in 'SN':
            print('\033[33mInválido. Tente novamente... \033[m')
        else: 
            if x == 'N':
                print('Indo para o resultado...')
                break
            
    if x == 'N':
        break
mai = list()
c =0
men = list()
print(f'Ao todo você registrou {len (galera)} pessoas.')
print('Analisando os pesos...')
for p in galera:    
  
    if c == 0 :
        mai.append(p[:])
        men.append(p[:])

    else:
        if p[1] >= mai[0][1]:
            if p[1] != mai[0][1]:
                mai.clear()
            mai.append(p[:])
        if p[1] <= men[0][1]:
            if p[1] != men[0][1]:
                men.clear()
            men.append(p[:])
    
    c+=1
print(galera)
print(f'\033[31mOs maior peso é {mai[0][1]}kg. Peso de ', end='')
for m in mai: 
    print(m[0],end=' ')
print(f'\n\033[32mOs menor peso é {men[0][1]}kg. Peso de ', end='')
for m in men:
    print(m[0], end=' ')

