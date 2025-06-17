# Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta

dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
año = int(input("Ingrese el año: "))

bisiesto = (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

# Asignar la cantidad de días que tiene cada mes
if mes == 2:
    dias_mes = 29 if bisiesto else 28
elif mes in [4, 6, 9, 11]:
    dias_mes = 30
elif mes in [1, 3, 5, 7, 8, 10, 12]:
    dias_mes = 31
else:
    dias_mes = 0
if mes >= 1 and mes <= 12 and dia >= 1 and dia <= dias_mes:
    print("La fecha es válida")
else:
    print("La fecha no es válida")
