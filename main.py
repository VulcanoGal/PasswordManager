import mysql.connector
print('¡Hola, Bienvenido a Password Manager!')
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
		if opc == "1":
			print("opc1")
		elif opc == "2":
			print("opc2")
		elif opc == "3":
			print("opc3")
		elif opc == "4":
			print("opc4")
		elif opc == "5":
			print("opc5")
		elif opc == "6":
			print("Salir")
			break
		else:
		 print("No ha introducido un número, vuelva a intentarlo de nuevo")
	except:
		print("Ha ocurrido un error")
		break