lista = []
while len(lista) < 120:
    lista.append(input("Ingrese un valor: "))
    print(len(lista))
    if len(lista) == 120:
        print("Espacio lleno")
        print(lista)
        break
print(lista)


for i in range(120):
    lista.append(input("Ingrese un valor: "))
    print(len(lista))
    if len(lista) == 120:
        print(lista)
        print("Espacio lleno")
