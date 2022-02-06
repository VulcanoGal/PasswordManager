import mysql.connector,os,main
class DBstuff:
    def __init__(self):
        self.a = input("Introduzca el nombre de usuario de la BBDD [Base de Datos] \n")
        self.b = input("Introduzca la contraseña del usuario de la BBDD [Base de Datos] \n")
        self.c = input("Introduzca el nombre que tiene / va a tener la BBDD donde se guardará sus contraseñas  \n")

    def createDB(self):
        if self.a and self.b and self.c is not None:
            PMDB = mysql.connector.connect(host = 'localhost', database= 'sys',  user=self.b, password=self.c, port=33060)
            PMcursor = PMDB.cursor()
            CreateDB = "CREATE DATABASE IF NOT EXISTS "+ self.a +";"
            useDB = " USE "+ self.a +";"
            createInitTable = "CREATE TABLE IF NOT EXISTS checklogin (Master varchar (255))"
            createDBTable = "CREATE TABLE IF NOT EXISTS PasswordDBClient (Servicio varchar(255), Email varchar(255), Usuario varchar(255), Contraseña varchar(255), TipoServicio varchar(255))"
            PMcursor.execute(CreateDB)
            PMcursor.execute(useDB)
            PMcursor.execute(createInitTable)
            PMcursor.execute(createDBTable)

    def connection(self):
        PMDB = mysql.connector.connect(host = 'localhost', database= 'sys',  user=self.b, password=self.c, port=33060)
        PMcursor = PMDB.cursor()



def clearWindow():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")
    
