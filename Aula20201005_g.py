lista = ["UM","DOIS","TRES"]
try:
  num = eval(input("Entre com um número: "))
  print(lista[num])
except ValueError:
  print("Mensagem 1")
except IndexError:
  print("Mensagem 2")
except:
  print("Mensagem 3")

