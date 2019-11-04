class Tablero:
	

	def __init__(self):
		self.tablero = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

	def setPosicion(self, pos, ficha):
		length = len(self.tablero)

		for f in range(length):
			if pos == self.tablero[f]:
				if self.tablero[f] != "O" and self.tablero[f] != "X":
					self.tablero[f] = ficha


	def dibujarTablero(self):
		tab = "╔═══╦═══╦═══╗\n"+\
			  "║ "+self.tablero[0]+" ║ "+self.tablero[1]+" ║ "+self.tablero[2]+" ║\n"+\
			  "╠═══╬═══╬═══╣\n"+\
			  "║ "+self.tablero[3]+" ║ "+self.tablero[4]+" ║ "+self.tablero[5]+" ║\n"+\
			  "╠═══╬═══╬═══╣\n"+\
			  "║ "+self.tablero[6]+" ║ "+self.tablero[7]+" ║ "+self.tablero[8]+" ║\n"+\
			  "╚═══╩═══╩═══╝\n"
		return tab

	def verificarGanador(self, ficha):
		tablero = self.tablero
		return ((tablero[0] == ficha and tablero[1] == ficha and tablero[2] == ficha) or
		(tablero[3] == ficha and tablero[4] == ficha and tablero[5] == ficha) or
		(tablero[6] == ficha and tablero[7] == ficha and tablero[8] == ficha) or
		(tablero[2] == ficha and tablero[5] == ficha and tablero[8] == ficha) or
		(tablero[1] == ficha and tablero[4] == ficha and tablero[7] == ficha) or
		(tablero[0] == ficha and tablero[3] == ficha and tablero[6] == ficha) or
		(tablero[0] == ficha and tablero[4] == ficha and tablero[8] == ficha) or
		(tablero[2] == ficha and tablero[4] == ficha and tablero[6] == ficha))

	def resetTablero(self):
		self.tablero = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

	def verificarEmpate(self):
		tablero = self.tablero
		return ((tablero[0] == "O" or tablero[0] == "X") and (tablero[1] == "O" or tablero[1] == "X") and
				(tablero[2] == "O" or tablero[2] == "X") and (tablero[3] == "O" or tablero[3] == "X") and
				(tablero[4] == "O" or tablero[4] == "X") and (tablero[5] == "O" or tablero[5] == "X") and
				(tablero[6] == "O" or tablero[6] == "X") and (tablero[7] == "O" or tablero[7] == "X") and
				(tablero[8] == "O" or tablero[8] == "X"))



