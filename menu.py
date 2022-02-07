import mysql.connector,os

def start():
    PMDB = mysql.connector.connect(host = 'localhost', database= 'Paco13245',  user='root', password='abc123..', port=33060)
    return PMDB


def createDB(a):
    if a is not None:
        print("1")
        PMDB = start()
        PMcursor = PMDB.cursor()
        CreateDB = "CREATE DATABASE IF NOT EXISTS "+ a +";"
        useDB = " USE "+ a +";"
        createInitTable = "CREATE TABLE IF NOT EXISTS checklogin (Master varchar (255))"
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
    
