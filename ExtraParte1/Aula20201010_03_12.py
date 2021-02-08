valido = False
while not valido:
    valor = int(input("Digite o valor:"))
    valido = valor >= 1 and valor <= 10
    if not valido:
        print("Digite um valor entre 1 e 10")
    
print("Tabuada de",valor,":")
# range(1,11) - exclui o 11 - será de 1 a 10
for i in range(1,11):
    resultado = i * valor
    print("{:2d} x {:2d} = {:2d}".
          format(valor,i,resultado))
    

