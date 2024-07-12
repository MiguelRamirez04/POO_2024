from conexionBD import *

micursor=conexion.cursor()

try:
    sql="select * from clientes"
    micursor.execute(sql)
    # Crear un objeto para enviar l resultado de la ejecucion del execute para posteriormente mostrar con ciclo
    resultado=micursor.fetchall()
except:
    print(f"Ocurrio un problema por favor verifica...")

else:
    for x in resultado:
        print(x)