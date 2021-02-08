class Bichinho():
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
    
    def getNome(self):
        print(self.nome)

    def getFome(self):
        print(self.fome)

    def getSaude(self):
        print(self.saude)

    def getIdade(self):
        print(self.idade)

    def setNome(self, nome):
        self.nome = nome
        print(self.nome)

    def setFome(self, fome):
        self.fome = fome
        print(self.fome)

    def setSaude(self, saude):
        self.saude = saude
        print(self.saude)

    def setIdade(self, idade):
        self.idade = idade
        print(self.idade)

    def getHumor(self):
        humor =  (int(self.fome) + int(self.saude)) / 2
        if ( humor <= 5 ):
            print("mal humor")
        elif ( humor > 5 and humor < 7 ):
            print("bom humor")
        elif ( humor >= 7):
            print("excelente humor")
        print(humor)




bichinho = Bichinho("Jubileu", 5, 9, "500");
bichinho.getHumor()

