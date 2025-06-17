# Una compañía de transporte internacional tiene servicio en algunos países de América del
# Norte, América Central, América del Sur, Europa y Asia. El costo por el servicio de
# transporte se basa en el peso del paquete y la zona a la que va dirigido. Lo anterior se
# muestra en la tabla:
# Parte de su política implica que los paquetes con un peso superior a 5 kg no son
# transportados, esto por cuestiones de logística y de seguridad. Realice un algoritmo para
# determinar el cobro por la entrega de un paquete o, en su caso, el rechazo de la entrega.



peso = float(input("Introduce el peso del paquete en kg: "))
zona = int(input("Introduce la zona de destino (1 a 5): "))

if peso > 5:
    print("Paquete no transportable.")
else:
    gramos = peso * 1000

    if zona == 1:
        costo = gramos * 24
        print("Costo:", costo, "euros")
    elif zona == 2:
        costo = gramos * 20
        print("Costo:", costo, "euros")
    elif zona == 3:
        costo = gramos * 21
        print("Costo:", costo, "euros")
    elif zona == 4:
        costo = gramos * 10
        print("Costo:", costo, "euros")
    elif zona == 5:
        costo = gramos * 18
        print("Costo:", costo, "euros")
    else:
        print("Zona no válida.")
