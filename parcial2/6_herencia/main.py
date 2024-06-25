from coches import *

# print("Objeto 1")
coche1=Coches("Blanco", "BMW", "2022", 200, 250, 5)
coche1.getInfo()

# print("Objeto 2")
coche2=Coches("Azul", "Nissan", "2020", 180, 150, 6)
coche2.getInfo()

# print("Objeto 3")
camion1=Camiones("Negro", "Dina", "2020", 180, 300, 12, 8, 2500)
camion1.getInfo()

# print("Objeto 4")
camion2=Camionetas("Azul", "Star", "2019", 150, 300, 14, 6, 2000)
camion2.getInfo()

# print("Objeto 5")
camioneta1 = Camionetas("Amarillo", "Renault","2025", 240, 250, 8, "Delantera", True)
camioneta1.getInfo()

# print("Objeto 6")
camioneta2 = Camionetas("Blanca", "Nissan","2020", 100, 150, 6, "trasera", False)
camioneta2.getInfo()