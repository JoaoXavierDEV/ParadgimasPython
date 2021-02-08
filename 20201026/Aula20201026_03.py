
def somapares(lista):
    soma = 0
    for valor in lista:
        if valor%2==0:
            soma += valor
    return soma

minha_lista = [1,2,3,4,5,6,7,8]
print(somapares(minha_lista))
        
        

