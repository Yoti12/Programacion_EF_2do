 #La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la
# cual se clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del
# producto, ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un
# productor por la uva que entrega en un embarque, considerando lo siguiente: si es de tipo
# A, se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de
# tamaño 2. Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos
# cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida
precio_inicial = float(input("Ingrese el precio inicial por kilo de uva: "))
tipo = input("Ingrese el tipo de uva (A o B): ").upper()
tamaño = int(input("Ingrese el tamaño de la uva (1 o 2): "))
kilos = float(input("Ingrese la cantidad de kilos entregados: "))

if tipo == "A":
    if tamaño == 1:
        precio_final = precio_inicial + 0.20
    elif tamaño == 2:
        precio_final = precio_inicial + 0.30
    else:
        print("Tamaño inválido")
        precio_final = None
elif tipo == "B":
    if tamaño == 1:
        precio_final = precio_inicial - 0.30
    elif tamaño == 2:
        precio_final = precio_inicial - 0.50
    else:
        print("Tamaño inválido")
        precio_final = None
else:
    print("Tipo inválido")
    precio_final = None
if precio_final is not None:
    ganancia = precio_final * kilos
    print("La ganancia del productor es: $", round(ganancia, 2))
