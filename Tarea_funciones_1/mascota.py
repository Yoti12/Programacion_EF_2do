class Mascota ():
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy {self.nombre} soy un/a {self.especie} y tengo {self.edad} años")
    
    def cumplir_anios(self, edad):
        for i in range(edad):
            self.edad +=1


mascota1 = Mascota("Negra","perro", 5)
mascota2 = Mascota("Pepina","loro", 3)
mascota3 = Mascota("Max","gato", 0.5)

mascota1.cumplir_anios(3) #Desafío

mascota1.presentarse()
mascota2.presentarse()
mascota3.presentarse()