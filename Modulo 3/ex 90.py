# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
dados =dict()
dados['nome']= str(input('Nome: '))
dados['media'] = float(input('Média: '))
print('-='*30)
print(f'- O nome: {dados["nome"]}.')
print(f'- a média:  {dados["media"]}.')
if dados["media"] >=7.0:
    print('- Siltuação: aprovado.')
elif dados["media"]< 7.0 and dados["media"]>=5.0:
    print('- Situação: recuperção.')
else:
    print('- Situação: reprovado.')