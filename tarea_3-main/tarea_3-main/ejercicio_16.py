# Calcular el tiempo (en minutos) en que un vehículo más rápido alcanza a otro, dada la distancia d y velocidades v1 y v2.

d = float(input("Ingrese la distancia entre los vehículos (km): "))
v1 = float(input("Ingrese la velocidad del vehículo más rápido (km/h): "))
v2 = float(input("Ingrese la velocidad del vehículo más lento (km/h): "))

if v1 > v2:
    tiempo_horas = d / (v1 - v2)
    tiempo_minutos = tiempo_horas * 60
    print(f"El vehículo más rápido alcanzará al otro en {tiempo_minutos:.2f} minutos.")
else:
    print("Error: La velocidad del vehículo más rápido debe ser mayor que la del más lento.")
