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
	except:
		print("Ha ocurrido un error")