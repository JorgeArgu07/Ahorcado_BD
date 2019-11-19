from main import Menu
from Gato.Jugador import Jugador
from Palabra import Palabra
from BD import BD
from Gato.main import Main
import os

p = Palabra()
conexion = p.llenarbasedatos()
opc="a"
while opc!="s":
    os.system('cls')
    opc = input("Bienvenido ¿Qué quieres jugar? \n <G> Gato || <A> Ahorcado || <S> Salir\n").lower()

    if opc=="g":
        j1nombre = input("Ingresa el nombre del jugador 1 (O)\n")
        j1 = Jugador(j1nombre, "X")

        j2nombre = input("Ingresa el nombre del jugador 2 (X)\n")
        j2 = Jugador(j2nombre, "O")

        gato=Main()
        gato.menu(j1, j2)
    elif opc=="a":
        ahorcado=Menu()
        ahorcado.crearMenu(conexion)
    elif opc=="s":
        print("Hasta pronto.")
    else:
        print("Tecla incorrecta, intenta de nuevo.")

