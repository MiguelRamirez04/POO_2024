from conexionBD import *

try:
    micursor=conexion.cursor()
    nombre=input("Cual es el nombre?")
    direccion=input("Cual es tu direccion?")
    tel =input("Cual es tu numero de telefono?")
    # sql= "INSERT INTO `clientes` (`id`, `nombre`, `direccion`, `tel`) VALUES (NULL, 'Daniel Contreras', 'Col. Centro', '6181234567');"
    sql= "INSERT INTO `clientes` (`id`, `nombre`, `direccion`, `tel`) VALUES (NULL, %s, %s, %s);"
    valores=(nombre, direccion, tel)
    micursor.execute(sql)
    

    # Sirve para finalizar la ejecucion de 
    conexion.commit()
except:
    print(f"Ocurrio un problema por favor verifica...")

else:
    print("Registro agregado exitosamente")