valores = []
tamanho = 10
for i in range(tamanho):
    novo = int(input("valores[{:d}] = ".
                        format(i)))
    valores.append(novo)

#soma dos quadrados
soma = 0
for i in range(tamanho):
    soma += valores[i] ** 2
print("A soma dos quadrados deu",soma)
    
