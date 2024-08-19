from conexionBD import *

class Cliente:
    def __init__(self, nif, nombre, direccion, ciudad, telefono):
        self.nif = nif
        self.nombre = nombre
        self.direccion = direccion
        self.ciudad = ciudad
        self.telefono = telefono

    def registrar_auto(self):
        try:
            cursor.execute(
                "INSERT INTO clientes (nif, nombre, direccion, ciudad, telefono) VALUES (%s, %s, %s, %s, %s)",
                (self.nif, self.nombre, self.direccion, self.ciudad, self.telefono)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al registrar cliente: {e}")
            return False

    @staticmethod
    def ver_autos():
        try:
            cursor.execute("SELECT * FROM clientes")
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al mostrar clientes: {e}")
            return None

    @staticmethod
    def actualizar_auto(nif, nombre, direccion, ciudad, telefono):
        try:
            cursor.execute(
                "UPDATE clientes SET nombre=%s, direccion=%s, ciudad=%s, telefono=%s WHERE nif=%s",
                (nombre, direccion, ciudad, telefono, nif)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar cliente: {e}")
            return False

    @staticmethod
    def eliminar_auto(nif):
        try:
            cursor.execute("DELETE FROM clientes WHERE nif=%s", (nif,))
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar cliente: {e}")
            return False

class Auto:
    def __init__(self, matricula, marca, modelo, color, nif):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.nif = nif

    def registrar(self):
        try:
            cursor.execute(
                "INSERT INTO autos (matricula, marca, modelo, color, nif) VALUES (%s, %s, %s, %s, %s)",
                (self.matricula, self.marca, self.modelo, self.color, self.nif)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al registrar auto: {e}")
            return False

    @staticmethod
    def mostrar():
        try:
            cursor.execute("SELECT * FROM autos")
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al mostrar autos: {e}")
            return None

    @staticmethod
    def actualizar(matricula, marca, modelo, color, nif):
        try:
            cursor.execute(
                "UPDATE autos SET marca=%s, modelo=%s, color=%s, nif=%s WHERE matricula=%s",
                (marca, modelo, color, nif, matricula)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar auto: {e}")
            return False

    @staticmethod
    def eliminar(matricula):
        try:
            cursor.execute("DELETE FROM autos WHERE matricula=%s", (matricula,))
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar auto: {e}")
            return False
