class Funcionario:

    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    def autentica(self, senha):
        if self._senha == senha:
            print("acesso permitido")
            return True
        else:
            print("acesso negado")
            return False

class Gerente (Funcionario):

    def __init__(self,senha,qtd_Funcionario,nome,cpf,salario):
        super().__init__(nome,cpf,salario)
        self.senha = senha
        self.qtd_Funcionario = qtd_Funcionario


