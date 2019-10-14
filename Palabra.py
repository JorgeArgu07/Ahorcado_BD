from random import shuffle
from Dibujo import Dibujo
from BD import BD
import os
class Palabra:

	def getpalabrasarchivo(self):
		palabras = [line.rstrip() for line in open("Palabras.txt")]
		if len(palabras) == 0:
			self.obtenerPalabras()
			palabras = [line.rstrip() for line in open("Palabras.txt")]
		shuffle(palabras)
		return palabras

	def getPalabra(self, conexion):

		if conexion.is_connected:
			palabrasbd=[]


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

	def añadirPalabra(self, conexion):
		archivoPalabras = open("Palabras_todas.txt", "r+")
		otra = "s"
		while otra == "s":
			palabra = input("Escriba la palabra que desea añadir y presione Enter para agregarla\n")

			if conexion.is_connected():
				cursor = conexion.cursor()
				cursor.execute("insert into palabras(palabra) values('"+palabra+"') ")
				conexion.commit()
				cursor.close()
				conexion.close()
			else:
				archivoPalabras.readlines()
				archivoPalabras.write("\n"+palabra.lower())
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
		palabra = self.concatLista(palabraDestapada)
		intentos = 5
		ganador = True

		while self.concatLista(palabraTapada) != self.concatLista(palabraDestapada):

			os.system('cls')
			print(self.concatLista(palabraDestapada))

			dibujo = Dibujo()

			dibujo.dibujarHorca()
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
					print("Acertaste!")
				else:
					intentos -= 1
					if intentos == 4:
						dibujo.dibujarCabeza()
						print(palabraTapada)
					elif intentos == 3:
						dibujo.dibujarBrazo1()
						print(palabraTapada)
					elif intentos == 2:
						dibujo.dibujarBrazo2()
						print(palabraTapada)
					elif intentos == 1:
						dibujo.dibujarPierna1()
						print(palabraTapada)
					elif intentos == 0:
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








		
			








