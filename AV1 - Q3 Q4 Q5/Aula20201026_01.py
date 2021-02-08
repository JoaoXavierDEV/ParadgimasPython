valor = int(input("numero:"))
maior = menor = valor
while valor!=0 :
    valor = int(input("numero:"))
    if valor!=0 and valor < menor :
        menor = valor
    if valor!=0 and valor > maior :
        maior = valor
print(maior/menor)
        
        

