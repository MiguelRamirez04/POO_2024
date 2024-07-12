import math
class Figura:
    def Calculo(self):
        print("El profe jugo con mis sentimientos")
        

class Rectangulo(Figura):
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def set_largo(self, largo):
        self.largo = largo

    def get_largo(self):
        return self.largo

    def set_ancho(self, ancho):
        self.ancho = ancho

    def get_ancho(self):
        return self.ancho

    def area(self):
        return self.largo * self.ancho

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def set_radio(self, radio):
        self.radio = radio

    def get_radio(self):
        return self.radio

    def area(self):
        return math.pi * (self.radio) ** 2

class Triangulo(Figura):
    def __init__(self, altura, ancho):
        self.altura = altura
        self.ancho = ancho

    def set_altura(self, altura):
        self.altura = altura

    def get_altura(self):
        return self.altura

    def set_ancho(self, ancho):
        self.ancho = ancho

    def get_ancho(self):
        return self.ancho

    def area(self):
        return (self.altura * self.ancho) / 2

figura1 = Rectangulo(8, 3)

