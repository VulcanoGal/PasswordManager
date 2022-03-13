from cryptography.fernet import Fernet
import os
 
def genera_clave():
    if os.path.isfile('clave.key') and os.path.getsize('clave.key') > 0:
         print("OK")
    else:
        with open("clave.key","w") as archivo_clave:
            clave = Fernet.generate_key().decode()
            archivo_clave.write(clave)

# Cargar clave
def cargar_clave():
    return open("clave.key","r").read()


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
    return desencriptado