import mysql.connector

try:
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='agencia_autos_datos'
    )
    cursor = conexion.cursor(buffered=True)
    print("Conexión establecida con la base de datos")
except:
    print("Ocurrió un error con el sistema, por favor verifique...")

