class Conta():
    def __init__(self, nome, numero, saldo, limite):
        self.nome = nome
        self.numero = numero
        self.saldo = saldo
        self.limite = limite

    def criarConta(self):
        print(self.nome)
    
    def mostrarSaldoLimite(self):
        print("Seu limite é de R$ {}".format(self.limite))

conta01 = Conta("João", 21980827649, 1900, 5000);
conta01.mostrarSaldoLimite()


