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

    def agregarpalabradb(self, palabra):
        conexion = BD()
        archivopalabras = open("Palabras_todas.txt", "r+")
        success = conexion.agregarpalabra(palabra)
        archivopalabras.readlines()
        archivopalabras.write("\n" + palabra.lower())
        if success == 1:
            return 1
        else:
            return success
        archivopalabras.close()

    def reiniciarpalabrasbd(self):
            conexion = BD()
            palabras = [line.rstrip() for line in open("Palabras_todas.txt")]
            if len(palabras) == 0:
                return 0
            conexion.reiniciarusadas()
            palabras2 = open("Palabras.txt", "w")
            nuevaLista = "\n".join(str(x) for x in palabras)
            palabras2.write(nuevaLista)
            palabras2.close()
            return 1

    def getpalabrabd(self):
            palabras = []
            conexion = BD()
            for palabra in conexion.getpalabras():
                palabras.append(palabra)
            if len(palabras) == 0:
                if self.reiniciarpalabrasbd()==0:
                    return 0
                for palabra in conexion.getpalabras():
                    palabras.append(palabra)
            shuffle(palabras)
            palabra = palabras.pop()
            conexion.cambiarvalidacion(palabra)
            palabras2 = open("Palabras.txt", "w")
            nuevaLista = "\n".join(str(x) for x in palabras)
            palabras2.write(nuevaLista)
            palabras2.close()
            return palabra

    def getPalabra(self):
        palabras=[line.rstrip() for line in open("Palabras.txt")]
        if len(palabras) == 0:
            return 0
        shuffle(palabras)
        palabra = palabras.pop()
        palabras2 = open("Palabras.txt", "w")
        nuevaLista = "\n".join(str(x) for x in palabras)
        palabras2.write(nuevaLista)
        palabras2.close()
        return palabra


    def añadirPalabra(self,palabra):
        archivoPalabras = open("Palabras_todas.txt", "r+")
        os.system('cls')
        archivoPalabras.readlines()
        archivoPalabras.write("\n"+palabra.lower())
        archivoPalabras.close()
        return 1


    def obtenerPalabras(self):
        palabras = [line.rstrip() for line in open("Palabras_todas.txt")]
        if len(palabras) == 0:
            return 0
        palabras2 = open("Palabras.txt", "w")
        nuevaLista = "\n".join(str(x) for x in palabras)
        palabras2.write(nuevaLista)
        palabras2.close()
        return 1

    def separarPalabra(self, palabra):
        palabraDestapada = list(palabra)
        palabraTapada = []
        output=[]

        for letra in palabraDestapada:
            palabraTapada.append(" _")

        output.append(palabraDestapada)
        output.append(palabraTapada)
        return output

    # def compararPalabra(self, palabraTapada, palabraDestapada):


    def concatLista(self, lista):
        palabra = ""
        for l in lista:
            palabra+= l
        return palabra
