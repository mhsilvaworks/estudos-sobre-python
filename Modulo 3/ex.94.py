# programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média
dados = dict()
lista = list()
soma =media=0 
while True:
    x=y= 'e'
    dados['nome'] = str(input('Nome: '))
    while y not in 'MF':
        y = str(input('Sexo(M/F): ')).strip().upper()[0]
        if y not in 'MF':
            print('\033[33mErro digite apenas M ou F \033[m')
    dados['sexo'] = y
    idade = int(input('Idade: '))
    soma += idade
    dados ['idade'] =idade
    
    
    lista.append(dados.copy())
    
    while x not in 'SN':
        x= str(input('Quer continuar?[S/N] ')).upper().strip()[0] 
        if x not in 'SN':
            print('\033[33mErro digite apenas S on N. \033[m')
        else: 
            if x == 'N':
                print('')
                break
    dados.clear()
    if x == 'N':
        break
print(lista) 
media =soma/ len(lista)
print('-='*30)
print(f'a) Ao todo nos temos {len(lista)} pessoas.')
print(f'b) A média de idade é {media:5.2f}')
print('c) As mulheres são:: ', end='')
for p in lista:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print('\nd) Pessoas com a idade acima da média: ',end='')
for p in lista: 
    if p['idade'] >= media:
        print(f'{p["nome"]}', end=' ')
