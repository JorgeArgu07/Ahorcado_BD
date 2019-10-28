from Tablero import Tablero
from Jugador import Jugador
import os

turno = 1
ganador = 0
reset = "s"

j1nombre = input("Ingresa el nombre del jugador 1\n")
j1 = Jugador(j1nombre, "X")

j2nombre = input("Ingresa el nombre del jugador 2\n")
j2 = Jugador(j2nombre, "O")


tablero = Tablero()


while reset == "s":
	while ganador == 0:

		
		print(Tablero.dibujarTablero())
		if turno == 1:
			pos = input("Turno de "+j1.getNombre()+"\n")
			Tablero.setPosicion(pos, j1.getFicha())
		
			if Tablero.verificar(j1.getFicha()):
				ganador = 1
				print(Tablero.dibujarTablero())
				print("Ganador!!")
			turno = 2

		else:
			pos = input("Turno de "+j2.getNombre()+"\n")
			Tablero.setPosicion(pos, j2.getFicha())
			
			if Tablero.verificar(j2.getFicha()):
				ganador = 1
				print(Tablero.dibujarTablero())
				print("Ganador!!")
			turno = 1
reset = input("Deseas volver a jugar?(s/n)\n")
reset.lower()	
	








