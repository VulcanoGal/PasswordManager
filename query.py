import getpass,menu
def addnew():
    print("Introduzca los siguientes datos: ")
    C0 = input("Introduzca el tipo de servicio: ")
    C1 = input("Introduzca la página web o aplicación: ")
    C2 = input("Introduzca el correo usado en el sitio web o aplicación: ")
    C3 = input("Introduzca el nombre del usuario: ")
    C4 = getpass.getpass("Introduzca la contraseña correspondiente a " + C3 + " en "+ C1)
    if (C0 and C1 and C2 and C3 and C4) is not None:
        q1 = ("INSERT INTO PasswordDBClient (Servicio, Email, Usuario, Contraseña, TipoServicio) VALUES (%s, %s, %s, %s, %s)", (C1,C2,C3,C4,C0))
        menu.DBstuff.connection(q1)