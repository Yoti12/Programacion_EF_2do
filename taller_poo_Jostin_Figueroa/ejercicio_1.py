class Ave ():
    def __init__(self, nombre):
        self.nombre = nombre
        pass

    def Volar (self):
        print("EL ave vuela")

class Aguila (Ave):
    def Volar(self):
        print("El águila vuela alto")

class Pinguino (Ave):
    def Volar(self):
        print("El pinguino no puede volar")

aguila = Aguila("Apolo")
pinguino = Pinguino("Ramon")

aguila.Volar()
pinguino.Volar()