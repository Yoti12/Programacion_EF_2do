# Crea un programa que pida al usuario dos números y muestre su división si el segundo no
# es cero, o un mensaje de aviso en caso contrario

numero_1 = float(input("Ingrese el primer valor: "))

numero_2 = float(input("Ingrese el segundo valor: "))

if (numero_2 !=0 ):
    resultado = numero_1 / numero_2
    print("La división es: ", resultado)
else:
    print("ERROR\n" + "No se puede dividir entre 0")