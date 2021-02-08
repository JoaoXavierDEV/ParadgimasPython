
tamanho = 20

valores = []
pares = []
impares = []

for i in range(tamanho):
    valores.append(int(input("Valor:")))
    if valores[i] % 2 == 0:
        pares.append(valores[i])
    else:
        impares.append(valores[i])

print("Numeros digitados")
for i in range(tamanho):
    print(valores[i])
    
print("Pares")
for i in range(len(pares)):
    print(pares[i])
    
print("Impares")
for i in range(len(impares)):
    print(impares[i])


