from threading import Thread, Lock

contador = 0
lock = Lock()

def funcao_a(indice):
    global contador
    for i in range(100000):
        lock.acquire()
        contador += 1
        lock.release()
    print("Termino thread ", indice)

tarefas = []
print("Antes de aguardar o termino!", contador)
for indice in range(10):
    tarefa = Thread(target=funcao_a, args=(indice,))
    tarefas.append(tarefa)
    tarefa.start()
for tarefa in tarefas:
    tarefa.join()
print("Após aguardar o termino!", contador)

