def mul(a,b):
    return a*b

m1 = lambda a,b: a*b

print(mul(4,2))
print(m1(4,2))

def somatorio(lista,funcao):
    return sum(map(funcao,lista))

f1 = lambda x: x
f2 = lambda x: x**2
print(somatorio([2,4,6,8,12],f1))
print(somatorio([2,4,6,8,12],f2))

 
