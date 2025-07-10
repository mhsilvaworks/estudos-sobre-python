# Program com função que informa a maior nota, a menor, a média , a quantidade de notas informadas e asituação da turma (opcional) 
def notas(*notas, sit= False):
    cont=s =0

    dados = dict()
    dados['quantidade de notas'] = len(notas)
    for c in notas:
        s+=c
        if cont ==0:
            mai= 0
            men = 0
        if c > mai:
            mai = c
        if c < men:
            men = c            
    dados['menor nota'] = men
    dados['maior nota'] = mai
    m = s /len(notas)
    dados['média'] = m
    if sit:
        if m < 5.0:
            st = 'Péssimo'
        elif m >5 and m<= 6:
            st ='Médio' 
        elif m > 6 and m <7:
            st= 'Ok'
        elif m >=7 and m<= 9:
            st = 'Ótimo'
        elif m >9:
            st= 'Exelente'

        dados['situação'] = st  
    return dados
# Programa principal:
resp = notas(5.0 ,7.5, 8.0,3.5, 6.4,2.1, sit= True)
print(resp)