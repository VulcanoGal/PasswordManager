# PasswordManager
 Password Manager es un administrador de contraseñas seguro que le ayudará en la tarea de mantener sus credenciales seguras sin tener que memorizarlas todas.

  ## Pre-requisitos
   - [MYSQL] Con este programa, se trabajará en MySQL.
      * Para descargarlo en Windows, deberá acceder a la siguiente página y escoger la opción más adecuada para su equipo, y proceder a la instalación.
      * En caso de ser una distriución linux, escoja una de las opciónes que aparecen en la página dependiento del administrador de paquetes o sistema operativo que esté usando. 

   - [Python] El programa está escrito en el lenguaje Python, por lo que necesita instalarlo para que su equipo sea capaz de ejecutarlo.
 ## Funcionamiento
   La primera vez que se ejecute el script, le pedirá que escriba una contraseña maestra la cual será necesaria a partir de ese momento para entrar en el programa. 
   El programa guarda sus contraseñas al igual que su nombre de usuario, nombre y enlace de las páginas o servicios a utilizar, para que sea más facil buscar y/o filtrar.
   Todos esos datos serán guardados en una BBDD local, la cual no tendrá acceso a internet, y además como medida de protección, las contraseñas serán hasheadas dentro de la BBDD, para evitar que cualquiera pueda descubrirlas.
 ## Instalación
   Primero de todo vamos a instalar python, para ello en caso de usar Windows basta con usar el instalador .exe que Python ofrece.
   Sin embargo, si usamos una distribución Linux (Ubuntu, Debian, Manjaro, Arch Linux, Fedora, SUSE ...) lo haremos mediante terminal.
   
   La 'x' representa la versión de python, por lo que es recomendable comprobar primero que versión instalar y luego cambiar la letra por la versión.
   -Ubuntu/Debian (apt manager)
   ```sh
      sudo apt install software-properties-common
      sudo add-apt-repository ppa:deadsnakes/ppa
      sudo apt install python3.x
   ```
  -openSUSE (zypper)
   ```sh
      sudo zypper ar http://download.opensuse.org/repositories/devel:/languages:/python:/Factory/openSUSE_12.2/devel:languages:python:Factory.repo
   ```
   -Manjaro/Arch Linux (pacman)
   ```sh
      sudo pacman -S python
   ```


[MYSQL]: <https://dev.mysql.com/downloads/mysql/>
[Python]: <https://www.python.org/downloads/>