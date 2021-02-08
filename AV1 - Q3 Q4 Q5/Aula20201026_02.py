a = float(input("Valor de A:"))
b = float(input("Valor de B:"))
c = float(input("Valor de C:"))

delta = b**2-4*a*c
if delta < 0: 
    print("Não apresenta raizes")
else:
    raiz1 = (-b + delta**0.5)/2*a
    raiz2 = (-b - delta**0.5)/2*a
    print(raiz1)
    print(raiz2)


