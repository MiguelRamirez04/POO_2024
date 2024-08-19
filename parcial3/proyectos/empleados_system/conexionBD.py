import mysql.connector

try:
    # Conectar con la BD en MySQL
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='bd_empleados'
    )
    # Crear un objeto de tipo cursor que tenga un parámetro que permita reutilizar el objeto 
    cursor = conexion.cursor(buffered=True)
except:
    print(f"Ocurrió un error con el Sistema, por favor verifique ...")
