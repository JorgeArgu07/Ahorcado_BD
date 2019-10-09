from Palabra import Palabra
import os
class Menu:

    def crearMenu(self):

        opc = "a"
        while opc != "s":

            
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

            


            
        





            







