class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo
    def depositar(self,valor):
        self.saldo += valor
    def sacar(self,valor):
        if valor<=self.saldo:
            self.saldo -= valor
            return True
        else:
            return False
    def gerarextrato(self):
        print(f"numero: {self.numero} \ncpf: {self.cpf}\nsaldo: {self.saldo}")
    def transfereValor(self,contaDestino,valor):
        if self.saldo < valor:
            return ("Não existe saldo suficiente")
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            return("Transferencia Realizada")

c1 = Conta(1,123,"Joao",1000)
c1.depositar(300)
c1.sacar(250)
c2= Conta(3,345,"Maria",1000)
print(c1.transfereValor(c2,500))
c1.gerarextrato()
c2.gerarextrato()




