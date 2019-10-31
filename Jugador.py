

class Jugador:
    

    def getnombresjugadores(self):
        jugadoryp=[]
        nombres=[]
        jugadores = [line.rstrip() for line in open("jugadores.txt")]
        for jugador in range(len(jugadores)):
            jugadoryp.append(jugadores[jugador].split())

        for nomjugador in range(len(jugadoryp)):
            nombres.append(jugadoryp[nomjugador][0])

        return nombres



""" Ju=Jugador()
Ju.getjugadoresarchivo() """