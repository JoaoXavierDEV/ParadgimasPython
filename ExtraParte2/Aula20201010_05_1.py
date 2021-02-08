
def imprimir(n):
    for i in range(n):
        valor = "{:d} ".format(i+1)
        print((i+1)*valor)
imprimir(9)

# o exercicio 2 seria mais complicado
def imprimir2(n):
    valores = []
    for i in range(n):
        valores.append("{:d}".format(i+1))
        print(" ".join(valores))
imprimir2(9)        

