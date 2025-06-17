# Algoritmo que pida tres números y los muestre ordenados (de mayor a menor);
numero_1 = int(input("Ingrese el primer valor: "))
numero_2 = int(input("Ingrese el segundo valor: "))
numero_3 = int(input("Ingrese el tercer valor: "))

if numero_1 >= numero_2 and numero_1 >= numero_3:
    if numero_2 >= numero_3:
        print(numero_1, numero_2, numero_3)
    else:
        print(numero_1, numero_3, numero_2)

elif numero_2 >= numero_1 and numero_2 >= numero_3:
    if numero_1 >= numero_3:
        print(numero_2, numero_1, numero_3)
    else:
        print(numero_2, numero_3, numero_1)

else:
    if numero_1 >= numero_2:
        print(numero_3, numero_1, numero_2)
    else:
        print(numero_3, numero_2, numero_1)