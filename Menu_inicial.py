from main import Menu
from Palabra import Palabra
from BD import BD
from Jugador import Jugador
from Gato.main import Main
import os

class MenuInicial:
    def crearmenu(self):

        j=Jugador()
        conexion2=j.llenarjugadoresbd()
        jugadores=[]
        jugador=""
        puntos=0
        p = Palabra()
        conexion = p.llenarbasedatos()
        opc="a"

        print("¡Identifícate! ¿Cuál es tu nombre de jugador?")
        if conexion==1 and conexion2==1:
                                                                     # CON CONEXION
# =============================================================================================================================================================================
            print("Estás jugando con conexión.")
            for row in j.getnombresjugadoresbd():
                print(row)
            jugador=input("\n")
            existe=str(j.verifyjugadorbd(jugador))
            if existe=="0":
                os.system('cls')
                input("El nombre de jugador que escribió no existe, se agregará como un jugador nuevo.\nPresione Enter para continuar")
                if j.agregarjugadorbd(jugador)==0:
                    os.system('cls')
                    print("Ocurrió un error inesperado, inténtalo nuévamente.")
                else:
                    os.system('cls')
                    existe=str(j.verifyjugadorbd(jugador))
                    jugador=existe
                    puntos=j.verifypuntosjugadorbd(jugador)
                    input("¡Estás jugando como "+jugador+"! tienes {} puntos\nPresiona Enter para continuar".format(puntos))
            else:
                os.system('cls')
                jugador=existe
                puntos=j.verifypuntosjugadorbd(jugador)
                input("¡Estás jugando como "+jugador+"! tienes {} puntos\nPresiona Enter para continuar".format(puntos))
        else:
                                                                        # SIN CONEXION
# =============================================================================================================================================================================
            print("Estás jugando sin conexión.")
            for row in j.getnombresjugadores():
                print(row)
            jugador=input("\n")
            existe=str(j.verifyjugador(jugador))
            if existe=="0":
                os.system('cls')
                input("El nombre de jugador que escribió no existe, se agregará como un jugador nuevo.\nPresione Enter para continuar")
                if j.agregarjugador(jugador)!=1:
                    os.system('cls')
                    print("Ocurrió un error inesperado, inténtalo nuévamente.")
                else:
                    os.system('cls')
                    existe=str(j.verifyjugador(jugador))
                    jugador=existe
                    puntos=j.verifypuntosjugador(jugador)
                    input("¡Estás jugando como "+jugador+"! tienes {} puntos\nPresiona Enter para continuar".format(puntos))
            else:
                os.system('cls')
                jugador=existe
                puntos=j.verifypuntosjugador(jugador)
                input("¡Estás jugando como "+jugador+"! tienes {} puntos\nPresiona Enter para continuar".format(puntos))

        while opc!="s":
            os.system('cls')   
            opc = input("Bienvenido ¿Qué quieres jugar? \n <G> Gato || <A> Ahorcado || <S> Salir\n").lower()
            if opc=="g":
                gato=Main()
                gato.menu()
            elif opc=="a":
                ahorcado=Menu()
                ahorcado.crearMenu(conexion, jugador)
            elif opc=="s":
                print("Hasta pronto.")
            else:
                print("Tecla incorrecta, intenta de nuevo.")

menu=MenuInicial()
menu.crearmenu()