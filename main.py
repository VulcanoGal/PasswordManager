import mysql.connector
print('¡Hola, Bienvenido a Password Manager!')
##def masterlogin(masterpasswd):
#	i=0
#	while i < 3:
#		masterpasswd = input("Introduzca la contraseña maestra para entrar al gestor")
#		i = i + 1
#		if masterpasswd=="Contraseña":
#			print("Contraseña correcta")
#		else:
#			print("Contraseña Incorrecta, intentos restantes:", i)
#			if    i == 3 :
#				print("Ha fallado 3 veces, se le ha denegado el acceso")
#				break

#def login1(masterpasswd)
#	if (len(masterpasswd) == 0)

#	else
MasterUser = ''
MasterContra = ''
MasterDB = ''
#database= MasterDB,
#while MasterUser == '' or MasterContra == '' or MasterDB == '':
while (MasterUser and MasterContra) == '':
	MasterUser = input("Introduzca el nombre de usuario de la BBDD [Base de Datos] \n")
	MasterContra = input("Introduzca la contraseña del usuario de la BBDD [Base de Datos] \n")
PMDB = mysql.connector.connect(host = 'localhost', database= 'PasswordManagerDB',  user=MasterUser, password=MasterContra)
PMcursor = PMDB.cursor()
checkDB = PMcursor.execute("CREATE DATABASE IF NOT EXISTS PasswordManagerDB1;")
print(checkDB)


while True:
	try:
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
	except:
		print("Ha ocurrido un error")
		break