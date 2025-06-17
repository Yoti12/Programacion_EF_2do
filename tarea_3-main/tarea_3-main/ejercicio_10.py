#Calcular la calificación final de un alumno en Algoritmos, considerando:
#  - 55% promedio de tres parciales.
#  - 30% examen final.
#  - 15% trabajo final


parcial1 = float(input("Ingrese la calificación del Parcial 1: "))
parcial2 = float(input("Ingrese la calificación del Parcial 2: "))
parcial3 = float(input("Ingrese la calificación del Parcial 3: "))
examen_final = float(input("Ingrese la calificación del Examen Final: "))
trabajo_final = float(input("Ingrese la calificación del Trabajo Final: "))

promedio_parciales = (parcial1 + parcial2 + parcial3) / 3
calificacion_final = (promedio_parciales * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)

print(f"La calificación final es: {calificacion_final:.2f}")