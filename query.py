import getpass, menu, re, encriptacion
from prettytable import PrettyTable
pattern_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
tabla = PrettyTable()

def conn1(query):
    if query is not None:
        conn = menu.start()
        cursor = conn.cursor()
        cursor.execute ( * query)
        conn.commit()
        res = cursor.fetchall()
        if  cursor.rowcount >= 1:
            tabla.field_names = ["Página Web o Servicio", "Correo Electrónico", "Nombre de Usuario", "Contraseña", "Tipo Servicio"]
            for fila in res:
                tabla.add_row([fila[0], fila[1], fila[2], fila[3], fila[4]])
            
            print(tabla)
            tabla.clear_rows()
        else:
            print("No existe nada similar en la BBDD")


def conn2(query, values):
    if query is not None:
        conn = menu.start()
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


def check_email(correo):
    if(re.fullmatch(pattern_email, correo)):
        print("OK")
    else:
        print("El correo escrito no es válido, vuelva a escribirlo")

def addnew():
    print("Introduzca los siguientes datos: ")
    C0 = input("Introduzca el tipo de servicio: ")
    C1 = input("Introduzca el nombre de la aplicación: ")
    C2 = input("Introduzca el correo usado en el sitio web o aplicación: ")
    check_email(C2)
    C3 = input("Introduzca el nombre del usuario: ")
    C4 = getpass.getpass("Introduzca la contraseña correspondiente a " + C3 + " en "+ C1)
    if (C0 and C1 and C2 and C3 and C4) is not None:
        q1 = ("INSERT INTO PasswordDBClient (Servicio, Email, Usuario, Contraseña, TipoServicio) VALUES (%s, %s, %s, %s, %s)", (C1,C2,C3,encriptacion.encrypt(C4),C0))
        conn1(q1)
        #print(q1)


def filter1():
    print("Va a filtrar resultados según servicio:")
    a = input("Introduzca el nombre del servicio a filtrar: ")
    if a is not None:
        q2 = ("SELECT * FROM PasswordDBClient where Servicio = %s")
        values = a,
        conn2(q2,values)
        exit



def filter2():
    print("Va a filtrar resultados según correo electrónico:")
    a = input("Introduzca el correo a filtrar: ")
    if a is not None:
        q3 = ("SELECT * FROM PasswordDBClient where Email = %s")
        values = a,
        conn2(q3,values)
        exit
    else:
        print("Escribe el nome de un correo, por favor.")



def filter3():
    print("Va a filtrar resultados según Usuario:")
    a = input("Introduzca el nombre del Usuario a filtrar: ")
    if a is not None:
        q4 = ("SELECT * FROM PasswordDBClient where Usuario = %s")
        values = a,
        conn2(q4,values)
        exit
    else:
        print("Escribe el nome de un Usuario, por favor.")


def delete():
    print("1 = SI")
    print("Cualquier otro caracter será entendido como un NO")
    prev = int(input("Va a borrar datos de la BBDD, estas seguro de esto?"))
    if prev == 1:
        a = input("Introduzca el nombre del servicio en el cual eliminar el usuario: ")
        b = input("Introduzca el correo del usuario a eliminar de "+ a +": ")

        c = input("Introduzca el nombre de ese usuario: ")
        if a and b and c is not None:
            q5 = ("DELETE FROM PasswordDBClient WHERE Servicio = %s and Email = %s and Usuario = %s", (a, b, c,))
            conn1(q5)
            exit
        else:
            print("Error")
    else:
        exit


def mod():
    M0 = input("Introduzca o servicio a modificar: ")
    M1 = input ("Introduzca o usuario a modificar do servicio " + M0 +" : ")
    if M0 and M1 is not None:
        qcheck = ("SELECT * FROM PasswordDBClient WHERE Servicio = %s and Usuario = %s",(M0, M1))
        if qcheck is not None:
            conn = menu.start()
            cursor = conn.cursor()
            cursor.execute( * qcheck)
            cursor.fetchall()
            if cursor.rowcount != 1:
                print("Error, no hay una entrada en la BBDD que coincida con lo introducido, vuelva a intentarlo ")
                exit
            else :
                C0 = input("Introduzca el tipo de servicio: ")
                C1 = input("Introduzca el nombre de la aplicación: ")
                C2 = input("Introduzca el correo usado en el sitio web o aplicación: ")
                check_email(C2)
                C3 = input("Introduzca el nombre del usuario: ")
                C4 = getpass.getpass("Introduzca la contraseña correspondiente a " + C3 + " en "+ C1)
                if (C0 and C1 and C2 and C3 and C4) is not None:
                    q6 = ("UPDATE PasswordDBClient SET Servicio = %s, Email = %s, Usuario = %s, Contraseña = %s, TipoServicio = %s WHERE Servicio = %s and Usuario = %s", (C1,C2,C3,encriptacion.encrypt(C4),C0,M0,M1))
                    conn1(q6) 
                    exit
                else:
                    print("No se permiten campos vacíos ")
    else:
        print("No se permiten campos vacíos ")