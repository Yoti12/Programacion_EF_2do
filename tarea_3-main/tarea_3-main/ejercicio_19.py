# # Calcular la nota final de un estudiante según:
#  - Respuesta correcta: +5 puntos.
#  - Incorrecta: -1 punto.
#  - En blanco: 0 puntos. 

correctas = int(input("Número de respuestas correctas: "))
incorrectas = int(input("Número de respuestas incorrectas: "))
en_blanco = int(input("Número de respuestas en blanco: "))

nota_final = (correctas * 5) + (incorrectas * -1) + (en_blanco * 0)

print(f"La nota final del estudiante es: {nota_final}")
