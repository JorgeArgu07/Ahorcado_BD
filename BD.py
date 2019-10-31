import mysql.connector
from mysql.connector import Error


class BD:

    def llenarbd(self, palabras):
        success = 0
        er = ""
        eliminarbd = "truncate table ahorcado_bd.palabras;"
        try:
            conexion = mysql.connector.connect(host="localhost", user="root", passwd="", db="ahorcado_BD")
            cursor = conexion.cursor()
            cursor.execute(eliminarbd)
            for palabra in palabras:
                query = "insert into palabras (palabra) values('"+palabra+"')"
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

    def agregarpalabra(self, palabra):
        success = 0
        er = ""
        try:
            conexion = mysql.connector.connect(host="localhost", user="root", passwd="", db="ahorcado_BD")
            query = "insert into palabras (palabra) values('" + palabra + "')"
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

    def reiniciarusadas(self):
        success = 0
        er = ""
        try:
            conexion=mysql.connector.connect(host="localhost",user="root",passwd="", db="ahorcado_BD")
            cursor = conexion.cursor()
            cursor.execute("select id from ahorcado_bd.palabras")
            consulta = cursor.fetchall()
            for i in consulta:
                cursor.execute("UPDATE palabras SET validacion = 0 WHERE id ={}".format(i[0]))
            conexion.commit()

        except Error as error:
            success = 0
            er = error
        finally:
            if success != 1:
                return er
            else:
                return success

    def getpalabras(self):
        palabras = []
        success = 0
        er = ""
        try:
            conexion=mysql.connector.connect(host="localhost", user="root", passwd="", db="ahorcado_BD")
            cursor = conexion.cursor()
            cursor.execute("select * from palabras where validacion = 0")
            consulta = cursor.fetchall()
            if len(consulta) == 0:
                success = 0
            else:
                for row in consulta:
                    palabras.append(row[1])
                success = 1
        except Error as e:
            success = 0
            er = e
        finally:
            if success == 1:
                return palabras
            else:
                return er

    def validacionaux(self, identificador):
        success = 0
        er = ""
        try:
            conexion = mysql.connector.connect(host="localhost", user="root", passwd="", db="ahorcado_BD")
            cursor = conexion.cursor()
            query = "UPDATE palabras SET validacion = 1 WHERE id ={}".format(identificador)
            cursor.execute(query)
            conexion.commit()
            success = 1
        except Error as error:
            er = error
            success = 0
        finally:
            if success != 1:
                return er
            else:
                return success

    def cambiarvalidacion(self, palabra):
        success = 0
        er = ""
        try:
            conexion = mysql.connector.connect(host ="localhost", user="root", passwd="", db="ahorcado_BD")
            query = "select id from ahorcado_bd.palabras where palabra ='"+palabra+"'"
            cursor = conexion.cursor()
            cursor.execute(query)
            consulta = cursor.fetchall()
            identificador = 0
            for row in consulta:
                identificador = row[0]
            self.validacionaux(identificador)
            success = 1
        except Error as error:
            er = error
            success = 0
        finally:
            if success != 1:
                return er
            else:
                return success