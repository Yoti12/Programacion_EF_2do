# Escribir un programa que lea un año indicar si es bisiesto. Nota: un año es bisiesto si es un
# número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible
# por 400.
# Leer el año
año = int(input("Ingrese un año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")
