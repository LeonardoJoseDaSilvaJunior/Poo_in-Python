class Conta:

    def __init__(self,nome,numero_conta):
        self.nome = nome
        self.numero_conta = numero_conta
        self.saldo = 0
        self.status = False
        self.limite = 0
        self.limite_inicial = 0
        self.status_limite = False

    def depositar (self,valor):
        if self.limite_inicial  == self.limite:
            if valor > 0 and self.status == True:
                self.saldo += valor
                print("Deposito feito com sucesso! ")
            else:
                print(f"{valor} é um valor inválido. Deposite um valor válido! Acima de 0(zero)! ")
        elif self.status == False:
            print("Esta conta está inativa !")
        else:
            if self.limite_inicial + valor >= self.limite :
                self.saldo += ((self.limite+valor) - self.limite_inicial)
                self.limite = (self.limite_inicial)
            else:
                self.limite += valor
    def sacar (self,valor):
        if (self.saldo >= valor and self.status != False) and valor > 0:
            self.saldo-=valor
        elif self.status == False:
            print("Esta conta está inativa !")
        elif (valor <= (self.limite + self.saldo)) and self.status_limite == True:
            self.limite -= (valor - self.saldo)
            self.saldo = 0
            print("Você está usando o seu limite especial! ")
        elif valor == 0:
            print("Insira um valor maior que 0 (zero)! ")
        else:
            print("Saldo insuficiente !")
    def ativar(self):
        if self.status == True:
            print("Está conta já esta ativa! ")
        else:
            self.status = True
            print("Conta ativada com sucesso! ")
    def desativar (self):
        if self.status == True and self.saldo == 0:
            self.status =  False
            print("Conta desativada com sucesso! ")
        elif self.saldo > 0:
            print("para desativar a conta é necessário que o seu saldo seja igual a 0 (zero)")
        else:
            print("Esta conta já foi desativada! ")
    def verificar_saldo(self):
        if self.status == True:

            print(f"Seu saldo atual é : {self.saldo}")
            print(f"Seu saldo do limite especial atual é : {self.limite}")

        else:
            print("Esta conta está inativa")
    def ativar_limite(self,valor):

        if valor > 0 and self.status == True:
            self.status_limite = True
            self.limite = valor
            self.limite_inicial = valor
        elif valor == 0:
            print("Insira um valor maior que 0 (zero)")

        elif self.status == False:
            print("Esta conta está inativa: ")

        else:
            print("Insira um valor acima de 0 (zero)")

primeria = Conta("leonardo",5)
print("DADOS DA CONTA: ")
print()
print(vars(primeria))


print("TESTE - SACAR")
print()
primeria.ativar()
print(vars(primeria))
primeria.depositar(500)
print(vars(primeria))
primeria.sacar(600)
primeria.ativar_limite(100)
print(vars(primeria))
primeria.sacar(600)
print(vars(primeria))
