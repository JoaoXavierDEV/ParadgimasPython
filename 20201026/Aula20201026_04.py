from tkinter import *

def funcClicar():
    print("Botão pressionado")

janelaPrincipal = Tk()
texto = Label(master = janelaPrincipal, text = "Minha janela exibida")
#texto.place(x = 50, y = 100)
texto.pack()
botao = Button(master = janelaPrincipal, text = 'Clique', command = funcClicar)
botao.pack()

janelaPrincipal.mainloop()
