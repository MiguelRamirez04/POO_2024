calculos = 0
Acceso = input("Quieres calcular tu IMC?(S/N)")

def calcular_imc(peso, altura):
    return peso / (altura ** 2)
    calculos += 1
while True:
    Acceso = input("Quieres calcular tu IMC?(S/N)")
    if Acceso == "S":
        peso = float(input("Introduce tu peso en kg: "))
        altura = float(input("Introduce tu altura en metros (Ej. 1.75): "))
        imc = calcular_imc(peso, altura)

        if imc < 18.5:
            print(f"Tu IMC es: {imc}, estas bajo de peso")

        elif imc >= 18.5 and imc <= 24.9:
            print(f"Tu IMC es: {imc}, estas normal")

        elif imc >= 25 and imc <= 29.9:
            print(f"Tu IMC es: {imc}, estas con sobrepeso")

        elif imc >= 30:
            print(f"Tu IMC es: {imc}, estas con obesidad")

        print(f"El cálculo del IMC se ha realizado {calculos} vez/veces.")
    elif Acceso == "N":
        print("Gracias por usar el calculador de IMC.")
        print(f"se han realizado {calculos} calculos.")
        break
    elif Acceso == "N" and calculos == 0:
        print("No se han realizado calculos")
    else:
        print("Entrada no válida. Por favor, introduce 'S' para sí o 'N' para no.")