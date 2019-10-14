from random import shuffle
from Dibujo import Dibujo
import mysql.connector
from mysql.connector import Error
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


	def añadirPalabra(self):
		archivoPalabras = open("Palabras_todas.txt", "r+")
		otra = "s"
		while otra == "s":
			palabra = input("Escriba la palabra que desea añadir y presione Enter para agregarla\n")
			try:
				conexion = mysql.connector.connect(host="localhost", user="root", passwd="", db="ahorcado_BD")
				cursor = conexion.cursor()
				cursor.execute("insert into palabras(palabra) values('"+palabra+"') ")
				conexion.commit()
				cursor.close()
				conexion.close()	
				archivoPalabras.readlines()
				archivoPalabras.write("\n"+palabra.lower())
	
			except Error as e:
				archivoPalabras.readlines()
				archivoPalabras.write("\n"+palabra.lower())
				print("Error al conectar a MySQL", e)

			finally:
				print("Palabra añadida")
			otra = input ("¿Desea añadir otra palabra?(s/n)")

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
					actual
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








		
			








