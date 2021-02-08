nome = input("Seu nome:")
print() 
tamanho = len(nome)   
for i in range(tamanho):
    print(nome[0:tamanho-i])
