
import math

#y=ax2+bx+c
#raiz = (-b +- sqrt(delta)) / 2a

a=float(input("Valor de a na equacao:"))
if a==0:
    print("Não é do segundo grau")
else:
    b=float(input("Valor de b na equacao:"))
    c=float(input("Valor de c na equacao:"))
    delta = b**2 - 4 * a * c
    vertice = -b / (2 * a)
    if delta < 0:
        print("Não tem raizes reais")
    elif delta==0:
        print("Tem apenas uma raiz")
        print(vertice)
    else:
        print("Tem duas raizes")
        r1 = vertice + math.sqrt(delta)
        r2 = vertice - math.sqrt(delta)
        print(r1,r2)
        
