class Cliente:
    def __init__(self, cpf, nome, endereco):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco

class Conta:
    def __init__(self, clientes, numero, saldo):
        self.numero = numero
        self.clientes = clientes
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
        print(f"numero: {self.numero} \nsaldo: {self.saldo}")
    def transfereValor(self,contaDestino,valor):
        if self.saldo < valor:
            return ("Não existe saldo suficiente")
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            return("Transferencia Realizada")
    def exibirClientes(self):
        for cliente in self.clientes:
            print(cliente.nome)

cliente1 = Cliente(123, "Joao", "Rua 1")
cliente2 = Cliente(345, "Maria","Rua 2")

c1 = Conta([cliente1,cliente2],1,1000)
c1.depositar(300)
c1.sacar(250)
c2= Conta([cliente2],3,1000)
print(c1.transfereValor(c2,500))
c1.gerarextrato()
c2.gerarextrato()





