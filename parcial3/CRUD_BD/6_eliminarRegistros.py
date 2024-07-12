from conexionBD import *

try:
    micursor=conexion.cursor()

    sql="delete * from clientes where id=3"
    micursor.execute(sql)

    conexion.commit()

except:
    print(f"Ocurrio un problema por favor verifica...")

else:
    print("Registro eliminado exitosamente")