def aumentar(v=0, p=0, format= False):
    r=(v*((100+p)/100))  
    return r if format is False else moeda (r)
def diminuir(v=0, p=0,format= False):
    r= v*((100-p)/100)
    return r if format is False else moeda (r)
def dobro(v=0,format= False):
    r  = v*2
    return r if format is False else moeda (r)
def metade(v=0,format= False):
    r = v/2
    return r if format is False else moeda (r)
def moeda(p= 0, m ='R$',format= False):
    p = float(p)
    return f'{m}{p:.2f}'.replace('.',',') 
def resumo (x,a,b):
    print('='*35)
    print(f'{'RESUMO':>20}')
    print('='*35)
    print(f'Se aumentar 10%: {aumentar(x,a,True)}')
    print(f'Se diminuir 10%: {diminuir(x,b, True)}')
    print(f'Se dobrar: {dobro(x, True)}')
    print(f'Se dividir por 2: {metade(x, True)}')
    print('='*35)