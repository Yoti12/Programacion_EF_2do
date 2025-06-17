# Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un
# dado de seis caras y muestre por pantalla el número en letras (dato cadena) de la cara
# opuesta al resultado obtenido.
# • Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-
# 6, 2-5 y 3-4.
# • Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se
# mostrará el mensaje: “ERROR: número incorrecto.”.
# Ejemplo:
# Introduzca número del dado: 5
# En la cara opuesta está el "dos".
numero = int(input("Introduzca número del dado: "))
if numero == 1:
    print('En la cara opuesta está el "seis".')
elif numero == 2:
    print('En la cara opuesta está el "cinco".')
elif numero == 3:
    print('En la cara opuesta está el "cuatro".')
elif numero == 4:
    print('En la cara opuesta está el "tres".')
elif numero == 5:
    print('En la cara opuesta está el "dos".')
elif numero == 6:
    print('En la cara opuesta está el "uno".')
else:
    print("ERROR: número incorrecto.")
