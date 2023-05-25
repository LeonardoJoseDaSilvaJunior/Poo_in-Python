class Ingresso:
    def __init__(self, valor):
        self.valor = valor

    def imprimevalor(self):
        print(f"Valor do ingresso: {self.valor}")


class Vip(Ingresso):
    def __init__(self,valor):
        super().__init__(valor)

    def ingressoVip(self,adicional):
        self.valor += adicional
        return self.valor


b = Vip(40)
print(vars(b))
print(b.ingressoVip(25))
print(vars(b))