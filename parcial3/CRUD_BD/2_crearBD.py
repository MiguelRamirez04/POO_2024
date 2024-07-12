import mysql.connector

try:
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password=''
    )
except:
    print(f"Ocurrio un error con el servidor... Por favor verifica...")

else:
    # Crear un objeto de tipo cursor que permita ejecutar instrucciones SQL
    micursor = conexion.cursor()

    sql = "create database bd_python"
    # Ejecutar la consulta sql
    micursor.execute(sql)

    if micursor:
        print("Se creó la bd exitosamente")

    # mostrar las BD que existen en el SGBD MySQL
    micursor.execute("show database")

    for x in micursor:
        print(x)