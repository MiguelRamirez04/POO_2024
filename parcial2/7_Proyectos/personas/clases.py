class Personas:
    def __init__(self, nombre, edad,tel):
        self.nombre = nombre
        self.edad = edad
        self.tel = tel

    def info_persona(self):
        print(f"Informacion de la persona: {self.getnombre}, {self.getedad}, {self.gettel}")

    def setnombre(self, nombre):
        self.nombre = nombre
    def getnombre(self):
        return self.nombre
    
    def setedad(self, edad):
        self.edad = edad
    def getedad(self):
        return self.edad
    
    def settel(self, tel):
        self.tel = tel
    def gettel(self):
        return self.tel


persona = Personas("Daniel", 20, 6181234567)
persona.info_persona()

class Estudiantes(Personas):
    def __init__(self, nombre, edad, tel, carrera, matricula):
        super().__init__(nombre, edad, tel)
        self.__carrera = carrera
        self.__matricula = matricula
    
    def info_persona(self):
        print(f"Informacion de la persona: {self.getnombre}, {self.getedad}, {self.gettel}, {self.getcarrera}, {self.getmatricula} ")

    def setmatricula(self, matricula):
        self.__matricula = matricula
    def getmatricula(self):
        return self.__matricula
    
    def setcarrera(self, carrera):
        self.__carrera = carrera
    def getcarrera(self):
        return self.__carrera
    
class Docentes(Personas):
    def __init__(self, nombre, edad, tel, modalidad, num_empleado):
        super().__init__(nombre, edad, tel)
        self._modalidad = modalidad
        self._num_empleado = num_empleado
    
    def info_persona(self):
        print(f"Informacion de la persona: {self.getnombre}, {self.getedad}, {self.gettel}, {self.getmodalidad}, {self.getnum_empleado} ")

    def setmodalidad(self, modalidad):
        self._modalidad = modalidad
    def getmodalidad(self):
        return self.modalidad
    
    def setnum_empleado(self, num_empleado):
        self._num_empleado = num_empleado
    def getnum_empleado(self):
        return self._num_empleado