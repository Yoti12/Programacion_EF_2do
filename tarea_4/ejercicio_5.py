# Escribe un programa que pida un nombre de usuario y una contraseña y si se ha 
# introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error

nombre_usuario = input("INGRESE SU NOMBRE DE USUARIO: ")
contraseña = input("INGRESE SU CONTRASEÑA: ")

if (nombre_usuario == "pepe" and contraseña == "asdasd"):
    print("HAZ ENTRADO AL SISTEMA")
else:
    print("ERROR\n" + "NOMBRE DE USUARIO O CONTRASEÑA INCORRECTO")