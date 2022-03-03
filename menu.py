import mysql.connector,os

def startConnection():
    initDB = mysql.connector.connect(host = 'XXXXX', database= 'XXXXX',  user='XXXXX', password='XXXX', port=3306)
    #Ej 1: mysql.connector.connect(host = 'localhost', database= 'PaswordDatabase',  user='username', password='passwd', port=3306)
    #Ej 2: mysql.connector.connect(host = '10.0.2.56', database= 'PaswordDatabase2',  user='username2', password='passwd2', port=33060)
    return initDB


def createDB():
    initDB = mysql.connector.connect(host = 'xxxxx', user='xxxxxx', password='xxxxx', port=3306)
    cursor = initDB.cursor()
    createDB = "CREATE DATABASE IF NOT EXISTS PasswdMgrDB;"
    useDB = " USE PasswdMgrDB;"
    createDBTable = "CREATE TABLE IF NOT EXISTS PasswordDBClient (Servicio varchar(255), Email varchar(255), Usuario varchar(255), Contraseña varchar(255), TipoServicio varchar(255))"
    cursor.execute(createDB)
    cursor.execute(useDB)
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

        