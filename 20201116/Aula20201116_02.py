import random
lista = []
for i in range(100):
    lista.append(random.randint(1,1000))
listaPares = list(filter(lambda x: x%2==0, lista))
print(listaPares)
print(len(listaPares))