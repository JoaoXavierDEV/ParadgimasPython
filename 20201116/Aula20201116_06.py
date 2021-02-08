class Pessoa():
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def envelhecer(self):
        self.idade += 1
        if(self.idade<=21):
            self.crescer()
    
    def engordar(self, quilos):
        self.peso += quilos
    
    def emagrecer(self, quilos):
        self.peso -= quilos
        
    def crescer(self):
        self.altura += 0.005
    
    def exibir(self):
        print("Nome: {} \nPeso: {:.2f} \nAltura: {:.2f} \nIdade: {}".
              format(self.nome,self.peso,self.altura,self.idade))

p1 = Pessoa("Ana",16,50.0,1.5)
p1.exibir()
p1.engordar(30)
for i in range(4):
    p1.envelhecer()
p1.exibir()