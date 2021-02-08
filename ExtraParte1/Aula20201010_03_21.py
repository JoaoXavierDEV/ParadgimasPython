
numero = int(input("Digite o valor:"))

# Só pode dividir por ele e por 1
# Não pode dividir entre 2 e numero-1

ePrimo = True
for i in range (2,numero):
    if numero % i == 0:
        ePrimo = False
        print("Divide por ",i)
        break

if ePrimo:
    print(numero," eh primo")
else:
    print(numero," nao eh primo")
            
