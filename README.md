# <center> PasswordManager </center>
[![CodeFactor](https://www.codefactor.io/repository/github/vulcanogal/passwordmanager/badge/main)](https://www.codefactor.io/repository/github/vulcanogal/passwordmanager/overview/main)
   Password Manager es un administrador de contraseñas seguro que le ayudará en la tarea de mantener sus credenciales seguras sin tener que memorizarlas todas.  
   Además, estas contraseñas estarán cifradas mediante una clave privada que deberá guardar, para que así nadie pueda saber sus contraseñas.

  ## <center> Pre-requisitos </center>
   - [MYSQL] Con este script, se puede  en MySQL.
      * Para descargarlo en Windows, deberá acceder a la siguiente página y escoger la opción más adecuada para su equipo, y proceder a la instalación.
      * En caso de ser una distriución linux, escoja una de las opciónes que aparecen en la página dependiento del administrador de paquetes o sistema operativo que esté usando. 
      * También puedes usar una BBDD externa a la cual poder conectarse
   - [MariaDB] El conector también es disponible con MariaDB.
      * Para descargarlo en Windows, deberá acceder a la siguiente página y escoger la opción más adecuada para su equipo, y proceder a la instalación.
      * En caso de ser una distriución linux, escoja una de las opciónes que aparecen en la página dependiento del administrador de paquetes o sistema operativo que esté usando. 
      * También puedes usar una BBDD externa a la cual poder conectarse
   - [Python] El programa está escrito en el lenguaje Python, por lo que necesita instalarlo para que su equipo sea capaz de ejecutarlo. Además de esto habrá una serie de plugins que deberá instalar para que el programa pueda funcionar sin problemas. Normalmente los equipos Linux ya vienen con Python instalado por defecto, pero en caso de no tenerlo / no estar actualizado, puede clicar en "Python" para dirigirse a la página y seguir la guía de instalación.
# <center> Funcionamiento </center>
   El script principal ( main.py) será el menú por el cual manejará la Base de Datos. Es el único script ejecutable que le dará una pequeña interfaz por terminal para realizar las consultas a la BBDD.  
   Las opciones disponibles son las siguientes:
   - Introducir unas credenciales nuevas
   - Consultar credenciales por Servicio
   - Consultar credenciales por E-mail
   - Consultar credenciales por Usuario
   - Eliminar credenciales
   - Modificar credenciales

# <center> Instalación de plugins </center>
   **ATENCIÓN:**
   En caso de no instalar los plugins, el programa **NO FUNCIONARÁ**.  

   Antes de iniciar el programa, el usuario deberá consultar el archivo de [requisitos](requeriments.md), en el cual estarán listados los plugins necesarios para le funcionamiento correcto, así como los comandos a ejecutar para instalar esos plugins en caso de no saber como.

[MYSQL]: <https://dev.mysql.com/downloads/mysql/>
[Python]: <https://www.python.org/downloads/>
[MariaDB]: <https://www.mariadbtutorial.com/getting-started/install-mariadb/>
