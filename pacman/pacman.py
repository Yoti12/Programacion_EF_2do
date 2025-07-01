import turtle
import math
import random

# --- Configuración inicial de la pantalla ---
ventana = turtle.Screen()
ventana.title("Mini Pac-Man Nivel 1")
ventana.bgcolor("black")
ventana.setup(width=700, height=700)
ventana.tracer(0)

# --- Creación de los actores del juego ---
class Jugador(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.speed(0)
        self.direccion = "stop"
        self.velocidad = 200  # velocidad inicial en milisegundos

    def mover(self):
        x, y = self.xcor(), self.ycor()
        nuevo_x, nuevo_y = x, y  # variables para calcular el nuevo destino

        if self.direccion == "up":
            nuevo_y += 24
        elif self.direccion == "down":
            nuevo_y -= 24
        elif self.direccion == "left":
            nuevo_x -= 24
        elif self.direccion == "right":
            nuevo_x += 24

        # verificar si hay una pared en la nueva posición
        puede_moverse = True
        for pared in paredes:
            if math.hypot(pared.xcor() - nuevo_x, pared.ycor() - nuevo_y) < 20:
                puede_moverse = False
                break

        if puede_moverse:
            self.goto(nuevo_x, nuevo_y)

    def direccion_arriba(self):
        self.direccion = "up"

    def direccion_abajo(self):
        self.direccion = "down"

    def direccion_izquierda(self):
        self.direccion = "left"

    def direccion_derecha(self):
        self.direccion = "right"

class Pared(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.goto(x, y)

class Punto(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(0)
        self.goto(x, y)

# clase para las frutas
class Fruta(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed(0)
        self.goto(x, y)

# --- Mapa del nivel 1: W = wall, . = punto, F = fruta ---
nivel1 = [
    "WWWWWWWWWWWWWW",
    "W....F.......W",  
    "W.WWW.WWWW.W.W",
    "W.......F....W", 
    "W.WWW.WWWW.W.W",
    "W....F.......W", 
    "WWWWWWWWWWWWWW"
]

paredes = []
puntos = []
frutas = []  # lista para almacenar las frutas

# --- Función para construir el nivel ---
def construir_nivel(mapa):
    for y in range(len(mapa)):
        for x in range(len(mapa[y])):
            caracter = mapa[y][x]
            pos_x = -288 + (x * 48)
            pos_y = 288 - (y * 48)

            if caracter == "W":
                pared = Pared(pos_x, pos_y)
                paredes.append(pared)
            elif caracter == ".":
                punto = Punto(pos_x, pos_y)
                puntos.append(punto)
            elif caracter == "F":  # si hay una fruta, crearla
                fruta = Fruta(pos_x, pos_y)
                frutas.append(fruta)

jugador = Jugador()
construir_nivel(nivel1)

ventana.listen()
ventana.onkeypress(jugador.direccion_arriba, "Up")
ventana.onkeypress(jugador.direccion_abajo, "Down")
ventana.onkeypress(jugador.direccion_izquierda, "Left")
ventana.onkeypress(jugador.direccion_derecha, "Right")

def colision_con_punto():
    for punto in puntos:
        if jugador.distance(punto) < 20:
            punto.hideturtle()
            puntos.remove(punto)

# detectar colisión con frutas
def colision_con_fruta():
    for fruta in frutas:
        if jugador.distance(fruta) < 20:
            fruta.hideturtle()
            frutas.remove(fruta)
            jugador.velocidad = int(jugador.velocidad * 0.8)  # aumenta velocidad un 20%
            break

# --- Bucle principal del juego ---
def bucle_juego():
    jugador.mover()
    colision_con_punto()
    colision_con_fruta()  # verificar frutas

    if len(puntos) == 0:
        print("¡Ganaste!")
        return

    ventana.update()
    ventana.ontimer(bucle_juego, jugador.velocidad)  # ahora depende de velocidad del jugador

bucle_juego()
ventana.mainloop()
