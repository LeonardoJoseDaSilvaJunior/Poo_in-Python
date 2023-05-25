class Forma:
    def _init_(self, area, perimetro):
        self.area = area
        self.perimetro = perimetro


class Retangulo(Forma):

    def _init_(self, area, perimetro):
        super()._init_(area, perimetro)

    def calcularArea(self, base, altura):
        self.area = base * altura

    def calcularPerimetro(self, base, altura):
        self.perimetro = 2 * (base + altura)


class Triangulo(Forma):
    def _init_(self, area, perimetro):
        super()._init_(area, perimetro)

    def calcularArea(self, base, altura):
        self.area = (base * altura) / 2

    def calcularPerimetro(self, base, altura):
        self.perimetro = base + (2 * (base * 2 + altura) * 0.5)


retangulo = Retangulo()
triangulo = Triangulo()

print(isinstance(retangulo, Forma))
print(isinstance(triangulo, Forma))
retangulo.calcularArea(20, 40)
retangulo.calcularPerimetro(20, 40)
print(vars(retangulo))
triangulo = Triangulo()
triangulo.calcularArea(20, 40)
triangulo.calcularPerimetro(20, 40)
print(vars(triangulo))