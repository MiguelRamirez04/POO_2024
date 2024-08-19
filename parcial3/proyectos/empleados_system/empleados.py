from conexionBD import *
import hashlib
import datetime

class Empleado:
    def __init__(self, nombre, apellidos, email, password, is_admin=False):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.contrasena = self.hash_password(password)
        self.is_admin = is_admin
    
    # Función para encriptar la contraseña
    def hash_password(self, contrasena):
        return hashlib.sha256(contrasena.encode()).hexdigest()
   
    def registrar(self):
        try:
            fecha = datetime.datetime.now()
            cursor.execute(
                "insert into empleados values (null, %s, %s, %s, %s, %s, %s)",
                (self.nombre, self.apellidos, self.email, self.contrasena, fecha, self.is_admin)
            )
            conexion.commit()
            return True
        except:
            return False    

    @staticmethod
    def iniciar_sesion(email, contrasena):
        contrasena = hashlib.sha256(contrasena.encode()).hexdigest()
        try:
            cursor.execute(
                "select * from empleados where email=%s and password=%s",
                (email, contrasena)
            )
            empleado = cursor.fetchone()
            if empleado:
                return empleado
            else:
                return None    
        except:    
            return None  
    
    @staticmethod
    def registrar_entrada(empleado_id):
        try:
            cursor.execute(
                "insert into registros (empleado_id, tipo, fecha_hora) values (%s, %s, NOW())",
                (empleado_id, 'entrada')
            )
            conexion.commit()
            return True
        except:
            return False
    
    @staticmethod
    def registrar_salida(empleado_id):
        try:
            cursor.execute(
                "insert into registros (empleado_id, tipo, fecha_hora) values (%s, %s, NOW())",
                (empleado_id, 'salida')
            )
            conexion.commit()
            return True
        except:
            return False
