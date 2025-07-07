# programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
dados = dict()
jogos = list()
t=0
dados['nome'] = str(input('Qual o nome do jogador: ')).strip()
n = int(input('Quantas partidas: '))

for c in range (0,n):
    gols= int (input(f'Quantos gols no {c+1}º jogo? '))
    jogos.append(gols)
    t += gols

dados['total'] = t
dados['gols'] = jogos
print('-='*30)
print(dados)
print('-='*30)
for k, v in dados.items():
    print(f'O campo {k} tem valor {v}')
print('-='*30)
print(f'O jogador {dados["nome"]} jogou {n} jogos.')
for c in range(0,n):
    print(f'=> Na partida  {c+1}, fez {dados["gols"][c]} gols')
print(f'Ao todo o jogador {dados["nome"]} fez {dados["total"]} gols')