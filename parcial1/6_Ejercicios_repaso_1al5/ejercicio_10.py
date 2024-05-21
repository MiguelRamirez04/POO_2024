# 10.- Crear un programa que solicite la calificacion de 15 alumnos e imprimir en pantalla cuantos aproboron y cuantos no aprobaron

aprobados = 0
reprobados = 0

for i in range(1,16):
    calif = int(input(f"Ingrese la calificacion del alumno {i}: "))

    if calif >= 8:
        aprobados += 1
        print(f"El alumno {i} aprobo")
        i += 1
    else:
        reprobados += 1
        print(f"El alumno {i} reprobo")
        i += 1

print(f"Aprobados: {aprobados}")
print(f"Reprobados: {reprobados}")