import mysql.connector,os,getpass,ipaddress

def login():
    global dbhost 
    global dbname 
    global dbuser  
    global dbpassword 
    global dbport
    dbhost = input("Introduzca la IP de la BBDD [localhost también es válido]: ")
    dbname = input("Introduzca el nombre de la BBDD: ")
    dbuser = input("Introduzca el nombre de usuario de la BBDD: ")
    dbpassword = getpass.getpass("Introduzca la contraseña del usuario "+ dbuser +" en la BBDD: ")
    dbport = int(input("Introduzca el número del puerto de la BBDD"))
    initDB = mysql.connector.connect(host = dbhost, database = dbname,  user = dbuser, password = dbpassword, port = dbport)
    return initDB

conection = login()

    
def createDB():
    initDB = mysql.connector.connect(host = 'localhost', user='root', password='abc123.', port=3306)
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

        