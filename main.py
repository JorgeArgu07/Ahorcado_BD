from Palabra import Palabra
from Jugador import Jugador
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
                    opcion='s'
                    while opcion=='s':
                        palabra = input("Escribe la palabra que deseas añadir y presiona Enter para agregarla\n")
                        success=p.agregarpalabradb(palabra)
                        if success==1:
                            print("Registro exitoso")
                        else:
                            print("Ocurrió un error inténtalo de nuevo "+success)
                        opcion=input("¿Deseas agregar otra palabra? <S><N>").lower()
                    os.system('cls')

                elif opc.lower() == "j":
                    """  jugador=Jugador()
                        nojugador=0
                        for jugador in jugador.getnombresjugadores():
                            print(str(nojugador)+")"+jugador)
                            nojugador = nojugador + 1
                        print("n)Ninguno de los anteriores")
                        opcjugador=input("¿Qué jugador eres?") """
                    p = Palabra()
                    p.getpalabrabd()

                elif opc.lower() == "s":
                    print("Hasta pronto.")

                elif opc.lower() == "r":
                    p = Palabra()
                    success=p.reiniciarpalabrasbd()
                    if success==0:
                        input("Lista de palabras vacía, presione enter para agregar más palabras")
                        os.system('cls')
                        opcion='s'
                        while opcion=='s':
                            palabra = input("Escribe la palabra que deseas añadir y presiona Enter para agregarla\n")
                            success=p.agregarpalabradb(palabra)
                            if success==1:
                                print("Registro exitoso")
                            else:
                                print("Ocurrió un error inténtalo de nuevo "+success)
                            opcion=input("¿Deseas agregar otra palabra? <S><N>").lower()
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
                    otra = "s"
                    while otra == "s":
                        palabra = input("Escribe la palabra que deseas añadir y presiona Enter para agregarla\n")
                        success=p.añadirPalabra(palabra)
                        if success==1:
                            print("Palabra añadida exitosamente.")
                        else:
                            print("Ocurrió un error inténtelo de nuevo.")
                        otra=input("¿Deseas agregar otra palabra? <S><N>").lower()
                    os.system('cls')

                elif opc.lower() == "j":
                    p = Palabra()
                    success=p.getPalabra()
                    if success==0:
                        success2=p.obtenerPalabras()
                        if success2==0:
                            input("Lista de palabras vacía, presione enter para agregar más palabras")
                            otra='s'
                            while otra=='s':
                                os.system('cls')
                                palabra = input("Escribe la palabra que deseas añadir y presiona Enter para agregarla\n")
                                success3=p.añadirPalabra(palabra)
                                if success3==1:
                                    print("Palabra añadida exitosamente.")
                                else:
                                    print("Ocurrió un error inténtelo de nuevo.")
                                otra=input("¿Deseas agregar otra palabra? <S><N>").lower()

                elif opc.lower() == "s":
                    print("Hasta pronto.")

                elif opc.lower() == "r":
                    p = Palabra()
                    success=p.obtenerPalabras()
                    if success==0:
                        input("Lista de palabras vacía, presione enter para agregar más palabras")
                        os.system('cls')
                        otra='s'
                        while otra=='s':
                            os.system('cls')
                            palabra = input("Escribe la palabra que deseas añadir y presiona Enter para agregarla\n")
                            success=p.añadirPalabra(palabra)
                            if success==1:
                                print("Palabra añadida exitosamente.")
                            else:
                                print("Ocurrió un error inténtelo de nuevo.")
                            otra=input("¿Deseas agregar otra palabra? <S><N>").lower()

                    print("Lista de palabras reiniciada.")

                else:
                    print("Tecla incorrecta. Vuelve a intentarlo.")


menu = Menu()
menu.crearMenu()