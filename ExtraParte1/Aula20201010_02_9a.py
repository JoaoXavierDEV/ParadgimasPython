
# Bubble Sort

valores = [0,0,0]
valores[0] = float(input("Primeiro numero:"))
valores[1] = float(input("Segundo numero:"))
valores[2] = float(input("Terceiro numero:"))

acabou = False
while not acabou:
    acabou = True
    for i in range(2):
        if valores[i] > valores[i+1]:
            aux = valores[i]
            valores[i] = valores[i+1]
            valores[i+1] = aux
            acabou = False

for i in range(3):
    print(valores[i])

