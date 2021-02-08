
x = lambda: 2+2

y = lambda valor1: valor1

# print(x())

# -------------------------------------

class TV():
    def __init__(self, ligada , canal, volume):
        self.ligada = ligada
        self.canal = canal
        self.volume = volume

    def mudarVolume(self):
        volume = input("VOLUME  0 - 10\n")
        if (int(volume) >= 0 and int(volume) <= 10):
            self.volume = volume
            print("O volume foi alterado para {}".format(self.volume))
        elif (int(volume) > 10):
            print("Insira um valor entre 0 e 10")
    
        
    
    def mudarCanal(self, canal):
        canal = input("INSIRA UM CANAL 1 -- 99 \n")
        if (int(canal) >= 1 and int(canal) <= 99):
            self.canal = canal
        elif (int(canal) > 99):
            print("Digite um canal válido")

    def infoTV(self):
        if(self.ligada):
            print("A tv está ligada \nCanal: {} \nVolume: {}".format(self.canal, self.volume))
        else:
            print("A tv está desligada")

tv = TV(True, 0, 0)
tv.mudarVolume()
tv.infoTV()
