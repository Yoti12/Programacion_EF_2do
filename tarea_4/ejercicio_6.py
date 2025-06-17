# Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.

ingreso_por_teclado = input("Ingrese una palabra: ")

tiene_mayuscula = False
for letra in ingreso_por_teclado:
    if letra.isupper():
        tiene_mayuscula = True
        break

if tiene_mayuscula:
    print("Su palabra tiene al menos una letra mayúscula")
else:
    print("Su palabra no tiene letras mayúsculas")
