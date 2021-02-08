

qtd = 5
soma = 0

for i in range(qtd):
    valor = float(input(
            "Valor {:d}:".format(i+1)))
    soma += valor

media = soma / qtd
print("Soma: {:.2f}  Media:{:.2f}".
      format(soma,media))