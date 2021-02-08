
def reverso(n):
    soma = 0
    while n>10:
        soma = soma * 10 + (n%10)
        n = n // 10   # divisão inteira
        #print(soma,n)
    else:
        soma = soma * 10 + n
        #print(soma,n)
    return soma

def reverso2(n):
    return int(str(n)[::-1])

print(reverso(123456789))
print(reverso2(123456789))

        



