
salario_atual = float(input("Salario atual:"))

percentual = 5
if salario_atual <= 280:
    percentual = 20
elif salario_atual > 280 and salario_atual <= 700:
    percentual = 15
elif salario_atual > 700 and salario_atual < 1500:
    percentual = 10
    
valor_aumento = salario_atual * percentual / 100
novo_salario = salario_atual + valor_aumento

print("Com salario inicial de",salario_atual,
      "foi aplicado o percetual de",percentual,
      "obtendo o valor adicional de",valor_aumento,
      "e gerando o novo salario de",novo_salario)
    


