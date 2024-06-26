import math
class Figura:
    def __init__(self, x, y, visible):
        self.x = x
        self.y = y
        self.visible = visible

    def visibility(self, visible):
        self.visible = visible

    def mostrar(self):
        self.visible = True

    def ocultar(self):
        self.visible = False

    def set_move(self, move):
        self.moving = False

    def move(self, move):
        self.moving = move
        if self.moving == True:
            print("La figura se está moviendo o se está moviendo")
        else:
            print("La figura no se está moviendo o no se movió")
    
    def printed(self):
        print(f"X = {self.x}\nY = {self.y}\visible: {self.visible}")


class Rectangulo(Figura):
    def area(self):
        return self.x * self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_ancho(self):
        return self.x

    def get_alto(self):
        return self.y
    
    def printed(self):
        print(f"X = {self.x}\nY = {self.y}\visible: {self.visible}")

class Circulo(Figura):
    def __init__(self, radio):
        super().__init__(radio, radio)

    def area(self):
        return math.pi * (self.x ** 2)

    def get_radio(self):
        return self.x
    
    def printed(self):
        print(f"Radio = {self.x}\visible: {self.visible}")
