from Palabra import Palabra
from Jugador import Jugador
from BD import BD
from Dibujo import Dibujo
import os
class Menu:


    def crearMenu(self, conexion, jugador):
        j=Jugador()
        opc = "a"
        while opc != "s":
            if conexion == 1:
                                                                # CON CONEXIÓN
# ==================================================================================================================================================
                os.system('cls')
                print("¡Estás jugando con conexión!")
                os.system('cls')
                opc = input("Bienvenido "+jugador+" ¿Qué deseas hacer? \n <J> = Jugar || <A> = Añadir Palabra || <R> Reiniciar Palabras || <S> Salir || <V> Ver Jugadores\n")
                if opc.lower() == "a":
                    p = Palabra()
                    opcion='s'
                    while opcion=='s':
                        os.system('cls')
                        palabra = input("Escribe la palabra que deseas añadir y presiona Enter para agregarla\n")
                        success=p.agregarpalabradb(palabra)
                        if success==1:
                            print("Registro exitoso")
                        else:
                            print("Ocurrió un error inténtalo de nuevo "+success)
                        opcion=input("¿Deseas agregar otra palabra? <S> Si || <N> No\n").lower()
                    os.system('cls')

                elif opc.lower() == "j":
                    os.system('cls')
                    p = Palabra()
                    success = p.getpalabrabd()
                    if success==0:
                        success2=p.reiniciarpalabrasbd()
                        if success2==0:
                            input("Lista de palabras vacía, presione enter para agregar más palabras")
                            otra='s'
                            while otra=='s':
                                os.system('cls')
                                palabra = input("Escribe la palabra que deseas añadir y presiona Enter para agregarla\n")
                                success3=p.agregarpalabradb(palabra)
                                if success3==1:
                                    print("Palabra añadida exitosamente.")
                                else:
                                    print("Ocurrió un error inténtelo de nuevo.")
                                otra=input("¿Deseas agregar otra palabra? <S> Si || <N> No\n").lower()
                    else:
                        palabratyd=p.separarPalabra(success)
                        palabraTapada = palabratyd[1]
                        palabraDestapada = palabratyd[0]

                        palabra = ''.join(palabraDestapada)
                        intentos = 5
                        ganador = True
                        dibujo = Dibujo()
                        actual = dibujo.dibujarHorca()

                        while palabraTapada != palabraDestapada:

                            print(actual)
                            print(''.join(palabraDestapada))
                            print(''.join(palabraTapada))
                            print("Tienes " + str(intentos) + " intentos")
                            letraIngresada = input("Escribe una letra o una palabra\n")
                            letraIngresada.lower()

                            if letraIngresada == palabra:
                                palabraTapada = palabraDestapada
                            else:
                                posiciones = [i for i, l in enumerate(palabraDestapada) if l == letraIngresada]
                                if len(posiciones) > 0:
                                    # enumerate(palabraTapada)
                                    for n in posiciones:
                                        palabraTapada[n] = letraIngresada
                                    os.system('cls')
                                    print("Acertaste!")
                                else:
                                    intentos -= 1
                                    if intentos == 4:
                                        os.system('cls')
                                        actual = dibujo.dibujarCabeza()
                                        # print(palabraTapada)
                                    elif intentos == 3:
                                        os.system('cls')
                                        actual = dibujo.dibujarBrazo1()
                                        # print(palabraTapada)
                                    elif intentos == 2:
                                        os.system('cls')
                                        actual = dibujo.dibujarBrazo2()
                                        # print(palabraTapada)
                                    elif intentos == 1:
                                        os.system('cls')
                                        actual = dibujo.dibujarPierna1()
                                        # print(palabraTapada)
                                    elif intentos == 0:
                                        os.system('cls')
                                        palabraTapada = palabraDestapada
                                        ganador = False
                        if ganador:
                            os.system('cls')
                            j.sumarpuntobd(jugador)
                            input("Adivinaste la palabra. Ganaste!\nPresiona enter para continuar")
                        else:
                            print(dibujo.dibujarPierna2())

                elif opc.lower() == "s":
                    print("Hasta pronto.")

                elif opc.lower() == "r":
                    os.system('cls')
                    p = Palabra()
                    success=p.reiniciarpalabrasbd()
                    if success==0:
                        input("Lista de palabras vacía, presione enter para agregar más palabras")
                        os.system('cls')
                        opcion='s'
                        while opcion=='s':
                            os.system('cls')
                            palabra = input("Escribe la palabra que deseas añadir y presiona Enter para agregarla\n")
                            success=p.agregarpalabradb(palabra)
                            if success==1:
                                print("Registro exitoso")
                            else:
                                print("Ocurrió un error inténtalo de nuevo "+success)
                            opcion=input("¿Deseas agregar otra palabra? <S> Si || <N> No\n").lower()
                    input("Lista de palabras reiniciada. \nPresiona enter para continuar")
                elif opc.lower()=="v":
                    os.system('cls')
                    print("Jugador\t|Puntos\n")
                    print(j.getjugadoresypbd())
                    input("Presiona Enter para regresar.")
                else:
                    print("Tecla incorrecta. Vuelve a intentarlo.")

                                                            # SIN CONEXION
