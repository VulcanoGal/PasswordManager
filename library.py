import mysql.connector,os
def createDB(a, b, c):
    if a and b and c is not None:
        PMDB = mysql.connector.connect(host = 'localhost', database= 'sys',  user=b, password=c, port=33060)
        PMcursor = PMDB.cursor()
        CreateDB = "CREATE DATABASE IF NOT EXISTS '%s';"%(a)
        useDB = " USE '%s';"%(a)
        createInitTable = "CREATE TABLE IF NOT EXIST checklogin (Master varchar (255))"
        createDBTable = "CREATE TABLE IF NOT EXISTS PasswordDBClient (Servicio varchar(255), Email varchar(255), Usuario varchar(255), Contraseña varchar(255), TipoServicio varchar(255))"
        PMcursor.execute(CreateDB)
        PMcursor.execute(useDB)
        PMcursor.execute(createInitTable)
        PMcursor.execute(createDBTable)
        PMDB.close()
        PMcursor.close()


def clearWindow():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")
    