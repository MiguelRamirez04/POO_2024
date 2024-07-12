from conexionBD import *

try:
    micursor=conexion.cursor()

    sql="update clientes set direccion='Colonia Vizcaya' where id=1"
    micursor.execute(sql)

    conexion.commit()

except:
    print(f"Ocurrio un problema por favor verifica...")

else:
    print("Registro actualizado exitosamente")