# ==================================================================================================================================================
            else:
                os.system('cls')
                print("Estás jugando sin conexión.")
                opc = input("Bienvenido "+jugador+" ¿Qué deseas hacer? \n <J> = Jugar || <A> = Añadir Palabra || <R> Reiniciar Palabras || <S> Salir || <V> Ver Jugadores\n ")
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
                        otra=input("¿Deseas agregar otra palabra? <S> Si || <N> No\n").lower()
                    os.system('cls')

                elif opc.lower() == "j":
                    os.system('cls')
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
                                otra=input("¿Deseas agregar otra palabra? <S> Si || <N> No\n").lower()
                    else:
                        palabratyd = p.separarPalabra(success)
                        # p.compararPalabra(palabratyd[1],palabratyd[0])
                        palabraTapada = palabratyd[1]
                        palabraDestapada = palabratyd[0]

                        palabra = ''.join(palabraDestapada)
                        intentos = 5
                        ganador = True
                        dibujo = Dibujo()
                        actual = dibujo.dibujarHorca()

                        while palabraTapada != palabraDestapada:

                            print(actual)
                            print(''.join(palabraDestapada))
                            print(''.join(palabraTapada))
                            print("Tienes " + str(intentos) + " intentos")
                            letraIngresada = input("Escribe una letra o una palabra\n")
                            letraIngresada.lower()

                            if letraIngresada == palabra:
                                palabraTapada = palabraDestapada
                            else:
                                posiciones = [i for i, l in enumerate(palabraDestapada) if l == letraIngresada]
                                if len(posiciones) > 0:
                                    # enumerate(palabraTapada)
                                    for p in posiciones:
                                        palabraTapada[p] = letraIngresada
                                    os.system('cls')
                                    print("Acertaste!")
                                else:
                                    intentos -= 1
                                    if intentos == 4:
                                        os.system('cls')
                                        actual = dibujo.dibujarCabeza()
                                        # print(palabraTapada)
                                    elif intentos == 3:
                                        os.system('cls')
                                        actual = dibujo.dibujarBrazo1()
                                        # print(palabraTapada)
                                    elif intentos == 2:
                                        os.system('cls')
                                        actual = dibujo.dibujarBrazo2()
                                        # print(palabraTapada)
                                    elif intentos == 1:
                                        os.system('cls')
                                        actual = dibujo.dibujarPierna1()
                                        # print(palabraTapada)
                                    elif intentos == 0:
                                        os.system('cls')
                                        palabraTapada = palabraDestapada
                                        ganador = False
                        if ganador:
                            os.system('cls')
                            j.sumarpunto(jugador)
                            input("Adivinaste la palabra. Ganaste!\nPresiona enter para continuar")
                        else:
                            print(dibujo.dibujarPierna2())

                elif opc.lower() == "s":
                    print("Hasta pronto.")

                elif opc.lower() == "r":
                    os.system('cls')
                    p = Palabra()
                    success=p.obtenerPalabras()
                    if success==0:
                        input("Lista de palabras vacía, presione enter para agregar más palabras")
                        os.system('cls')
                        otra='s'
                        while otra == 's':
                            os.system('cls')
                            palabra = input("Escribe la palabra que deseas añadir y presiona Enter para agregarla\n")
                            success = p.añadirPalabra(palabra)
                            if success == 1:
                                print("Palabra añadida exitosamente.")
                            else:
                                print("Ocurrió un error inténtelo de nuevo.")
                            otra = input("¿Deseas agregar otra palabra? <S> Si || <N> No\n").lower()

                    print("Lista de palabras reiniciada.")
                elif opc.lower()=="v":
                    os.system('cls')
                    print("Jugador\t|Puntos\n")
                    print(j.getjugadoresyp())
                    input("Presiona Enter para regresar.")

                else:
                    print("Tecla incorrecta. Vuelve a intentarlo.")


""" menu = Menu()
menu.crearMenu(1) """