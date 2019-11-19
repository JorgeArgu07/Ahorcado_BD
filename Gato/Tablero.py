import pygame,sys
from pygame.locals import *
from Button import Button
class Tablero:
	

	def __init__(self):
		#self.tablero = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
		colorGris = (225, 225, 225)
		x, y = 50, 50
		width = 50
		height = 50
		btn1 = Button(colorGris, x + 60, y, width, height, "1")
		btn2 = Button(colorGris, x + 120, y, width, height, "2")
		btn3 = Button(colorGris, x + 180, y, width, height, "3")
		btn4 = Button(colorGris, x + 60, y + 60, width, height, "4")
		btn5 = Button(colorGris, x + 120, y + 60, width, height, "5")
		btn6 = Button(colorGris, x + 180, y + 60, width, height, "6")
		btn7 = Button(colorGris, x + 60, y + 120, width, height, "7")
		btn8 = Button(colorGris, x + 120, y + 120, width, height, "8")
		btn9 = Button(colorGris, x + 180, y + 120, width, height, "9")

		self.botones = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]

	def setPosicion(self, pos, ficha):
		length = len(self.botones)

		for f in range(length):
			if pos == self.botones[f].text:
				if self.botones[f].text != "O" and self.botones[f].text != "X":
					self.botones[f].text = ficha

		if ficha == "O":
			for f in range(length):
				if pos == self.botones[f].text:
					if self.botones[f].text != "O" and self.botones[f].text != "X":
						self.botones[f].text = ficha




	def dibujarTablero(self, display):
		# tab = "╔═══╦═══╦═══╗\n"+\
		# 	  "║ "+self.tablero[0]+" ║ "+self.tablero[1]+" ║ "+self.tablero[2]+" ║\n"+\
		# 	  "╠═══╬═══╬═══╣\n"+\
		# 	  "║ "+self.tablero[3]+" ║ "+self.tablero[4]+" ║ "+self.tablero[5]+" ║\n"+\
		# 	  "╠═══╬═══╬═══╣\n"+\
		# 	  "║ "+self.tablero[6]+" ║ "+self.tablero[7]+" ║ "+self.tablero[8]+" ║\n"+\
		# 	  "╚═══╩═══╩═══╝\n"
		# return tab

		self.botones[0].draw(display)
		self.botones[1].draw(display)
		self.botones[2].draw(display)
		self.botones[3].draw(display)
		self.botones[4].draw(display)
		self.botones[5].draw(display)
		self.botones[6].draw(display)
		self.botones[7].draw(display)
		self.botones[8].draw(display)

		return self.botones



	def verificarGanador(self, ficha):
		tablero = self.botones
		return ((tablero[0].text == ficha and tablero[1].text == ficha and tablero[2].text == ficha) or
		(tablero[3].text == ficha and tablero[4].text == ficha and tablero[5].text == ficha) or
		(tablero[6].text == ficha and tablero[7].text == ficha and tablero[8].text == ficha) or
		(tablero[2].text == ficha and tablero[5].text == ficha and tablero[8].text == ficha) or
		(tablero[1].text == ficha and tablero[4].text == ficha and tablero[7].text == ficha) or
		(tablero[0].text == ficha and tablero[3].text == ficha and tablero[6].text == ficha) or
		(tablero[0].text == ficha and tablero[4].text == ficha and tablero[8].text == ficha) or
		(tablero[2].text == ficha and tablero[4].text == ficha and tablero[6].text == ficha))

	def resetTablero(self):

		i = 0
		for boton in self.botones:
			boton.text = str(i)
			i += 1
	def verificarEmpate(self):
		tablero = self.botones
		return ((tablero[0].text == "O" or tablero[0].text == "X") and (tablero[1].text == "O" or tablero[1].text == "X") and
				(tablero[2].text == "O" or tablero[2].text == "X") and (tablero[3].text == "O" or tablero[3].text == "X") and
				(tablero[4].text == "O" or tablero[4].text == "X") and (tablero[5].text == "O" or tablero[5].text == "X") and
				(tablero[6].text == "O" or tablero[6].text == "X") and (tablero[7].text == "O" or tablero[7].text == "X") and
				(tablero[8].text == "O" or tablero[8].text == "X"))