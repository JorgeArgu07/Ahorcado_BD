from Gato.Tablero import Tablero
from Gato.Jugador import Jugador
from Gato import Gato
import os

class Main:


    def menu(self, j1, j2):
        ganador = 0
        reset = "s"
        turno = 1
        tablero = Tablero()

        while reset == "s":
            while ganador == 0:

                print(tablero.dibujarTablero())
                if turno == 1:
                    pos = input("Turno de " + j1.getNombre() + "\n")
                    tablero.setPosicion(pos, j1.getFicha())


                    if tablero.verificarEmpate():
                        ganador = 1
                        print(tablero.dibujarTablero())
                        print("Es un empate.")

                    if tablero.verificarGanador(j1.getFicha()):
                        ganador = 1
                        print(tablero.dibujarTablero())
                        print("Ganador!!")

                    turno = 2
                else:
                    pos = input("Turno de " + j2.getNombre() + "\n")
                    tablero.setPosicion(pos, j2.getFicha())

                    if tablero.verificarEmpate():
                        ganador = 1
                        print(tablero.dibujarTablero())
                        print("Es un empate.")

                    if tablero.verificarGanador(j2.getFicha()):
                        ganador = 1
                        print(tablero.dibujarTablero())
                        print("Ganador!!")
                    turno = 1
            reset = input("Deseas volver a jugar?(s/n)\n")
            reset.lower()
            if reset == "s":
                ganador = 0
                turno = 1
                tablero.resetTablero()
