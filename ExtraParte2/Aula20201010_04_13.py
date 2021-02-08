
meses = ("Janeiro","Fevereiro","Março","Abril",
         "Maio","Junho","Julho","Agosto",
         "Setembro","Outubro","Novembro","Dezembro")

temperaturas = []
num_meses = len(meses)

soma = 0

for i in range(num_meses):
    mes_atual = meses[i]
    temperaturas.append(float(input(
            "Temperatura média de {:s}:".format(mes_atual))))
    soma += temperaturas[i]
    
media_anual = soma / num_meses

print("\nTempteratura Média Anual: {:5.2f}".format(media_anual))

for i in range(num_meses):
    if temperaturas[i] > media_anual:
        print("Em {:s} tivemos {:5.2f} graus".
              format(meses[i],temperaturas[i]))

    


