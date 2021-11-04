#Importamos o conector MySQL para que este script poida comunicarse co server MySQL que instalamos previamente
import mysql.connector
import sys
print('¡Hola, Bienvenido a Password Manager!')
MasterUser = ''
MasterContra = ''
MasterTable = ''
#Bucle para non permitir que as variables estén vacías
while (MasterUser and MasterContra and MasterTable ) == '':
	MasterUser = input("Introduzca el nombre de usuario de la BBDD [Base de Datos] \n")
	MasterContra = input("Introduzca la contraseña del usuario de la BBDD [Base de Datos] \n")
	MasterTable = input("Introduzca el nombre que tiene / va a tener la tabla donde se guardará sus contraseñas  \n")
	#MasterDB = input("Introduzca el nombre que la base de datos a la cual quieres entrar  \n")
#Facemos unha primeira conexión a unha BBDD creada por defecto dende o principio, para así crear ( xa sexa por primeira vez, 
#ou porque se precise [función por añadir]) unha nova BBDD na cal se gardarán os contrasinais cos seus servicios e usuarios relacionados
PMDB = mysql.connector.connect(host = 'localhost', database= 'sys',  user=MasterUser, password=MasterContra)
PMcursor = PMDB.cursor()
PMcursor.execute("CREATE DATABASE IF NOT EXISTS PasswordManagerDB;")
PMDB.close()
PMcursor.close()
# Cerramos conexión para entrar xa agora ca nova BBDD
PMDB = mysql.connector.connect(host = 'localhost', database= 'PasswordManagerDB',  user=MasterUser, password=MasterContra)
PMcursor = PMDB.cursor()
PMcursor.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_name = '"+ MasterTable +"' ;")
checkTB = PMcursor.fetchone()

	#Bucle como menú no cal manexamos a BBDD
while True:
	if checkTB[0] == 0:
		#Damoslle ao usuario a opción de crear unha nova tabla en caso de que el queira, e a opción de non, en caso de que se equivocase escribindo
		#
		opc = int( input ("Esa tabla non existe, quere creala? Pulse 1 para continuar, pulse calquera outro número para saír")[0:1])
		if opc == 1:
			print ("Vaise crear a nova tabla: ")
			PMcursor.execute("""CREATE TABLE """+ MasterTable +""" (Tipo INT NOT NULL,PRIMARY KEY (Tipo)) ;""")
		else:
			sys.exit("Escribiu outro caracter,polo que sairá do script")
	elif checkTB[0] == 1:
		print("""
				---- Menú ----
			1º Introducir unas credenciales nuevas
			2º Consultar credenciales por sitio
			3º Consultar credenciales por correo electrónico
			4º Consultar credenciales por usuario
			5º Eliminar credenciales
			6º Salir
			""")
		opc = int(input("Introduzca uno de los siguientes números para escoger una opción \n"))
		if opc == 1:
			print("opc1")
		elif opc == 2:
			print("opc2")
		elif opc == 3:
			print("opc3")
		elif opc == 4:
			print("opc4")
		elif opc == 5:
			print("opc5")
		elif opc == 6:
			print("Salir")
			break
		else:
		 print("No ha introducido un número que se corresponda con las opciones, vuelva a intentarlo de nuevo")