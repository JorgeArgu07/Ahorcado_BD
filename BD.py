import mysql.connector
from mysql.connector import Error


class BD:

    def execquery(self, query):
        success=0
        er=""
        try:
            conexion = mysql.connector.connect(host="localhost", user="root", passwd="", db="ahorcado_BD")
            cursor = conexion.cursor()
            cursor.execute(query)
            conexion.commit()
            cursor.close()
            success = 1
        except Error as error:
            er = error
            success = 0
        finally:
            if success != 1:
                return er
            else:
                return success
    
    def getselect(self,query):
        er = ""
        success = 0
        try:
            conexion=mysql.connector.connect(host="localhost",user="root",passwd="", db="ahorcado_BD")
            cursor = conexion.cursor()
            cursor.execute(query)
            consulta = cursor.fetchall()
            cursor.close()
            success = 1
        except Error as error:
            success=0
            er = error
        finally:
            if success != 1:
                return er
            else:
                return consulta

    def llenarbd(self, palabras):
        success = 0
        eliminarbd = "truncate table ahorcado_bd.palabras;"
        success=self.execquery(eliminarbd)
        if success!=1:
            return success
        else:
            for palabra in palabras:
                success=self.execquery(query = "insert into palabras (palabra) values('"+palabra+"')")
        return success

    def agregarpalabra(self, palabra):
        success = 0
        query = "insert into palabras (palabra) values('" + palabra + "')"
        success=self.execquery(query)
        return success

    def reiniciarusadas(self):
        success = 0
        obtenerids="select id from ahorcado_bd.palabras"
        for i in self.getselect(obtenerids):
            success=self.execquery(query="UPDATE palabras SET validacion = 0 WHERE id ={}".format(i[0]))
        return success

    def getpalabras(self):
        palabras = []
        success = 0
        obtenerpalabras="select * from palabras where validacion = 0"
        for row in self.getselect(obtenerpalabras):
            palabras.append(row[1])
        if len(palabras)==0:
            success=0
        else:
            success=1
        return palabras

    def cambiarvalidacion(self, palabra):
        success = 0
        identificador = 0
        getid="select id from ahorcado_bd.palabras where palabra ='"+palabra+"'"
        for row in self.getselect(getid):
            identificador=row[0]
        query = "UPDATE palabras SET validacion = 1 WHERE id ={}".format(identificador)
        success=self.execquery(query)
        return success

    def getjugadores(self):
        jugadores=[]
        query="select * from jugadores"
        jugadores=list(self.getselect(query))
        return jugadores
    
    def verifyjugador(self, jugador):
        query="select * from jugadores where idjugador like('%"+jugador+"%') limit 1"
        if len(self.getselect(query))==0:
            return 0
        else:
            jugador=list(self.getselect(query))
            return jugador[0][0]

    def verifypuntosjugador(self, jugador):
        query="select * from jugadores where idjugador like('%"+jugador+"%') limit 1"
        if len(self.getselect(query))==0:
            return 0
        else:
            jugador=list(self.getselect(query))
            return jugador[0][1]
    
    def agregarjugador(self, nombre):
        query="insert into jugadores (idjugador) values('"+nombre+"')"
        success=self.execquery(query)
        return success

    def sumarpuntos(self, jugador):
        query = "UPDATE jugadores SET puntaje = puntaje+1 WHERE idjugador='"+jugador+"';"
        success=self.execquery(query)
        return success

    def llenarjugadores(self, jugadores):
        success=0
        eliminarbd = "truncate table ahorcado_bd.jugadores;"
        success=self.execquery(eliminarbd)
        for jugador in range(len(jugadores)):
            success=self.execquery(query="insert into jugadores (idjugador, puntaje) values('"+jugadores[jugador][0]+"','"+jugadores[jugador][1]+"')")
        return success

    def getjugadoresyp(self):
        query="select * from jugadores"
        jugadores=[]
        if len(self.getselect(query))==0:
            return 0
        else:
            jugadores = list(self.getselect(query))
        return jugadores