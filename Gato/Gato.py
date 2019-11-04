class Gato:

	def Jugar(tablero, j1, j2, reset):
		ganador = 0

		while reset == "s":
			while ganador == 0:

				ganador = Gato.Turno(ganador, turno, tablero, j1, j2)

			reset = input("Deseas volver a jugar?(s/n)\n")
			reset.lower()
			if reset == "s":
				ganador = 0

	def verificarGanador(tablero, j, turno):
		pos = input("Turno de "+j.getNombre()+" ("+j.getFicha()+")\n")
		tablero.setPosicion(pos, j.getFicha())
				
		if tablero.verificar(j.getFicha()):
			ganador = 1
			tab = tablero.dibujarTablero()+"\n Ganador!!"
			tablero.resetTablero()
		
		return 0
			

	def Turno(ganador, tablero, j1, j2):
		if turno == 1:
			Gato.verificarGanador(tablero, j1, turno)

		else:
			Gato.verficarGanador(tablero, j2, turno)
