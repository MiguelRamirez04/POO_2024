lista =[]
if len(lista) == 0:
    print("la lista esta vacia, llenarla con palabras o frases")
    while True:
        palabra = input("Ingrese una palabra o frase(Esribir fin para dejar de agregar palabras): ").upper()
        lista.append(palabra)
        if palabra == "FIN":
            break