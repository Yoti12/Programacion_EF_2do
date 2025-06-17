# Calcular la media de tres números pedidos por teclado.
import statistics
numero_1 = float(input ("Ingrese el primer valor:"))

numero_2 = float(input ("Ingrese el segundo valor:"))

numero_3 = float(input ("Ingrese el tercer valor:"))

media= statistics.mean([numero_1, numero_2, numero_3])

print ("La media de los números que ingresó es:", media)