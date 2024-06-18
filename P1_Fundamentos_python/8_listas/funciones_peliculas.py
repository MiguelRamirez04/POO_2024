def agregar_pelicula(peliculas):
    nombre = input("Ingrese el nombre de la película: ")
    peliculas.append(nombre)
    print(f"Película '{nombre}' agregada exitosamente.")

def remover_pelicula(peliculas):
    nombre = input("Ingrese el nombre de la película a remover: ")
    if nombre in peliculas:
        peliculas.remove(nombre)
        print(f"Película '{nombre}' removida exitosamente.")
    else:
        print(f"La película '{nombre}' no se encuentra en la lista.")

def consultar_peliculas(peliculas):
    if peliculas:
        print("\n--- Lista de Películas ---")
        for idx, pelicula in enumerate(peliculas, start=1):
            print(f"{idx}. {pelicula}")
    else:
        print("No hay películas en la lista.")