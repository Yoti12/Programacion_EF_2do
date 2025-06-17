# Escribe un programa que lea un número e indique si es par o impar.
numero = int(input("Ingrese un valor: "))
condicion_par = numero / 2

if (numero % 2 == 0):
    print("El número es par")
else:
    print("El número es impar")

print ("FIN DEL PROGRAMA")