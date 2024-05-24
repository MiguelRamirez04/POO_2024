def captura():
    lista_calificaciones_finales = []
    NCap = 0

    while True:
        nombre = input("Introduzca el nombre del alumno: ")
        carrera = input("Introduzca la carrera a la que pertenece: ")
        p1 = float(input("Calificación del parcial 1: "))
        p2 = float(input("Calificación del parcial 2: "))
        p3 = float(input("Calificación del parcial 3: "))
        promedio_parciales = (p1 + p2 + p3) / 3
        proyectoF = float(input("Calificación del proyecto final: "))

        final = (promedio_parciales + proyectoF) / 2
        print(f"\nNombre: {nombre}")
        print(f"Carrera: {carrera}")
        print(f"Promedio de los parciales: {promedio_parciales}")
        print(f"Calificación del proyecto final: {proyectoF}")
        print(f"Calificación final: {final}")

        if final < 80 or proyectoF < 50:
            print("Presenta examen extraordinario")
        else:
            print("Aprobado")

        lista_calificaciones_finales.append(final)
        NCap += 1

        pregunta = input("¿Deseas capturar otra captura? (SI/NO): ")
        if pregunta != 'SI':
            break

    if lista_calificaciones_finales:
        promedio_general = sum(lista_calificaciones_finales) / NCap
        print(f"\nPromedio general de las calificaciones finales: {promedio_general}")
    else:
        print("No se capturaron calificaciones.")

if True:
    captura()