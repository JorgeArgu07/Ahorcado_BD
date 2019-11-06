from BD import BD

class Jugador:
    

    def getnombresjugadoresbd(self):
        conexion=BD()
        jugadoresbd=list(conexion.getjugadores())
        nombresjugbd=[]
        for row in range(len(jugadoresbd)):
            nombresjugbd.append(jugadoresbd[row][0])
        return nombresjugbd

    def verifypuntosjugadorbd(self,jugador):
        conexion=BD()
        return conexion.verifypuntosjugador(jugador)
    
    def verifyjugadorbd(self, jugador):
        conexion=BD()
        return conexion.verifyjugador(jugador)

    def sumarpuntobd(self,jugador):
        conexion=BD()
        return conexion.sumarpuntos(jugador)

    def agregarjugadorbd(self,nombre):
        conexion=BD()
        return conexion.agregarjugador(nombre)

    def getnombresjugadores(self):
        jugadoryp=[]
        nombres=[]
        jugadores = [line.rstrip() for line in open("jugadores.txt")]
        for jugador in range(len(jugadores)):
            jugadoryp.append(jugadores[jugador].split())

        for nomjugador in range(len(jugadoryp)):
            nombres.append(jugadoryp[nomjugador][0])

        return nombres

    def getpuntajejugadores(self):
        jugadoryp=[]
        puntajes=[]
        jugadores = [line.rstrip() for line in open("jugadores.txt")]
        for jugador in range(len(jugadores)):
            jugadoryp.append(jugadores[jugador].split())

        for nomjugador in range(len(jugadoryp)):
            puntajes.append(jugadoryp[nomjugador][1])

        return puntajes
    
    def verifyjugador(self, jugador):
        if jugador in self.getnombresjugadores():
            return jugador
        else:
            return 0

    def verifypuntosjugador(self, jugador):
        pos=self.getnombresjugadores().index(jugador)
        puntos=self.getpuntajejugadores()[pos]
        return puntos

    def getjugadoresyp(self):
        jugadoryp=[]
        var=""
        jugadores = [line.rstrip() for line in open("jugadores.txt")]
        for jugador in range(len(jugadores)):
            jugadoryp.append(jugadores[jugador].split())
        for jugador in range(len(jugadoryp)):
            var+=jugadoryp[jugador][0]+"\t"+jugadoryp[jugador][1]+"\n"
        return var

    def agregarjugador(self, jugador):
        archivojugadores = open("jugadores.txt", "r+")
        archivojugadores.readlines()
        archivojugadores.write("\n"+jugador.lower()+"\t0")
        archivojugadores.close()
        return 1
    
    def getjugadoresypbd(self):
        conexion=BD()
        return conexion.getjugadoresyp()

    def sumarpunto(self,jugador):
        jugadoryp=[]
        var=""
        pos=self.getnombresjugadores().index(jugador)
        puntos=int(self.getpuntajejugadores()[pos])
        puntos+=1
        jugadores = [line.rstrip() for line in open("jugadores.txt")]
        for jug in range(len(jugadores)):
            jugadoryp.append(jugadores[jug].split())
        jugadoryp[pos][0]=jugador
        jugadoryp[pos][1]=puntos
        for linea in range(len(jugadoryp)):
            if linea==0:
                var+=jugadoryp[linea][0]+"\t"+str(jugadoryp[linea][1])
            else:
                var+="\n"+jugadoryp[linea][0]+"\t"+str(jugadoryp[linea][1])
        archivojugadores = open("jugadores.txt", "w")
        for linea in var:
            archivojugadores.write(linea)
        archivojugadores.close()
        return 1      

""" Ju=Jugador()
Ju.sumarpunto("jorge") """