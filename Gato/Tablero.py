class Tablero:

	
	tablero = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]	

	def setPosicion(pos, ficha):
		length = len(Tablero.tablero)

		for f in range(length):
			if  pos == Tablero.tablero[f]:
				if Tablero.tablero[f] != "O" and Tablero.tablero[f] != "X":
					Tablero.tablero[f] = ficha
				else:
					print("Posicion invalida")
					

	def dibujarTablero():
		tab = "╔═══╦═══╦═══╗\n"+"║ "+Tablero.tablero[0]+" ║ "+Tablero.tablero[1]+" ║ "+Tablero.tablero[2]+" ║\n"+"╠═══╬═══╬═══╣\n"+"║ "+Tablero.tablero[3]+" ║ "+Tablero.tablero[4]+" ║ "+Tablero.tablero[5]+" ║\n"+"╠═══╬═══╬═══╣\n"+"║ "+Tablero.tablero[6]+" ║ "+Tablero.tablero[7]+" ║ "+Tablero.tablero[8]+" ║\n"+"╚═══╩═══╩═══╝\n"
		return tab

	def verificar(ficha):
		tablero = Tablero.tablero 
		return ((tablero[0] == ficha and tablero[1] == ficha and tablero[2] == ficha) or # across the top
		(tablero[3] == ficha and tablero[4] == ficha and tablero[5] == ficha) or # across the middle
		(tablero[6] == ficha and tablero[7] == ficha and tablero[8] == ficha) or # across the bottom
		(tablero[2] == ficha and tablero[5] == ficha and tablero[8] == ficha) or # down the left side
		(tablero[1] == ficha and tablero[4] == ficha and tablero[7] == ficha) or # down the middle
		(tablero[0] == ficha and tablero[3] == ficha and tablero[6] == ficha) or # down the right side
		(tablero[0] == ficha and tablero[4] == ficha and tablero[8] == ficha) or # diagonal
		(tablero[2] == ficha and tablero[4] == ficha and tablero[6] == ficha))
