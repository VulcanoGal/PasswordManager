#Importamos el conector MySQL para que este script pueda comunicarse con el server MySQL que instalamos previamente, junto con otras librerías necesarias para mantener limpio
# y legible este código

import menu, query

print('¡Hola, Bienvenido a Password Manager!')
#Accedemos a nuestra librería de funciones para crear una nueva tabla
#menu.createDB()
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
		query.addnew()
		menu.clearWindow()
	elif opc == 2:
		query.filter1()
		menu.clearWindow()
	elif opc == 3:
		query.filter2()
		menu.clearWindow()
	elif opc == 4:
		query.filter3()
		menu.clearWindow()
	elif opc == 5:
		query.delete()
		menu.clearWindow()
	elif opc == 6:
		#query.mod()
		menu.clearWindow()
	elif opc == 7:
		print("Salir")
		menu.clearWindow()
		break
	else:
		print("No ha introducido un número que se corresponda con las opciones, vuelva a intentarlo de nuevo")
		menu.clearWindow()