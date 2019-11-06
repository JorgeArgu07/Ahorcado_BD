from Palabra import Palabra

import msvcrt
import os

class Juego:

    objpalabra = Palabra()

    def juegonuevo(self):

        opc1 = input("¿Iniciar juego nuevo? (s/n), puedes agregar otra palabra (a) o "
                                                "reiniciar la lista de palabras (r)").lower()
        if opc1 == 's':
            self.objpalabra.llenararchivo()
            return self.jugar()
        elif opc1 == 'a':
            os.system('cls')
            palabra = input("Escribe la palabra que quieres añadir:").lower()
            self.objpalabra.agregarpalabra(palabra)
            self.objpalabra.llenararchivo()
            return self.jugar()
        elif opc1 == "r":
            os.system('cls')
            self.objpalabra.llenararchivo()
        elif opc1 == 'n':
            print("OK, bye")
            msvcrt.getch()
        os.system('cls')

    def jugar(self):
        opc = "s"
        while opc == "s" or opc == "a" or opc == "r":
            os.system('cls')
            intentos = 6
            if not self.objpalabra.obtenerpalabras():
                print("No hay palabras")
                return self.juegonuevo()
            else:
                palabraenjuego = self.objpalabra.obtenerarreglopalabra()
                longitudpalabra=len(palabraenjuego)
                palabraposiciones = []
                for letra in palabraenjuego:
                    palabraposiciones.append(letra)
                arreglovacio = []
                for letra in range(longitudpalabra):
                    arreglovacio.append("_")
                pal = ""
                for char in palabraenjuego:
                    pal += char
                print(palabraenjuego)
                while intentos > 0:
                    if not palabraenjuego:
                        print("¡Descubriste la palabra! es: "+pal)
                        opc = input("¿Quieres obtener otra palabra? (s/n)), puedes agregar otra palabra (a) o "
                                                "reiniciar la lista de palabras (r)").lower()
                        if opc == "a":
                            os.system('cls')
                            palabra = input("Escribe la palabra que quieres añadir:").lower()
                            self.objpalabra.agregarpalabra(palabra)
                        elif opc=="r":
                            os.system('cls')
                            self.objpalabra.llenararchivo()
                        intentos = 0
                    else:
                        if intentos == 6:
                            print(self.horca())
                        elif intentos == 5:
                            print(self.cabeza())
                        elif intentos == 4:
                            print(self.cuerpo())
                        elif intentos == 3:
                            print(self.brazoder())
                        elif intentos == 2:
                            print(self.brazoizq())
                        elif intentos == 1:
                            print(self.piernader())
                        print(arreglovacio)
                        respuesta = input("Escribe una letra que creas que está en la palabra, ó escribe la palabra completa").lower()

                        if respuesta == pal:
                            print("¡Ganaste! la palabra es: "+pal)
                            opc = input("¿Quieres obtener otra palabra? (s/n)), puedes agregar otra palabra (a) o "
                                                "reiniciar la lista de palabras (r)").lower()
                            if opc == "a":
                                os.system('cls')
                                palabra = input("Escribe la palabra que quieres añadir:").lower()
                                self.objpalabra.agregarpalabra(palabra)
                            elif opc == "r":
                                os.system('cls')
                                self.objpalabra.llenararchivo()
                            intentos = 0
                        else:
                            result = respuesta in palabraenjuego
                            if result:
                                for index, letra in enumerate(palabraposiciones):
                                    if letra == respuesta:
                                        arreglovacio[index] = letra

                                for letra in palabraenjuego:
                                    if letra == respuesta:
                                        palabraenjuego.remove(letra)
                                print("La palabra sí contenía esa letra")
                                os.system('cls')
                            else:
                                if intentos == 1:
                                    os.system('cls')
                                    print(self.piernaizq())
                                    opc = input("¡Perdiste! ¿quieres obtener otra palabra? (s/n), puedes agregar otra palabra (a) o "
                                                "reiniciar la lista de palabras (r)").lower()
                                    if opc == "a":
                                        os.system('cls')
                                        palabra = input("Escribe la palabra que quieres añadir:").lower()
                                        self.objpalabra.agregarpalabra(palabra)
                                        intentos = 6
                                    elif opc == "r":
                                        os.system('cls')
                                        self.objpalabra.llenararchivo()
                                        intentos = 6
                                    elif opc == "n":
                                        intentos = -1
                                    elif opc == "s":
                                        intentos = -1
                                else:
                                    os.system('cls')
                                    intentos = intentos - 1
                                    print("La palabra no contiene la letra "+respuesta + " tienes " + str(intentos)+" intentos")
                                    opc = "n"
        print("ok, bye")

    def horca(self):
        var = "       +------------+ \n" \
            "         |            | \n" \
            "                      | \n" \
            "                      | \n" \
            "                      | \n" \
            "                      | \n" \
            "                      | \n" \
            "                      | \n" \
            "======================= \n"
        return var

    def cabeza(self):
        var = "         +------------+ \n" \
              "         |            | \n" \
              "         O            | \n" \
              "                      | \n" \
              "                      | \n" \
              "                      | \n" \
              "                      | \n" \
              "                      | \n" \
              "======================= \n"
        return var

    def cuerpo(self):
        var = "         +------------+ \n" \
              "         |            | \n" \
              "         O            | \n" \
              "         |            | \n" \
              "                      | \n" \
              "                      | \n" \
              "                      | \n" \
              "                      | \n" \
              "======================= \n"
        return var

    def brazoder(self):
        var = "         +------------+ \n" \
              "         |            | \n" \
              "         O            | \n" \
              "        /|            | \n" \
              "                      | \n" \
              "                      | \n" \
              "                      | \n" \
              "                      | \n" \
              "======================= \n"
        return var

    def brazoizq(self):
        var = "         +------------+ \n" \
              "         |            | \n" \
              "         O            | \n" \
              "        /|\           | \n" \
              "                      | \n" \
              "                      | \n" \
              "                      | \n" \
              "                      | \n" \
              "======================= \n"
        return var

    def piernader(self):
        var = "         +------------+ \n" \
              "         |            | \n" \
              "         O            | \n" \
              "        /|\           | \n" \
              "        /             | \n" \
              "                      | \n" \
              "                      | \n" \
              "                      | \n" \
              "======================= \n"
        return var

    def piernaizq(self):
        var = "         +------------+ \n" \
              "         |            | \n" \
              "         O            | \n" \
              "        /|\           | \n" \
              "        / \           | \n" \
              "                      | \n" \
              "                      | \n" \
              "                      | \n" \
              "======================= \n"
        return var


# juego = Juego()
#
# juego.horca()
# juego.cabeza()
# juego.brazoder()
# juego.brazoizq()
# juego.piernader()
# juego.piernaizq()
