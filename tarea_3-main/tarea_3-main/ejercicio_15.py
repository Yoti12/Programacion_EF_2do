# Intercambiar los valores de dos variables \(A\) y \(B\) e imprimir el resultado.

variable_A = input("Ingrese el valor de A: ")
variable_B = input("Ingrese el valor de B: ")
print(f"Antes del intercambio: A = {variable_A}, B = {variable_B}")
variable_A, variable_B = variable_B, variable_A
print(f"Después del intercambio: A = {variable_A}, B = {variable_B}")
