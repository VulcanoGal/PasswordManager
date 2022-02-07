import getpass, menu
from prettytable import PrettyTable
tabla = PrettyTable()
def conn1(query, values):
    if query is not None:
        conn = menu.start()
        cursor = conn.cursor()
        cursor.execute (query,(values))
        res = cursor.fetchall()
        if res:
            tabla.field_names = ["Página Web o Servicio", "Correo Electrónico", "Nombre de Usuario", "Contraseña", "Tipo Servicio"]
            for fila in res:
                tabla.add_row([fila[0], fila[1], fila[2], fila[3], fila[4]])
            
            print(tabla)
            tabla.clear_rows()



def addnew():
    print("Introduzca los siguientes datos: ")
    C0 = input("Introduzca el tipo de servicio: ")
    C1 = input("Introduzca la página web o aplicación: ")
    C2 = input("Introduzca el correo usado en el sitio web o aplicación: ")
    C3 = input("Introduzca el nombre del usuario: ")
    C4 = getpass.getpass("Introduzca la contraseña correspondiente a " + C3 + " en "+ C1)
    if (C0 and C1 and C2 and C3 and C4) is not None:
        q1 = ("INSERT INTO PasswordDBClient (Servicio, Email, Usuario, Contraseña, TipoServicio) VALUES (%s, %s, %s, %s, %s)", (C1,C2,C3,C4,C0))
        conn = menu.start()
        cursor = conn.cursor()
        cursor.execute ( * q1)
        conn.commit()


def filter1():
    print("Va a filtrar resultados según servicio:")
    a = input("Introduzca el nombre del servicio a filtrar: ")
    if a is not None:
        q2 = ("SELECT * FROM PasswordDBClient where TipoServicio = %s")
        values = a,
        conn1(q2,values)
        exit



def filter2():
    print("Va a filtrar resultados según correo electrónico:")
    a = input("Introduzca el correo a filtrar: ")
    if a is not None:
        q3 = ("SELECT * FROM PasswordDBClient where Email = %s")
        values = a,
        conn1(q3,values)
        exit
    else:
        print("Escribe el nome de un correo, por favor.")



def filter3():
    print("Va a filtrar resultados según Usuario:")
    a = input("Introduzca el nombre del Usuario a filtrar: ")
    if a is not None:
        q4 = ("SELECT * FROM PasswordDBClient where Usuario = %s")
        values = a,
        conn1(q4,values)
        exit
    else:
        print("Escribe el nome de un Usuario, por favor.")