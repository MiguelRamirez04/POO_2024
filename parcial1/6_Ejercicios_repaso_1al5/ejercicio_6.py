# 6.- Mostrar todas las tablas del 1 al 10. Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10

for x in range(1,11):
    print(f"Tabla del {x}")
    for y in range(1,11):
        print(f"{x} x {y} = {x*y}")