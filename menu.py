import mysql.connector,os

def startConnection():
    initDB = mysql.connector.connect(host = 'localhost', database= 'PasswdMgrDB',  user='root', password='abc123.', port=3306)
    return initDB


def createDB():
    initDB = mysql.connector.connect(host = 'localhost', database= 'sys',  user='root', password='abc123.', port=3306)
    cursor = initDB.cursor()
    createDB = "CREATE DATABASE IF NOT EXISTS PasswdMgrDB;"
    useDB = " USE PasswdMgrDB;"
    createInitTable = "CREATE TABLE IF NOT EXISTS checklogin (Master varchar (255))"
    createDBTable = "CREATE TABLE IF NOT EXISTS PasswordDBClient (Servicio varchar(255), Email varchar(255), Usuario varchar(255), Contraseña varchar(255), TipoServicio varchar(255))"
    cursor.execute(createDB)
    cursor.execute(useDB)
    cursor.execute(createInitTable)
    cursor.execute(createDBTable)
    initDB.close()
    cursor.close()


def clearfast():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")
    


def clearWindow():
    if os.name == "posix":
        checkClean = input("Presiona Intro para continuar:")
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        checkClean = input("Presiona Intro para continuar:")
        os.system ("cls")

        