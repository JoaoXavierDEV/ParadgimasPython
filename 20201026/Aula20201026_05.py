class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo
    def depositar(self,valor):
        self.saldo += valor
    def sacar(self,valor):
        self.saldo -= valor
    def gerarextrato(self):
        print(f"numero: {self.numero} \ncpf: {self.cpf}\nsaldo: {self.saldo}")

c1 = Conta(1,1,"Joao",1000)
c1.depositar(300)
c1.sacar(250)
c1.gerarextrato()


