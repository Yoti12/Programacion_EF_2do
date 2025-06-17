

nota = int(input("Ingrese la nota: "))
edad = int(input("Ingrese la edad: "))
sexo = input("Ingrese su sexo en M o F: ")

if (nota >= 5 and edad >= 18 and sexo == "F" ):
    print ("Aceptada")
else:
    print ("POSIBLE")