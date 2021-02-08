import datetime as dt

class Cliente:
    def __init__(self, cpf, nome, endereco):
        self.__cpf = cpf
        self.nome = nome
        self.__endereco = endereco
    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self,value):
        self.__cpf = value

class Extrato:
    def __init__(self):
        self.transacoes = []
    def extrato(self, numeroconta):
        print(f"Extrato : {numeroconta} \n")
        for p in self.transacoes:
            print(f"{p[0]:15s} {p[1]:10.2f} {p[2]:10s} {p[3].strftime('%d/%b/%y')}")

class Conta:
    def __init__(self, clientes, numero, saldo):
        self.numero = numero
        self.clientes = clientes
        self.saldo = saldo
        self.abertura = dt.datetime.today()
        self.extrato = Extrato()
    def depositar(self,valor):
        self.saldo += valor
        self.extrato.transacoes.append(["DEPOSITO", valor, "Data",dt.datetime.today ()])
    def sacar(self,valor):
        if valor<=self.saldo:
            self.saldo -= valor
            self.extrato.transacoes.append(["SAQUE", valor, "Data", dt.datetime.today()])
            return True
        else:
            return False
    def gerarsaldo(self):
        print(f"numero: {self.numero} \nsaldo: {self.saldo}")
    def transfereValor(self,contaDestino,valor):
        if self.saldo < valor:
            return ("Não existe saldo suficiente")
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(["TRANSFERENCIA", valor, "Data", dt.datetime.today()])
            return("Transferencia Realizada")
    def exibirClientes(self):
        for cliente in self.clientes:
            print(cliente.nome)
    def gerarExtrato(self):
        self.extrato.extrato(self.numero)







