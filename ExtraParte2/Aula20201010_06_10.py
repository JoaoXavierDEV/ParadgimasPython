proprios = ("zero","um","dois","tres","quatro","cinco",
            "seis","sete","oito","nove","dez","onze",
            "doze","treze","quatorze","quinze",
            "dezesseis","dezessete","dezoito","dezenove")
dezenas = ("vinte","trinta","quarenta","cinquenta",
           "sessenta","setenta","oitenta","noventa")

def num_extenso(n):
    if n<0 or n>99:
        raise Exception("Valor invalido")
    if n<20:
        return proprios[n]
    else:
        texto = dezenas[(n//10) - 2]
        if n%10 > 0:
            texto = texto + " e " + proprios[n%10]
        return texto

numero = int(input("Valor:"))
print(num_extenso(numero))