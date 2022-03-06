# <center> Plugins </center>

Estos plugins mencionados serán necesarios para el funcionamiento correcto del Password Manager

## <center>Cryptography</center>

```bash
pip install crytography
```

Cryptography es el encargado de importar fernet, el método que usaremos para crear una clave privada la cual será la encargada de cifrar las contraseñas de la BBDD, como de la contraseña maestra

## <center>Prettytable</center>

```bash
pip install pretty-table
```

PrettyTable es un plugin que sirve básicamente para dar una salida legible y organizada para que el usuario pueda leer sin problemas las contraseñas almacenadas en la Base de Datos

## <center>validate-email</center>

 ```bash
 pip install validate_email
 pip install pydns
 ```

​	Validate-Email es un pequeño plugin que comprueba que el correo que ha introducido existe, y no se introduzca un correo falso.

## <center>mysql.connector</center>

```bash
pip install mysql-connector
```

Este plugin es el encargado de hacer las conexiones entre la BBDD y los scripts de Python.

Es compatible con bases de datos que usen tanto MySQL como MariaDB.
