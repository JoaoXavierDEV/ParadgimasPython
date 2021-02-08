class Quadrado():
    def __init__(self,lado):
        self.lado = lado
        
    def mudarLado(self,ladoAlterado):
        self.lado = ladoAlterado
    
    def obterLado(self):
        return self.lado
    
    def calcArea(self):
        print("Area: "+str(self.lado**2))

q1 = Quadrado(10)
q2 = Quadrado(20)
q2.mudarLado(15)
q1.calcArea()
q2.calcArea()
