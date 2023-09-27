"""
Consigna
Deberán crear una aplicación de consola que simulara el juego “Adivina el numero”
 1-Generación de número aleatorio: El programa debe generar un número aleatorio dentro de 
un rango predefinido.
 2-Entrada de jugadores: Cada jugador ingresa su nombre para identificarse.
 3-Adivinanzas de los jugadores: En cada turno, cada jugador ingresa un número como su 
intento de adivinanza.
 4-Validación de respuestas: El programa compara el número ingresado por cada jugador con 
el número aleatorio generado y brinda retroalimentación (mayor, menor o igual) para ayudar a 
los jugadores a adivinar.
 5-Puntuación: Llevar un registro de la puntuación de cada jugador, contabilizando el número 
de intentos realizados.
 6-Finalización del juego: El juego termina cuando uno de los jugadores adivina correctamente 
el número o cuando se alcanza un límite de intentos.
 7-Registro de puntuaciones: Mantener un registro de las puntuaciones más altas de los 
jugadores y mostrarlas al final del juego.
"""
# 1- Bienvenidos a el juego “Adivina el numero”
import random

num_ganador = random.randint(1, 100)
intentos = 0

# 2-
while True:
  num_elegido= int(input("Ingresa un número (entre 1 y 100): "))
  intentos += 1
  if num_elegido == num_ganador:
     print(f"¡Correcto! Adivinaste el número en {intentos} intentos.")
     break
  elif num_elegido < num_ganador:
     print("Te quedaste corto. Intenta nuevamente.")
  else:
    print("Te pasaste. Intenta nuevamente.")

nvo_juego = input("¿Queres jugar de nuevo? (s/n): ")
if nvo_juego.lower() != 's':
 print("gracias por jugar regresa pronto ") 


