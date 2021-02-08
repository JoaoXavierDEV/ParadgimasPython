from threading import Thread

def funcao_a(nome):
    print(nome)

if __name__ == '__main__':
   t = Thread(target=funcao_a, args=("Minha Thread",))
   t.start()



