class Vehiculo ():
    def __init__(self, marca, modelo, velocidad):
        self.__marca = marca
        self.__modelo = modelo
        self.__velocidad = velocidad
        pass
    def get_velocidad(self):
        return self.__velocidad
    
    def set_velocidad(self, nueva_velocidad):
        if nueva_velocidad >= 0:
            self.__velocidad = nueva_velocidad
        else:
            print("La velocidad no puede ser negativa.")

class Auto(Vehiculo):
    def acelerar(self, incremento):
        nueva_velocidad = self.get_velocidad() + incremento
        self.set_velocidad(nueva_velocidad)

auto = Auto("Hyundai", "Kia",0)
print("Velocidad inicial:", auto.get_velocidad())
auto.acelerar(15)
print("Velocidad después de acelerar:", auto.get_velocidad())
auto.acelerar(10)
print("Velocidad después de acelerar", auto.get_velocidad())

    