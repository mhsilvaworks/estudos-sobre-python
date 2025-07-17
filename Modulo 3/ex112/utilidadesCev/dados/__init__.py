def leiaDinheiro(pergunta):
    value = False
    while value is False:
        x = str(input(pergunta)).strip().replace(',','.')
        
        if x.isalpha() or x =='':
            print(f'\033[31mErro: "{x}" é um preço inválido.\033[m')
        else:
            x= float(x)
            value = True
    return x