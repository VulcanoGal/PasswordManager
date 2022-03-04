import getpass, menu, encriptacion
from prettytable import PrettyTable
from validate_email import validate_email
tabla = PrettyTable()

def modifyDBQueries(query):
    if query is not None:
        conn = menu.conection
        cursor = conn.cursor()
        cursor.execute ( * query)
        conn.commit()
        cursor.fetchall()
        

def selectQueries(values, Type):
    if values is not None:
        query = ("SELECT * FROM PasswordDBClient where "+ Type +" = %s")
        conn = menu.conection
        cursor = conn.cursor()
        cursor.execute (query,(values))
        res = cursor.fetchall()      
        if cursor.rowcount >= 1:
            tabla.field_names = ["Página Web o Servicio", "Correo Electrónico", "Nombre de Usuario", "Contraseña", "Tipo Servicio"]
            for fila in res:
                tabla.add_row([fila[0], fila[1], fila[2], encriptacion.decrypt(fila[3]), fila[4]])

            print(tabla)
            tabla.clear_rows()
        else:
            print("No existe nada similar en la BBDD")

def addnew():
    print("Introduzca los siguientes datos: ")
    TipoServicio = input("Introduzca el tipo de servicio: ")
    Servicio = input("Introduzca el nombre de la aplicación: ")
    Email = input("Introduzca el correo usado en el sitio web o aplicación: ")
    validate_email(Email, check_mx=True, verify=True)
    Users = input("Introduzca el nombre del usuario: ")
    Passwd = getpass.getpass("Introduzca la contraseña correspondiente a " + Users + " en "+ Servicio)
    if (TipoServicio and Servicio and Email and Users and Passwd) is not None:
        query = ("INSERT INTO PasswordDBClient (Servicio, Email, Usuario, Contraseña, TipoServicio) VALUES (%s, %s, %s, %s, %s)", (Servicio.capitalize(),Email,Users,encriptacion.encrypt(Passwd),TipoServicio.capitalize()))
        modifyDBQueries(query)


def services():
    Type = "Servicio"
    a = input("Va a filtrar resultados según servicio. Introduzca el nombre del servicio a filtrar: ")
    if a is not None:
        values = a,
        selectQueries(values,Type)
        exit



def emails():
    Type = "Email"
    a = input("Va a filtrar resultados según correo electrónico. Introduzca el correo a filtrar: ")
    validate_email(a, check_mx=True, verify=True)
    if a is not None:

        values = a,
        selectQueries(values,Type)
        exit
    else:
        print("Escribe el nome de un correo, por favor.")



def users():
    Type = "Usuario"
    a = input("Va a filtrar resultados según Usuario. Introduzca el nombre del Usuario a filtrar: ")
    if a is not None:   
        values = a,
        selectQueries(values,Type)
        exit
    else:
        print("Escribe el nome de un Usuario, por favor.")


def delete():
    print("1 = SI")
    print("Cualquier otro caracter será entendido como un NO")
    prev = int(input("Va a borrar datos de la BBDD, estas seguro de esto?"))
    if prev == 1:
        DelService = input("Introduzca el nombre del servicio en el cual eliminar el usuario: ")
        DelEmail = input("Introduzca el correo del usuario a eliminar de "+ DelService +": ")
        DelUser = input("Introduzca el nombre de ese usuario: ")
        if DelService and DelEmail and DelUser is not None:
            query = ("DELETE FROM PasswordDBClient WHERE Servicio = %s and Email = %s and Usuario = %s", (DelService.capitalize(), DelEmail, DelUser,))
            modifyDBQueries(query)
            exit
        else:
            print("Error")
    else:
        exit


def mod():
    ModService = input("Introduzca o servicio a modificar: ")
    ModUser = input ("Introduzca o usuario a modificar do servicio " + ModService +" : ")
    if ModService and ModUser is not None:
        qcheck = ("SELECT * FROM PasswordDBClient WHERE Servicio = %s and Usuario = %s",(ModService.capitalize(), ModUser.capitalize()))
        if qcheck is not None:
            conn = menu.conection
            cursor = conn.cursor()
            cursor.execute( * qcheck)
            cursor.fetchall()
            if cursor.rowcount != 1:
                print("Error, no hay una entrada en la BBDD que coincida con lo introducido, vuelva a intentarlo ")
                exit
            else :
                TipoServicio = input("Introduzca el tipo de servicio: ")
                Servicio = input("Introduzca el nombre de la aplicación: ")
                while check is False:
                    Email = input("Introduzca el correo usado en el sitio web o aplicación: ")
                    check = validate_email(Email, check_mx=True, verify=True)

                Users = input("Introduzca el nombre del usuario: ")
                Passwd = getpass.getpass("Introduzca la contraseña correspondiente a " + Users + " en "+ Servicio)
                if (TipoServicio and Servicio and Email and Users and Passwd) is not None:
                    query = ("UPDATE PasswordDBClient SET Servicio = %s, Email = %s, Usuario = %s, Contraseña = %s, TipoServicio = %s WHERE Servicio = %s and Usuario = %s", (Servicio.capitalize(),Email,Users,encriptacion.encrypt(Passwd),TipoServicio.capitalize(),ModService.capitalize(),ModUser.capitalize()))
                    modifyDBQueries(query) 
                    exit
                else:
                    print("No se permiten campos vacíos ")
    else:
        print("No se permiten campos vacíos ")