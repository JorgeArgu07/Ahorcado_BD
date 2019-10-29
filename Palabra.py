from random import shuffle
from Dibujo import Dibujo
from BD import BD
import mysql.connector
from mysql.connector import Error
import os
class Palabra:
    def llenarbasedatos(self):
        palabras = [line.rstrip() for line in open("Palabras.txt")]
        if len(palabras) == 0:
            self.obtenerPalabras()
            palabras = [line.rstrip() for line in open("Palabras.txt")]
        shuffle(palabras)
        conexion = BD()
        success = conexion.llenarbd(palabras)
        return success

    def agregarpalabradb(self):
        conexion = BD()
        archivopalabras = open("Palabras_todas.txt", "r+")
        otra = "s"
        while otra == "s":
            palabra = input("Escriba la palabra que desea añadir y presione Enter para agregarla\n")
            success = conexion.agregarpalabra(palabra)
            archivopalabras.readlines()
            archivopalabras.write("\n" + palabra.lower())
            if success == 1:
                print("Palabra añadida")
            else:
                print("Ocurrió un error: {}".format(success))
            otra = input("¿Desea añadir otra palabra?(s/n)")
        archivopalabras.close()

    def reiniciarpalabrasbd(self):
            conexion = BD()
            palabras = [line.rstrip() for line in open("Palabras_todas.txt")]
            if len(palabras) == 0:
                print("No se encontraron palabras")
                self.agregarpalabradb()
                palabras = [line.rstrip() for line in open("Palabras_todas.txt")]
            conexion.reiniciarusadas()
            palabras2 = open("Palabras.txt", "w")
            nuevaLista = "\n".join(str(x) for x in palabras)
            palabras2.write(nuevaLista)
            palabras2.close()

    def getpalabrabd(self):
            palabras = []
            conexion = BD()
            for palabra in conexion.getpalabras():
                palabras.append(palabra)
            if len(palabras) == 0:
                self.reiniciarpalabrasbd()
                for palabra in conexion.getpalabras():
                    palabras.append(palabra)
            shuffle(palabras)
            palabra = palabras.pop()
            conexion.cambiarvalidacion(palabra)
            palabras2 = open("Palabras.txt", "w")
            nuevaLista = "\n".join(str(x) for x in palabras)
            palabras2.write(nuevaLista)
            palabras2.close()
            self.separarPalabra(palabra)

    def getPalabra(self):
        palabras=[line.rstrip() for line in open("Palabras.txt")]
        if len(palabras) == 0:
            self.obtenerPalabras()
            palabras=[line.rstrip() for line in open("Palabras.txt")]
        shuffle(palabras)
        palabra = palabras.pop()
        palabras2 = open("Palabras.txt", "w")
        nuevaLista = "\n".join(str(x) for x in palabras)
        palabras2.write(nuevaLista)
        palabras2.close()
        self.separarPalabra(palabra)


    def añadirPalabra(self):
        archivoPalabras = open("Palabras_todas.txt", "r+")
        otra = "s"
        while otra == "s":
            os.system('cls')
            palabra = input("Escriba la palabra que desea añadir y presione Enter para agregarla\n")
            archivoPalabras.readlines()
            archivoPalabras.write("\n"+palabra.lower())
            print("Palabra añadida")
            otra = input("¿Desea añadir otra palabra?(s/n)")
        archivoPalabras.close()


    def obtenerPalabras(self):
        palabras = [line.rstrip() for line in open("Palabras_todas.txt")]
        if len(palabras) == 0:
            print("No se encontraron palabras")
            self.añadirPalabra()
        palabras2 = open("Palabras.txt", "w")
        nuevaLista = "\n".join(str(x) for x in palabras)
        palabras2.write(nuevaLista)
        palabras2.close()

    def separarPalabra(self, palabra):
        palabraDestapada = list(palabra)
        palabraTapada = []

        for letra in palabraDestapada:
            palabraTapada.append(" _")


        self.compararPalabra(palabraTapada, palabraDestapada)



    def compararPalabra(self, palabraTapada, palabraDestapada):

        os.system('cls')
        palabra = self.concatLista(palabraDestapada)
        intentos = 5
        ganador = True

        dibujo = Dibujo()
        actual = dibujo.dibujarHorca()

        while self.concatLista(palabraTapada) != self.concatLista(palabraDestapada):

            actual

            print(self.concatLista(palabraDestapada))
            print(self.concatLista(palabraTapada))
            print("Tienes "+str(intentos)+" intentos")
            letraIngresada = input("Escribe una letra o una palabra\n")
            letraIngresada.lower()

            if letraIngresada == palabra:
                palabraTapada = palabra
            else:
                posiciones = [i for i,l in enumerate(palabraDestapada) if l == letraIngresada]
                if len(posiciones) > 0 :
                    #enumerate(palabraTapada)
                    for p in posiciones:
                        palabraTapada[p] = letraIngresada
                    os.system('cls')
                    print("Acertaste!")


                else:
                    intentos -= 1
                    if intentos == 4:
                        os.system('cls')
                        actual = dibujo.dibujarCabeza()
                        #print(palabraTapada)
                    elif intentos == 3:
                        os.system('cls')
                        actual = dibujo.dibujarBrazo1()
                        #print(palabraTapada)
                    elif intentos == 2:
                        os.system('cls')
                        actual = dibujo.dibujarBrazo2()
                        #print(palabraTapada)
                    elif intentos == 1:
                        os.system('cls')
                        actual = dibujo.dibujarPierna1()
                        #print(palabraTapada)
                    elif intentos == 0:
                        os.system('cls')
                        palabraTapada = palabraDestapada
                        ganador = False


        if ganador:
            print("Adivinaste la palabra. Ganaste!")
        else:
            dibujo.dibujarPierna2()


    def concatLista(self, lista):
        palabra = ""
        for l in lista:
            palabra+= l
        return palabra


pa=Palabra()
pa.getpalabrabd()