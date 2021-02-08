valores = [10, 20, 30]

def altera_lista(lista):
   lista[2] = lista[2] + 10
   return lista
print("Nova lista", altera_lista(valores))
print("Nova lista", altera_lista(valores))

def altera_lista2(lista):
   nova_lista = list(lista)
   nova_lista[2] = nova_lista[2] + 10
   return nova_lista
print("Nova lista", altera_lista2(valores))
print("Nova lista", altera_lista2(valores))
print(valores)


def multiplicar_por(multiplicador):
   def multi(multiplicando):
      return multiplicando * multiplicador
   return multi
multiplicar_por_10 = multiplicar_por(10)
print(multiplicar_por_10(5))
print(multiplicar_por(3)(5))

f1 = lambda a,b : a*b
print(f1(3,6))
f2 = lambda x: x**2
print(sum(map(f2,[3,6,2,7,5,8])))

numeros=[1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x: x %2 != 0, numeros)))



