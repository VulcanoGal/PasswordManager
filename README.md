# PasswordManager
 Password Manager es un administrador de contraseñas seguro que le ayudará en la tarea de mantener sus credenciales seguras sin tener que memorizarlas todas.

 # Pre-requisitos:
    -Tener instalado MYSQL: Con este programa, se trabajará en MySQL. ( https://dev.mysql.com/downloads/installer/ )\
        * Para descargarlo en Windows, deberá acceder a la siguiente página y escoger la opción más adecuada para su equipo, y proceder a la instalación.\
        * En caso de ser una distriución linux, escoja una de las 3 opciónes que aparecen en la página dependiento del administrador de paquetes que su distribución tenga. \
    -Tener instalado Python: El programa está escrito en el lenguaje Python, por lo que necesita instalarlo para que su equipo sea capaz de ejecutarlo. (https://www.python.org/downloads/)\
 # Funcionamiento:
    La primera vez que se ejecute el script, le pedirá que escriba una contraseña maestra la cual será necesaria a partir de ese momento para entrar en el programa. \
    El programa guarda sus contraseñas al igual que su nombre de usuario, nombre y enlace de las páginas o servicios a utilizar, para que sea más facil buscar y/o filtrar.\
    Todos esos datos serán guardados en una BBDD local, la cual no tendrá acceso a internet, y además como medida de protección, las contraseñas serán hasheadas dentro de la BBDD.
