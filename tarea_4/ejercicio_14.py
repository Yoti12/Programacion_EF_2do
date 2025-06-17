# El director de una escuela está organizando un viaje de estudios, y requiere determinar
# cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el
# servicio. La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada
# alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95
# euros, y si son menos de 30, el costo de la renta del autobús es de 4000 euros, sin
# importar el número de alumnos. Realice un algoritmo que permita determinar el pago a la
# compañía de autobuses y lo que debe pagar cada alumno por el viaje.
# Leer el número de alumnos

alumnos = int(input("Ingrese el número de alumnos: "))

costo_por_alumno = 0
pago_compania = 0

if alumnos >= 100:
    costo_por_alumno = 65
    pago_compania = alumnos * costo_por_alumno
elif alumnos >= 50:
    costo_por_alumno = 70
    pago_compania = alumnos * costo_por_alumno
elif alumnos >= 30:
    costo_por_alumno = 95
    pago_compania = alumnos * costo_por_alumno
else:
    pago_compania = 4000
    if alumnos > 0:
        costo_por_alumno = pago_compania / alumnos
    else:
        costo_por_alumno = 0 
print(f"Pago a la compañía: {pago_compania} euros")
print(f"Costo por alumno: {costo_por_alumno:.2f} euros")
