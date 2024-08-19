from conexionBD import get_connection, get_cursor, mysql

class Prestamo:
    def __init__(self, id, material_id, fecha_prestamo, fecha_entrega, cliente_id):
        self.id = id
        self.material_id = material_id
        self.fecha_prestamo = fecha_prestamo
        self.fecha_entrega = fecha_entrega
        self.cliente_id = cliente_id

    def pedir_prestado(self):
        conexion = get_connection()
        cursor = get_cursor(conexion)
        try:
            cursor.execute("""
                INSERT INTO prestamos (id_material, fecha_prestamo, fecha_entrega, cliente_id, empleado_id)
                VALUES (%s, %s, %s, %s, NULL)
            """, (self.material_id, self.fecha_prestamo, self.fecha_entrega, self.cliente_id))
            conexion.commit()
            return True
        
        except Exception as e:
            print(f"Error al registrar el préstamo: {e}")
            conexion.rollback()
            return False
        finally:
            cursor.close()
            conexion.close()