import turtle
import random
import time

# Configurar la pantalla
pantalla = turtle.Screen()
pantalla.title("Mini Pacman 🟡")
pantalla.bgcolor("black")
pantalla.setup(width=600, height=600)

# Crear al jugador
jugador = turtle.Turtle()
jugador.shape("circle")
jugador.color("yellow")
jugador.penup()
jugador.speed(0)

# Crear el "punto" a comer
punto = turtle.Turtle()
punto.shape("circle")
punto.color("red")
punto.penup()
punto.speed(0)
punto.goto(random.randint(-280, 280), random.randint(-280, 280))

# Crear el marcador
marcador = turtle.Turtle()
marcador.hideturtle()
marcador.color("white")
marcador.penup()
marcador.goto(0, 260)
puntos = 0
marcador.write(f"Puntos: {puntos}", align="center", font=("Arial", 16, "normal"))

# Movimiento del jugador
def arriba():
    jugador.setheading(90)
    jugador.forward(20)

def abajo():
    jugador.setheading(270)
    jugador.forward(20)

def izquierda():
    jugador.setheading(180)
    jugador.forward(20)

def derecha():
    jugador.setheading(0)
    jugador.forward(20)

# Controles
pantalla.listen()
pantalla.onkeypress(arriba, "Up")
pantalla.onkeypress(abajo, "Down")
pantalla.onkeypress(izquierda, "Left")
pantalla.onkeypress(derecha, "Right")

# Bucle principal del juego
while True:
    pantalla.update()
    # Detectar colisión con el punto
    if jugador.distance(punto) < 20:
        punto.goto(random.randint(-280, 280), random.randint(-280, 280))
        puntos += 1
        marcador.clear()
        marcador.write(f"Puntos: {puntos}", align="center", font=("Arial", 16, "normal"))
    time.sleep(0.05)  # Pequeño retraso para suavizar el bucle
