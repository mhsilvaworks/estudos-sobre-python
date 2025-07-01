print('-'*25)
print('Cadastre uma pessoa')
print('-'*25)
cnt = 0
H =0
f=0
list = ('homem', 'homens',  'mulher', 'mulheres')

while True:
    idade = int (input('Informe a idade: '))
    sexo = str (input('Informe o sexo [M][F]: ')).strip().upper()[0]
    print('-'*25)
    

    
    if idade >= 18:
        cnt +=1
    if sexo =='M':
        H +=1
    if sexo =='F':
        if idade >20:
            f += 1
    x = str (input('Deseja continuar [S/N]: ')).upper()[0]
    if x =='N':
        break
print (f'Total de pessoas maiores de idade: {cnt}')
print(f"Ao todo temos {H} {list[1] if H > 1 else list[0]}")
print(f'E temos {f} {list[3] if f > 1 else list [2]} com mais de 20 anos')