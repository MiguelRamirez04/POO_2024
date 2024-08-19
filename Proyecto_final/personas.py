from conexionBD import get_connection, get_cursor, mysql

class Empleados:
    def __init__(self, id, nombre, direccion, tel, correo, username, password, puesto, salario):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.tel = tel
        self.correo = correo
        self.username = username
        self.password = password
        self.puesto = puesto
        self.salario = salario

    def registrar_emp(self):
        conexion = get_connection()
        cursor = get_cursor(conexion)
        if not conexion or not cursor:
            return False
        
        try:
            query = """INSERT INTO personas (nombre, direccion, tel, correo, username, password, tipo)
                       VALUES (%s, %s, %s, %s, %s, %s, 'Empleado')"""
            values = (self.nombre, self.direccion, self.tel, self.correo, self.username, self.password)
            cursor.execute(query, values)
            conexion.commit()
            
            query = """INSERT INTO empleados (id, puesto, salario)
                       VALUES (LAST_INSERT_ID(), %s, %s)"""
            values = (self.puesto, self.salario)
            cursor.execute(query, values)
            conexion.commit()
            
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False
        finally:
            cursor.close()
            conexion.close()

    @staticmethod
    def iniciar_sesion(username, password):
        conexion = get_connection()
        cursor = get_cursor(conexion)
        if conexion and cursor:
            try:
                query = "SELECT * FROM personas WHERE username=%s AND password=%s AND tipo='Empleado'"
                cursor.execute(query, (username, password))
                empleado = cursor.fetchone()
                if empleado:
                    return empleado
                return None
            except mysql.connector.Error as err:
                print(f"Error al iniciar sesión: {err}")
                return None
            finally:
                cursor.close()
                conexion.close()

class Clientes:
    def __init__(self, id, nombre, direccion, tel, correo, username, password, tipo):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.tel = tel
        self.correo = correo
        self.username = username
        self.password = password
        self.tipo = tipo

    @classmethod
    def iniciar_sesion(cls, username, password):
        conexion = get_connection()
        cursor = get_cursor(conexion)
        if not conexion or not cursor:
            return None

        try:
            query = "SELECT * FROM personas WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            cliente_data = cursor.fetchone()
            if cliente_data:
                return cls(*cliente_data)
            else:
                return None
        except Exception as e:
            print(f"Error al iniciar sesión: {e}")
            return None
        finally:
            cursor.close()
            conexion.close()

    def registrar_cli(self):
        conexion = get_connection()
        cursor = get_cursor(conexion)
        if not conexion or not cursor:
            return False
        
        try:
            query = """INSERT INTO personas (nombre, direccion, tel, correo, username, password, tipo)
                       VALUES (%s, %s, %s, %s, %s, %s, 'Cliente')"""
            values = (self.nombre, self.direccion, self.tel, self.correo, self.username, self.password)
            cursor.execute(query, values)
            conexion.commit()
            
            query = "SELECT MAX(id) FROM personas WHERE tipo='Cliente'"
            cursor.execute(query)
            id_cliente = cursor.fetchone()[0]
            
            return Clientes(id_cliente, self.nombre, self.direccion, self.tel, self.correo, self.username, self.password, 'Cliente')
        except:
            print("Error al registrar cliente")
        finally:
            cursor.close()
            conexion.close()
