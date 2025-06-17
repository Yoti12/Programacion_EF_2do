# Algoritmo que pida dos números e indique si el primero es mayor que el segundo o no.
numero_1 = int(input("Ingrese el primer número: "))
numero_2 = int(input("Ingrese el segundo número: "))

if (numero_1>numero_2):
    print(numero_1, "es mayor que",numero_2)

elif numero_1 < numero_2:
        print(numero_1,"no es mmayor a",numero_2)

else:
    print("Ambos valores son iguales")

print("Fin del Programa")