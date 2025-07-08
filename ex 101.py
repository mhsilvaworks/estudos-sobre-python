def voto(x):
    if x >16 and x<18 or x>=70:
        return 'Opcional'
    elif x >=18:
        return 'Obrigatório'
    elif x<16:
        return'Negado'
        
idade = int(input('Idade: '))
print(voto(idade))