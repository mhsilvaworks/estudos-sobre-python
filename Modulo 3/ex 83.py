ex = str(input ('Digite a expressão: '))
pilha = []
for f in ex:
    print(f)
    if f in  '(':
        pilha.append(f)
    elif f in ')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(f)
            break
if len(pilha) ==0:
    print('Expressão está correta.')
else:
    print('expressão errada.')