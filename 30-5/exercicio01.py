class Atleta():
    def __init__(self, peso):
        self.aposentado=False
        self.peso=peso
        self.aquecido=False

    def aposentar(self):
        self.aposentado = True
        print(f'ATLETA APOSENTADO')

    def aquecer (self):
        if not self.aquecido:
            print(f'ESTÁ SE AQUECENDO')
            self.aquecido=True
        else:
            print(f'JÁ AQUECEU')

class Corredor(Atleta):
    def __init__ (self, peso):
        super().__init__(peso)
        self.correndo=False

    def correr(self):
        if self.aquecido==True:
            if not self.correndo:
                print(f'COMEÇOU A CORRER')
            else:
                print("JÁ ESTÁ CORRENDO")
        else:
            print("PRECISA AQUECER ANTES")

    def parar_de_correr(self):
        if self.correndo == True:
           print(f'PAROU DE CORRER')
           self.correndo = False
        else:
            print("NÃO ESTÁ CORRENDO")

class Nadador(Atleta):
    def __init__(self, peso):
        super().__init__(peso)
        self.nadando = False

    def nadar(self):
        if self.aquecido == True:
            if not self.correndo:
                print(f'COMEÇOU A NADAR')
            else:
                print("JÁ ESTÁ NADANDO")
        else:
            print("PRECISA AQUECER ANTES")

    def parar_de_nadar(self):
        if self.nadando == True:
            print(f'PAROU DE NADAR')
            self.nadando = False
        else:
            print("NÃO ESTÁ NADANDO")
class Ciclista(Atleta):
    def __init__(self,peso):
        super().__init__(peso)
        self.pedalando = False

    def pedalar(self):
        if self.aquecido == True:
            if not self.pedalando:
                print(f'COMEÇOU A PEDALAR')
            else:
                print("JÁ ESTÁ PEDALANDO")
        else:
            print("PRECISA AQUECER ANTES")

    def parar_de_pedalar(self):
        if self.pedalando == True:
            print(f'PAROU DE PEDALAR')
            self.pedalando = False
        else:
            print("NÃO ESTÁ PEDALANDO")
class Triatleta(Ciclista,Corredor,Nadador):
    def __init__(self,peso):
        super().__init__(peso)

    def correr(self):
        if self.nadando == True or self.pedalando == True:
            print("O ATLETA NÃO PODE PRATICAR DUAS MODALIDADES AO MESMO TEMPO ")
        elif self.correndo == True :
            print("O ATLETA JÁ ESTÁ CORRENDO ")
        else:
            print("COMEÇOU A CORRER")
            self.correndo = True

    def nadar(self):
        if self.correndo == True or self.pedalando == True:
            print("O ATLETA NÃO PODE PRATICAR DUAS MODALIDADES AO MESMO TEMPO ")
        elif self.nadando == True:
            print("O ATLETA JÁ ESTÁ NADANDO ")
        else:
            print("COMEÇOU A NADAR")
            self.nadando = True

    def pedalar(self):
        if self.correndo == True or self.nadando == True:
            print("O ATLETA NÃO PODE PRATICAR DUAS MODALIDADES AO MESMO TEMPO ")
        elif self.pedalando == True:
            print("O ATLETA JÁ ESTÁ PEDALANDO ")
        else:
            print("COMEÇOU A PEDALAR")
            self.pedalando = True

