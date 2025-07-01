num = (int(input('Informe um número inteiro:')),int(input('Informe um número inteiro:')),int(input('Informe um número inteiro:')),int(input('Informe um número inteiro:')))
print(f'Você digitou: {num}')
print(f'O número 9 foi digitado {num.count(9)} vezes.')
if 3 in num:
    print(f'O número 3 está na {num.index(3)+1}ª posição.')
else:
    print('O número 3 não foi digitado.')
print('Os valores pares digitados foram: ', end='')
for n in num:
    if n %2 ==0:
        print(n, end=' ')
