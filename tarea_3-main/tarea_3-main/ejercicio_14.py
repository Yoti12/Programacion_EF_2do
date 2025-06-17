# Invertir un número de dos cifras (ejemplo: 23 → 32)

numero = int(input("Ingrese un número de dos cifras: "))

if 10 <= abs(numero) <= 99:
    decena = numero // 10
    unidad = numero % 10
    invertido = (unidad * 10) + decena
    print(f"Número invertido: {invertido}")
else:
    print("Por favor, ingrese un número de DOS cifras.")
