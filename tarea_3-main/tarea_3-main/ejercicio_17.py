# Determinar la hora de llegada a una ciudad B, dada la hora de salida de A (HH:MM: SS) y el tiempo de viaje en segundos
from datetime import datetime, timedelta

hora_salida_str = input("Ingrese la hora de salida (HH:MM:SS): ")
tiempo_viaje_segundos = int(input("Ingrese la duración del viaje en segundos: "))

hora_salida = datetime.strptime(hora_salida_str, "%H:%M:%S")

duracion = timedelta(seconds=tiempo_viaje_segundos)
hora_llegada = hora_salida + duracion

print("Hora de llegada a ciudad B:", hora_llegada.time())
