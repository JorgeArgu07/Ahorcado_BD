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

    def getpalabras(self):
        palabras = []
        success = 0
        er = ""
        try:
            conexion=mysql.connector.connect(host="localhost", user="root", passwd="", db="ahorcado_BD")
            cursor = conexion.cursor()
            cursor.execute("select * from palabras where validacion = 0")
            consulta = cursor.fetchall()
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
                print("Ocurrió un error: {}".format(er))

    def conectar(self):
        success = 0
        er = ""
        try:
            conexion = mysql.connector.connect(host="localhost", user="root", passwd="", db="ahorcado_BD")
            success = 1
        except Error as error:
            er = error
            success = 0
        finally:
            if success != 1:
                return er
            else:
                return success

    def cambiarvalidacion2(self, identificador):
        success = 0
        er = ""
        try:
            conexion = mysql.connector.connect(host="localhost", user="root", passwd="", db="ahorcado_BD")
            query = "update ahorcado_bd.palabras set validacion=1 where id='"+identificador+"'"
            cursor = conexion.cursor()
            cursor.execute(query)
            success = 1
        except Error as error:
            print("hola", success, er)
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
            # print(identificador)
            self.cambiarvalidacion2(identificador)
            success = 1
        except Error as error:
            print("hola", success, er)
            success = 0
        finally:
            if success != 1:
                return er
            else:
                return success


bd = BD()
bd.cambiarvalidacion2(7)

