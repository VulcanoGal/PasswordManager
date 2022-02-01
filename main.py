#Importamos el conector MySQL para que este script pueda comunicarse con el server MySQL que instalamos previamente, junto con otras librerías necesarias para mantener limpio
# y legible este código

import library

print('¡Hola, Bienvenido a Password Manager!')
MasterUser = ''
MasterContra = ''
MasterTable = ''
#Bucle para no permitir que las variables estén vacías
while (MasterUser and MasterContra and MasterTable ) == '':
	MasterUser = input("Introduzca el nombre de usuario de la BBDD [Base de Datos] \n")
	MasterContra = input("Introduzca la contraseña del usuario de la BBDD [Base de Datos] \n")
	MasterDB = input("Introduzca el nombre que tiene / va a tener la BBDD donde se guardará sus contraseñas  \n")

#Accedemos a nuestra librería de funciones para crear una nueva tabla
library.createDB(MasterDB,MasterUser,MasterContra)
while True:
	print("""
			---- Menú ----
		1º Introducir unas credenciales nuevas
		2º Consultar credenciales por Servicio
		3º Consultar credenciales por correo electrónico
		4º Consultar credenciales por Usuario
		5º Eliminar credenciales
		6º Modificar credenciales
		7º Salir
		""")
	opc = int(input("Introduzca uno de los siguientes números para escoger una opción \n"))
	if opc == 1:
		print("opc1")
		library.clearWindow
	elif opc == 2:
		print("opc2")
		library.clearWindow
	elif opc == 3:
		print("opc3")
		library.clearWindow
	elif opc == 4:
		print("opc4")
		library.clearWindow
	elif opc == 5:
		print("opc5")
		library.clearWindow
	elif opc == 6:
		print("opc6")
		library.clearWindow
	elif opc == 7:
		print("Salir")
		library.clearWindow
		break
	else:
		print("No ha introducido un número que se corresponda con las opciones, vuelva a intentarlo de nuevo")
		library.clearWindow