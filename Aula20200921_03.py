# -*- coding: utf-8 -*-

def testeParImpar():
  digitado = input("Valor de A:") # Recebe Texto!!!
  a = int(digitado)
  if a%2==0 :
    print("A eh Par")
  else:
    print("A eh Impar")

parar = False
while parar != True:
  testeParImpar()
  c = input("Digite x para finalizar")
  if c=="x":
    parar = True;


