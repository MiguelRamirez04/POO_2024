# crear un programa que calcule y obtenga el total a pagar por un producto determinado.
# Se deberá de solicitar el nombre o descripcion del producto, codigo, cantidad y precio unitario.
# el total a pagar incluye el IVA y el descuento
# Si se compran de 1 a 5 productos se otorga el 10% de descuento, si se compran de 6 a 10 el 15% y si se compran mas de 10 el 20%

producto = input("Ingrese el nombre del producto: ")
id = int(input("Ingrese el codigo del producto: "))
cant = int(input("Ingrese la cantidad del producto: "))
precio = float(input("Ingrese el precio del producto: "))

Subtotal = cant * precio
IVA = Subtotal * 0.16
totalcrudo = Subtotal + IVA

if cant >= 1 and cant <= 5:
    descuento = totalcrudo * 0.1
    total = totalcrudo - descuento

elif cant >= 6 and cant <= 10:
    descuento = totalcrudo * 0.15
    total = totalcrudo - descuento

elif cant > 10:
    descuento = totalcrudo * 0.2
    total = totalcrudo - descuento

print(f"Ticket de pago\n {id} {producto}\n Cantidad: {cant}\n Subtotal: {Subtotal}\n IVA (16%): {IVA}\n Precio en bruto: {totalcrudo}\n Descuento: {descuento} \n Total con descuento: {total}")