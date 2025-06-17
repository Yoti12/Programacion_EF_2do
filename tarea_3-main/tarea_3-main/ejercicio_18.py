# Mostrar las iniciales de una persona a partir de su nombre y dos apellidos

nombre = input("Ingrese su nombre: ")
apellido1 = input("Ingrese su primer apellido: ")
apellido2 = input("Ingrese su segundo apellido: ")

iniciales = nombre[0].upper() + apellido1[0].upper() + apellido2[0].upper()

print(f"Iniciales: {iniciales}")
