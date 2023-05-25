class Atleta:
    def __init__(self, peso):
        self.aposentado = False
        self.peso = peso

    def aposentar(self):
        if not self.aposentado:
            print("Atleta aposentado com sucesso!")
            self.aposentado = True
        else:
            print("Este atleta já está aposentado!")

    def aquecer(self):
        print("Aquecendo...")


class Corredor(Atleta):
    def __init__(self, peso):
        super().__init__(peso)
        self.correndo = False

    def correr(self):
        if not self.correndo:
            print("O atleta começou a correr!")
            self.correndo = True
        else:
            print("O atleta já está correndo!")


class Nadador(Atleta):
    def __init__(self, peso):
        super().__init__(peso)
        self.nadando = False

    def nadar(self):
        if not self.nadando:
            print("O atleta começou a nadar!")
            self.nadando = True
        else:
            print("O atleta já está nadando!")


class Ciclista(Atleta):
    def __init__(self, peso):
        super().__init__(peso)
        self.pedalando = False

    def pedalar(self):
        if not self.pedalando:
            print("O atleta começou a pedalar!")
            self.pedalando = True
        else:
            print("O atleta já está pedalando!")


class TriAtleta(Corredor, Nadador, Ciclista):
    def __init__(self, peso):
        super().__init__(peso)


atleta = TriAtleta(25)
atleta.aquecer()
atleta.aposentar()
atleta.nadar()
atleta.correr()
atleta.pedalar()
atleta.aquecer()
atleta.aposentar()
atleta.nadar()
atleta.correr()
atleta.pedalar()
print(vars(atleta))
