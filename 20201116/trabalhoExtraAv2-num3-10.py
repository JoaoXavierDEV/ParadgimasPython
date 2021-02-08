class BombaDeCombustivel():
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel ):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        litro =   valor / self.valorLitro
        resto = litro / self.valorLitro
        self.getBomba(litro)

    def abastercerPorLitro(self, litro):
        total = self.valorLitro * litro
        #self.quantidadeCombustivel = int(self.quantidadeCombustivel) - int(litro)
        #print("quantidadeCombustivel {} litro {} ".format(self.quantidadeCombustivel, litro))
        self.getBomba(litro)
        

    def alterarValor(self, valorLitro):
        self.valorLitro = valorLitro


    def alterarCombustivel(self, tipoCombustivel):
        self.tipoCombustivel = tipoCombustivel

    def alterarQuantidadeCombustivel(self, quantidadeCombustivel):
        self.quantidadeCombustivel = quantidadeCombustivel

    def getBomba(self, litro):
        self.quantidadeCombustivel = int(self.quantidadeCombustivel) - int(litro)
        print("Quantidade de litros restantes: {}\n".format(self.quantidadeCombustivel))

abastecer = BombaDeCombustivel("Gasolina", 2.00 , 1000)
#abastecer.abastercerPorLitro(20)
abastecer.abastecerPorValor(20)
#abastecer.getBomba()

