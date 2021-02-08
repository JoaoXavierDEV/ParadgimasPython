
valido = False
while not valido:
    valor = float(input("Digite o valor:"))
    valido = valor >= 0 and valor <= 10
    if not valido:
        print("Digite um valor entre 0 e 10")
    
print("A nota digitada foi",valor)
