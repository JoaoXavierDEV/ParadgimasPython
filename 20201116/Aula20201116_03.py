def calcFibo(n):
    if n<2:
        return n
    else:
        return calcFibo(n-1) + calcFibo(n-2)

def fibo(n):
    lista = []
    for i in range(n+1):
        lista.append(calcFibo(i))
    return lista

print(fibo(13))
    

