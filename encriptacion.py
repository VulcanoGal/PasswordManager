from cryptography.fernet import Fernet
import os
 
def genera_clave():
    clave = Fernet.generate_key()
    with open("clave.key","wb") as archivo_clave:
        if os.path.isfile('clave.key'):
            print("OK")
        else:
            archivo_clave.write(clave)


def cargar_clave():
    return open("clave.key","rb").read()


def encrypt(a):
    clave = cargar_clave()
    f = Fernet(clave)
    mensaje = a.encode('utf-8')
    encriptado = f.encrypt(mensaje)
    return encriptado


def decrypt(a):
    clave = cargar_clave()
    f = Fernet(clave)
    mensaje = a.encode('utf-8')
    desencriptado = f.decrypt(mensaje).decode('utf-8')
    print(desencriptado)
    return desencriptado
