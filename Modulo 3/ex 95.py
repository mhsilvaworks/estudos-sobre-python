# Programa onde é realizado a leitura de dados (nome, partidas e gols), onde a saida deve infomar os dados de tdos e após isso ter a opção de consultar os dados de cada jogador de modo separado.
from time import sleep
dados = dict()
jogos = list() 
lista = list()
t=0
while True:
    x='e'
    dados['nome'] = str(input('Nome do jogador: ')).strip()
    n = int(input('Quantas partidas: '))
    for c in range (0,n):
        gols= int (input(f'Quantos gols no {c+1}º jogo? '))
        jogos.append(gols)
        t += gols
    dados['gols'] = jogos.copy()
    dados['total'] = t
    jogos.clear()
    lista.append(dados.copy())
    while x not in 'SN':
        x= str(input('Quer continuar?[S/N] ')).upper().strip()[0] 
        if x not in 'SN':
            print('\033[33mErro digite apenas S on N. \033[m')
        else: 
            if x == 'N':
                break
    dados.clear()
    t =0
    if x == 'N':
        break

print('-='*40)
print('No. | Jogador      | gols       | Total de gols ')
print('_'*50)
for k,v in enumerate(lista):
    print(f'{k:<5}',end='')
    for b in v.values():
    
            print(f'{str(b):<15}', end='')
    print()
    sleep(0.7)
print('_'*50)
while True:
    r = int(input('Informe o número do jogador que você deseja as informações(999 para encerrar): '))
    if  r == 999:
        print('Encerrando', end='')
        sleep(0.5)
        print('.',end='')
        sleep(0.6)
        print('.',end='')
        sleep(0.7)
        print('.',end='')
        sleep(0.4)
        break
    elif r >= len(lista) or r <0:
        
        print(f'ERRO, o número {r} não corresponde a nenhum jogador.')
    else:
        print(f'--- LEVANTAMENTO DO JOGADOR {lista[r]["nome"]} ---')
        print(f'    Jogou {len(lista[r]["gols"])} jogos')
        for k,v in enumerate (lista[r]['gols']):
            print(f'        Gols no jogo {k+1}: {v}.')
        print(f'    Total de gols: {lista[r]["total"]}')
        
        print('-'*35)