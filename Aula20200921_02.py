# -*- coding: utf-8 -*-

parar = False
while parar != True:
  digitado = input("Valor de A:") # Recebe Texto!!!
  a = int(digitado)
  if a%2==0 :
    print("A eh Par")
  else:
    print("A eh Impar")
  c = input("Digite x para finalizar")
  if c=="x":
    parar = True;


