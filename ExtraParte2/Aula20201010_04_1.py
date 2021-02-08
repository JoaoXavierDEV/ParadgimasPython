
valores = list()
for i in range(5):
    novo = int(input("valores[{:d}] = ".
                        format(i)))
    valores.append(novo)
print("Valores digitados:")
for i in range(5):
    print(valores[i])