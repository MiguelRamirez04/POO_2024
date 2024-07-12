import mysql.connector
# conectar con la BD en MySQL
conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bd_python'
)

if conexion.is_connected():
    print(f"se creó la conexion con la base de datos exitosamente...")