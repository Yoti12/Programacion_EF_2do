#Convertir una cantidad de minutos a horas y minutos (ejemplo: 1000 minutos →
#16 horas y 40 minutos).

minutos = int(input (("Ingrese la hora en minutos: ")))
conversion_hora = minutos // 60
conversion_segundos = minutos % 60
print ("En",minutos, "hay",conversion_hora,"horas","y", conversion_segundos,"minutos")
