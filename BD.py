import mysql.connector
from mysql.connector import Error
class BD:

	#def conectar(self):
	#	try:
	#		conexion = mysql.connector.connect(host="localhost", user="root", passwd="", db="ahorcado_BD")
	#		if conexion.is_connected():
	#			info = conexion.get_server_info()
	#			print ("Conectado a la version de MySQL: ", info)
	#			cursor = conexion.cursor()
	#			cursor.execute("select database();")
	#			record = cursor.fetchone()
	#			print("Conectado a la base de datos: ", record)
	#			cursor.execute("select * from Jugadores")
	#			consulta = cursor.fetchall()
	#			for row in consulta:
	#				print("Id: ", row[0])
	#				print("Nombre: ", row[1])
	#				print("Puntuacion: ", row[2])
	#	except Error as e:
	#		print("Error al conectar a MySQL", e)
#
#		finally:
#			if(conexion.is_connected()):
#				cursor.close()
#				conexion.close()
#				print("La conexion a MySQL se ha cerrado"

	def conectar(self):
		try:
			conexion = mysql.connector.connect(host="localhost", user="root", passwd="", db="ahorcado_BD")
			return conexion
		
					
		except Error as e:


			print("Error al conectar a MySQL", e)
			return False


		finally:
			print("")
			
		




		


