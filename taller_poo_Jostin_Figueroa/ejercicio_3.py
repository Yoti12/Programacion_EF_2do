class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        pass
    def Presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad}")

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera
    def especialidad(self):
        print(f"Hola, soy {self.nombre}, tengo {self.edad} años y mi carrera es {self.carrera}")

estudiante = Estudiante("Jostin", 19, "Tecnologías de la Información")
estudiante.Presentarse()
estudiante.especialidad()