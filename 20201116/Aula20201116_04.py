class Bola():
    def __init__(self,corX, raio, material = "borracha"):
        self.cor = corX
        self.raio = raio
        self.material = material
    
    def trocaCor(self,cor):
        self.cor = cor
    
    def mostraCor(self):
        print(self.cor)
        
    def mostraMaterial(self):
        print(self.material)

listaBolas = [Bola("azul",20,"plástico"), 
              Bola("marrom",30,"couro"),
              Bola("vermelha",25)]
listaBolas[0].trocaCor("verde")
for bola in listaBolas:
    bola.mostraCor()
    bola.mostraMaterial()

