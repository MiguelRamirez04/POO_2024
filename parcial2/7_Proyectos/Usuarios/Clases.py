class Usuario:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def get_info(self):
        print(f"Nombre: {self.nombre}\n Dirección: {self.direccion}\n Teléfono: {self.telefono}")
    
    def set_info(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

class Cliente(Usuario):
    def __init__(self, nombre, direccion, telefono, num_cliente):
        super().__init__(nombre, direccion, telefono)
        self.num_cliente = num_cliente

    def get_info(self):
        print(f"{super().get_info()}\n Número de cliente: {self.num_cliente}")
    
    def set_info(self, nombre, direccion, telefono, num_cliente):
        super().set_info(nombre, direccion, telefono)
        self.num_cliente = num_cliente
    
class Empleado(Usuario):
    def __init__(self, nombre, direccion, telefono, salario, num_empleado, tipo):
        super().__init__(nombre, direccion, telefono)
        self.salario = salario
        self.num_empleado = num_empleado
        self.tipo = tipo

    def get_info(self):
        print(f"{super().get_info()}\n Salario: ${self.salario}\n Número de empleado: {self.num_empleado}\n Tipo: {self.tipo}")
    
    def set_info(self, nombre, direccion, telefono, salario, num_empleado, tipo):
        super().set_info(nombre, direccion, telefono)
        self.salario = salario
        self.num_empleado = num_empleado
        self.tipo = tipo