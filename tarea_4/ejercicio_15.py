# La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el
# cobro es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos
# cuestan 1 euro, los siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos,
# y a partir del décimo minuto, 50 céntimos. Además, se carga un impuesto de 3 % cuando
# es domingo, y si es otro día, en turno de mañana, 15 %, y en turno de tarde, 10 %. Realice
# un algoritmo para determinar cuánto debe pagar por cada concepto una persona que realiza una llamada.

duracion = float(input("Duración (minutos): "))
dia = input("Día de la semana: ")
turno = input("Turno (mañana o tarde): ")


if duracion <= 5:
    costo = 1
elif duracion <= 8:
    costo = 1 + (duracion - 5) * 0.80
elif duracion <= 10:
    costo = 1 + 3 * 0.80 + (duracion - 8) * 0.70
else:
    costo = 1 + 3 * 0.80 + 2 * 0.70 + (duracion - 10) * 0.50


if dia == "domingo":
    impuesto = costo * 0.03
elif turno == "mañana":
    impuesto = costo * 0.15
else:
    impuesto = costo * 0.10

total = costo + impuesto
print("Base:", round(costo, 2))
print("Impuesto:", round(impuesto, 2))
print("Total:", round(total, 2))
