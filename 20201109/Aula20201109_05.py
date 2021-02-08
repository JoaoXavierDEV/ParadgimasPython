class ExcecaoCustomizada(Exception):
    pass

def lancar_excecao():
    raise ExcecaoCustomizada

try:
    lancar_excecao()
except ExcecaoCustomizada as ex:
    print ("Excecao lançada")
    print (ex.__cause__)


