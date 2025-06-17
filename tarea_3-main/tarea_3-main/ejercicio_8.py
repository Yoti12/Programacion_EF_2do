# Calcular el sueldo total de un vendedor con un sueldo base más un 10% extra por comisión de tres ventas.
sueldo_base = 450
comision_por_venta = 0.10
ventas_totales = int(input("Ingrese las ventas realizadas:"))
sueldo_total = sueldo_base * (comision_por_venta * ventas_totales)
print ("El sueldo total que recibirá es de: ", round(sueldo_total,1))