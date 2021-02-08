class Circulo():
    total_circulos = 0
    def __init__(self,pontox, pontoy, raio):
        self.pontox = pontox
        self.pontoy = pontoy
        self.raio = raio
        Circulo.total_circulos +=1

c1 = Circulo(10,10,10)
c2 = Circulo(20,20,20)
print(Circulo.total_circulos)



