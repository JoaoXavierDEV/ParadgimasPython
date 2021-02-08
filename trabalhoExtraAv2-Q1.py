class Pessoa():
    def __init__(self, nome, cpf, estadoCivil, dataNasc):
        self.nome = nome
        self.cpf = cpf
        self.estadoCivil = estadoCivil
        self.dataNasc = dataNasc
    def dadosPessoa(self):
        print("Nome: {} \nData de Nascimento: {}".format(self.nome, self.dataNasc))

class Aluno(Pessoa):
    def __init__(self, matricula):
        self.matricula = matricula

class Professor(Pessoa):
    def __init__(self, salario):
        self.salario = salario

class Funcionario(Pessoa):
    def __init__(self, salario, cargo):
        self.salario = salario
        self.cargo = cargo

pessoa01 = Pessoa("João Fernando", 11122233345, "Solteiro", "31011995")
aluno01 = Aluno(65465456456645)
#pessoa01.dadosPessoa()
aluno01.nome = "fulano"
print("Nome do aluno {} \nMatricula: {}".format(aluno01.nome, aluno01.matricula))