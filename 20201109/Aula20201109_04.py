class Circulo():
    _total_circulos = 0
    def __init__(self,pontox, pontoy, raio):
        self.pontox = pontox
        self.pontoy = pontoy
        self.raio = raio
        type(self)._total_circulos +=1
    @classmethod
    def get_total_circulos(cls):
        return cls._total_circulos

c1 = Circulo(10,10,10)
c2 = Circulo(20,20,20)
print(Circulo.get_total_circulos())



