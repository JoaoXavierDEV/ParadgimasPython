from Aula20201109_01 import Cliente
from Aula20201109_01 import Conta


cliente1 = Cliente(123, "Joao", "Rua 1")
cliente2 = Cliente(345, "Maria","Rua 2")

c1 = Conta([cliente1,cliente2],1,1000)
c1.depositar(300)
c1.sacar(250)
c2= Conta([cliente2],3,1000)
print(c1.transfereValor(c2,500))
c1.gerarExtrato()
c2.gerarExtrato()
c1.exibirClientes()