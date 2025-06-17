# Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de
# los lados de un triángulo. El programa debe determinar qué tipo de triangulo es, teniendo
# en cuenta los siguiente:
# • Si se cumple Pitágoras entonces es triángulo rectángulo
# • Si sólo dos lados del triángulo son iguales entonces es isósceles.
# • Si los 3 lados son iguales entonces es equilátero.
# • Si no se cumple ninguna de las condiciones anteriores, es escaleno.

lado_1 = float(input("Ingrese el lado 1: "))
lado_2 = float(input("Ingrese el lado 2: "))
lado_3 = float(input("Ingrese el lado 3: "))

if pow(lado_1, 2) + pow(lado_2, 2) == pow(lado_3, 2) or \
   pow(lado_1, 2) + pow(lado_3, 2) == pow(lado_2, 2) or \
   pow(lado_2, 2) + pow(lado_3, 2) == pow(lado_1, 2):
    print("El triángulo es rectángulo")
elif lado_1 == lado_2 == lado_3:
    print("El triángulo es equilátero")
elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
    print("El triángulo es isósceles")
else:
    print("El triángulo es escaleno")
