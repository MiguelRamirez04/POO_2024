import mysql.connector

try:
    # conectar con la BD en MySQL
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='bd_python'
    )
except Exception as e:
    print(type(e))
    print(type(e).__name__)
    print(f"Ocurrio un error con el servidor... Por favor verifica...")

# Verificar si la conexion fue exitosa
if conexion.is_connected():
    print(f"se creó la conexion con la base de datos exitosamente...")
else:
    print(f"No fue posible conectar con la BD... Verifique...")