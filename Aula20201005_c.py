# Entre com os valores do produto e desconto e apresente 
# o valor final

valor = float(input("Digite o valor:"))
desconto = float(input("Desconto percentual:"))

valor_final = valor * ((100-desconto)/100)

print("Valor final: ",valor_final)

