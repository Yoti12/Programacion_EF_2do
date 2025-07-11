class Producto ():
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        pass
    def mostrar_info(self):
        print(f"El producto se llama {self.nombre}, cuesta ${self.precio} y es {self.categoria}")

class ProductoConDescuento(Producto):
    def __init__(self, nombre, precio, categoria, descuento):
        super().__init__(nombre, precio, categoria)
        self.descuento = descuento
    def mostrar_info(self):
        precio_con_descuento = self.precio * (1- self.descuento /100)
        print(f"El producto se llama {self.nombre}, cuesta ${precio_con_descuento:.2f}, con descuento y es de la categoría {self.categoria}")

producto = ProductoConDescuento("Televisor", 200, "Tecnología",20)
producto.mostrar_info()

