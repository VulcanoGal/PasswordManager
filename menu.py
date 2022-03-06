import mysql.connector, os, getpass, encriptacion

def login():
    global dbhost  
    global dbuser  
    global dbpassword 
    global dbport
    dbhost = input("Introduzca la IP de la BBDD [localhost también es válido]: ")
    dbuser = input("Introduzca el nombre de usuario de la BBDD: ")
    dbpassword = getpass.getpass("Introduzca la contraseña del usuario " + dbuser + " en la BBDD: ")
    dbport = int(input("Introduzca el número del puerto de la BBDD: "))
    initDB = mysql.connector.connect(host=dbhost, user=dbuser, password=dbpassword, port=dbport)
    return initDB

conection = login()

    
def createDB():
    global dbname
    dbname = input("Introduzca el nombre de la BBDD: ")
    initDB = conection
    cursor = initDB.cursor()
    createDB = "CREATE DATABASE IF NOT EXISTS " + dbname + ";"
    useDB = " USE " + dbname + ";"
    createDBTable = "CREATE TABLE IF NOT EXISTS PasswordDBClient (Servicio varchar(255), Email varchar(255), Usuario varchar(255), Contraseña varchar(999), TipoServicio varchar(255));"
    createMasterTable = "CREATE TABLE IF NOT EXISTS MasterPasswd (Password varchar(999))"
    queryMasterPasswd = "SELECT * FROM MasterPasswd"
    cursor.execute(createDB)
    cursor.execute(useDB)
    cursor.execute(createDBTable)
    cursor.execute(createMasterTable)
    cursor.execute(queryMasterPasswd)
    checkMasterPasswd = cursor.fetchone()
    if cursor.rowcount != 1:
        newMasterPasswd = getpass.getpass("No tiene una contraseña maestra, vamos a añadir una: ")
        values = encriptacion.encrypt(newMasterPasswd)
        query = ("INSERT INTO MasterPasswd (Password) VALUES (%s)",(values,))
        cursor.execute( * query)
        initDB.commit()
    else:
        masterpasswd = getpass.getpass("Introduce la contraseña maestra: ")
        checkMasterPasswd = encriptacion.decrypt(checkMasterPasswd[0])
        if masterpasswd != checkMasterPasswd:
            print("La contraseña maestra es incorrecta, saliendo...")
            exit()
        else:
            print("Contraseña Maestra OK")

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
