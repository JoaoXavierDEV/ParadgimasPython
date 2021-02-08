# CRIAR FUNCAO PARA RETORNAR O VALOR COM DESCONTO

def calcula_valor(valor, desconto):
    valor_final = valor * ((100-desconto)/100)
    return valor_final
    
valor = float(input("Digite o valor:"))
desconto = float(input("Desconto percentual:"))
print("Valor com desconto: ",calcula_valor(valor,desconto))

