from coches import *

# print("Objeto 1")
coche1=Coches("Blanco", "VMW", "2022", 200, 250, 5)
# coche1.getInfo()

# print("Objeto 2")
# coche2=Coches("Azul", "Nissan", "2020", 180, 150, 6)
# coche2.getInfo()

print(coche1.publico_atributo)

# print(coche1.__privado_atributo) no esta permitido
print(coche1.getPrivadoAtributo())

# coche1.getMetodoPrivado() no esta permitido
coche1.__getMetodoPrivado()
