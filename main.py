#Importamos el conector MySQL para que este script pueda comunicarse con el server MySQL que instalamos previamente, junto con otras librerías necesarias para mantener limpio
# y legible este código

import menu,query

print('¡Hola, Bienvenido a Password Manager!')
MasterUser = ''
MasterContra = ''
MasterDB = ''
#Bucle para no permitir que las variables estén vacías
while (MasterUser and MasterContra and MasterDB) == '':
	MasterUser = input("Introduzca el nombre de usuario de la BBDD [Base de Datos] \n")
	MasterContra = input("Introduzca la contraseña del usuario de la BBDD [Base de Datos] \n")
	MasterDB = input("Introduzca el nombre que tiene / va a tener la BBDD donde se guardará sus contraseñas  \n")


#Accedemos a nuestra librería de funciones para crear una nueva tabla
menu.DBstuff.createDB(MasterDB,MasterUser,MasterContra)
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
		query.addnew()
		menu.clearWindow
	elif opc == 2:
		print("opc2")
		query.filter()
		menu.clearWindow
	elif opc == 3:
		print("opc3")
		query.filter()
		menu.clearWindow
	elif opc == 4:
		print("opc4")
		query.filter()
		menu.clearWindow
	elif opc == 5:
		print("opc5")
		query.delete()
		menu.clearWindow
	elif opc == 6:
		print("opc6")
		query.mod()
		menu.clearWindow
	elif opc == 7:
		print("Salir")
		menu.clearWindow
		break
	else:
		print("No ha introducido un número que se corresponda con las opciones, vuelva a intentarlo de nuevo")
		menu.clearWindow