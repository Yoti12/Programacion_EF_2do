class Animal():
    def __init__(self, nombre):
        self.nombre = nombre 
        pass

    def hacer_sonido(self):
            print(f"Hacer sonido")

class Perro (Animal):
     def hacer_sonido(self):
          print(f"{perro.nombre} hace guau")
    
class Gato (Animal):
     def hacer_sonido(self):
          print(f"{gato.nombre} hace miau")

perro = Perro("Negra")
gato = Gato("Michurrio")

perro.hacer_sonido()
gato.hacer_sonido()