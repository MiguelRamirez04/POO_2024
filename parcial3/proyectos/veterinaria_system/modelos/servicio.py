class Servicio:
    @staticmethod
    def insertar_servicios_predefinidos(cursor):
        servicios = [
            ('Vacuna', 'Vacunación general para mascotas', 50.0),
            ('Consulta General', 'Revisión general del estado de salud del animal', 30.0),
            ('Lavado', 'Lavado y limpieza del animal', 20.0),
            ('Operación', 'Intervención quirúrgica', 150.0)
        ]
        cursor.executemany('''
        INSERT INTO servicios (nombre, descripcion, costo)
        VALUES (%s, %s, %s)
        ''', servicios)
