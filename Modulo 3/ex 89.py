aluno = list()
alunos = list()
while True:
    aluno.append( str(input('Nome: ')))
    aluno.append( float(input('Nota1: ')))
    aluno.append( float(input('Nota2: ')))
    alunos.append(aluno[:])
    aluno.clear()
    x='ee'
    while x not in 'SN':
        x= str(input('Você deseja informar mais dados?[S/N] ')).upper().strip()[0] 
        if x not in 'SN':
            print('\033[33mInválido. Tente novamente... \033[m')
        else: 
            if x == 'N':
                print('Calculando notas...')
                break
            
    if x == 'N':
        break
print('=-'*30)
print(' No. |  Nome    |  Média  |')
print('---------------------------')
for c in range (0, len(alunos)):
    print(f'   {c} | {alunos[c][0]} |{(alunos[c][1] + alunos[c][2])/2}|')
x =0
while x!=999:
    x= int(input('Deseja consultar os dados de algum aluno, se sim informe o número dele[999 para encerrar]: '))
    if x in range(0,len(alunos)):
        print(f'Aluno:{alunos[x][0]} nota1:{alunos[x][1]} nota2:{alunos[x][2]}')
    else:
        print('\033[33mNúmero inválido favor inserir um número de um aluno existente. Tente novamente...\033[m')
