from Palabra import Palabra
from BD import BD
import os
class Menu:


    def crearMenu(self):
        p = Palabra()
        conexion = p.llenarbasedatos()
        opc = "a"   
        while opc != "s":
            if conexion == 1:
                                                                # CON CONEXIÓN
# ==================================================================================================================================================
                os.system('cls')
                print("¡Estás jugando con conexión!")
                opc = input("Bienvenido ¿Que deseas hacer? \n <J> = Jugar || <A> = Añadir Palabra || <R> Reiniciar Palabras || <S> Salir ")
                if opc.lower() == "a":
                    p = Palabra()
                    p.agregarpalabradb()
                    os.system('cls')

                elif opc.lower() == "j":
                    p = Palabra()
                    p.getpalabrabd()

                elif opc.lower() == "s":
                    print("Hasta pronto.")

                elif opc.lower() == "r":
                    p = Palabra()
                    p.reiniciarpalabrasbd()
                    print("Lista de palabras reiniciada.")

                else:
                    print("Tecla incorrecta. Vuelve a intentarlo.")

                                                            # SIN CONEXION
# ==================================================================================================================================================
            else:
                print("Estás jugando sin conexión.")
                opc = input("Bienvenido ¿Que deseas hacer? \n <J> = Jugar || <A> = Añadir Palabra || <R> Reiniciar Palabras || <S> Salir ")
                if opc.lower() == "a":
                    p = Palabra()
                    p.añadirPalabra()
                    os.system('cls')

                elif opc.lower() == "j":
                    p = Palabra()
                    p.getPalabra()


                elif opc.lower() == "s":
                    print("Hasta pronto.")

                elif opc.lower() == "r":
                    p = Palabra()
                    p.obtenerPalabras()
                    print("Lista de palabras reiniciada.")

                else:
                    print("Tecla incorrecta. Vuelve a intentarlo.")


menu = Menu()
menu.crearMenu()