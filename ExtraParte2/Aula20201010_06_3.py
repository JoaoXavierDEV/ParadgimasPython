nome = input("Seu nome:")
for i in range(len(nome)):
    print(nome[i])

#exercicio 4
print()    
for i in range(len(nome)):
    print(nome[0:i+1])
    
#exercicio 5
print()    
for i in range(len(nome)):
    print(nome[0:len(nome)-i])
