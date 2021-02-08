# -*- coding: utf-8 -*-

import numpy as np

def media(entrada,tamanho):
  soma = 0.0
  for i in range(tamanho):
    soma += entrada[i]
  return soma / tamanho

def principal():
  tamanho = 5
  valores = np.zeros(tamanho)
  for i in range(tamanho):
    print("Posicao ",i)
    valores[i] = float(input("Valor :"))
  print(media(valores,tamanho))

principal()
