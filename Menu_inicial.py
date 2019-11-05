from main import Menu
from Palabra import Palabra
from BD import BD
from Gato.main import Main
import os

class MenuInicial:
    def crearmenu(self):
        p = Palabra()
        conexion = p.llenarbasedatos()
        opc="a"
        while opc!="s":
            os.system('cls')   
            opc = input("Bienvenido ¿Qué quieres jugar? \n <G> Gato || <A> Ahorcado || <S> Salir\n").lower()

            if opc=="g":
                gato=Main()
                gato.menu()
            elif opc=="a":
                ahorcado=Menu()
                ahorcado.crearMenu(conexion)
            elif opc=="s":
                print("Hasta pronto.")
            else:
                print("Tecla incorrecta, intenta de nuevo.")

menu=MenuInicial()
menu.crearmenu()