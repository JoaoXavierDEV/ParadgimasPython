

a = float(input("Primeiro numero:"))
b = float(input("Segundo numero:"))
c = float(input("Terceiro numero:"))

soma = a + b + c
maior = a
menor = a

if b<a and b<c:
    menor = b
elif c<b and c<a:
    menor = c

if b>a and b>c:
    maior = b
elif c>b and c>a:
    maior = c
    
meio = soma - maior - menor

print(menor,meio,maior)



