Git en el Servidor

En este punto ya deveras de ser capaz de realizar la mayoría de las tareas diarias para las cuales estarás usando Git. Sin embargo, para poder trabajar de forma colaborativa es necesario tener un repositorio remoto al que tengan acceso todos los miembros del proyecto y que sea una copia confiable sobre la que puedan trabajar.
Poner en funcionamiento un servidor Git es bastante sencillo, 
Primero tienes que elegir con que protocolo te vas a comunicar con el servidor, veremos los diferentes protocolos disponibles, así como los pros y contras de cada uno
Lo siguiente es explicar algunas configuraciones comunes utilizando dichos protocolos y como poner a funcionar tu servidor.
Finalmente revisaremos algunas de las opciones hospedadas.


Los Protocolos
Git puede usar únicamente cuatro protocolos para transferir datos:
-	Local
-	HTTP
-	SSH
-	Git
Vamos a ver en que consiste cada uno, así como sus ventajas y desventajas.

Local Protocol
Es el más básico, donde el repositorio remoto es simplemente otra carpeta en el disco, se usa cuando todos los miembros del equipo tienen acceso a un solo sistema como lo es un punto de montaje NFS o el caso menos viable es que todos tengan acceso a un solo computador.
Para clonar o enviar datos a un repositorio remoto local se usa el “path” del proyecto de esta forma:

$ git clone /opt/git/preject.git
$ git clone file:///opt/git /project.git

La mejor forma es usar únicamente el “path” ya que al agregar “file://”  Git lanza el proceso que usa habitualmente para transferir datos sobre una red y dicho proceso suele ser menos eficiente y más tardado.
Para añadir un repositorio local a un proyecto git existente puedes hacerlo de esta manera:

$ git remote add local_proj /opt/git/project.git

Ventajas:
La ventaja de los repositorios locales es su simplicidad y el aprovechamiento de los permisos preexistentes de acceso, también es útil para recuperar rápidamente el contenido del repositorio de trabajo de alguna otra persona

Desventajas:
La principal desventaja es la dificultad de acceso desde distintas ubicaciones, también cabe destacar que una carpeta compartida no es principalmente la opción más rápida, un repositorio local es rapido solamente en las ocasiones que tienes acceso rápido a él, normalmente un repositorio NFS es más lento que un repositorio SSH.


Protocolos HTTP
Git puede utilizar HTTP de dos maneras, antes de la versión 1.6.6 solamente se podía usar el protocolo HTTP solo en modo lectura, en laa versión 1.6.6 se integró un nuevo protocolo HTTP más inteligente el cual trabaja similar al protocolo SSH.
Nos referiremos a la nueva versión como HTTP “inteligente” y a la versión anterior como HTTP “tonto”.

HTTP Inteligente 
Funciona similar al protocolo SSH pero se ejecuta sobre puertos HTTP/S y puede usar los mecanismos de autenticación HTTP, por lo que es mas fácil para los usuarios por que se identifican con usuario y contraseña en lugar de usar claves SSH.
El protocolo HTTP tiene una única URL para todo, como clonar, enviar y recibir datos.

HTTP Tonto
Lo bueno de este protocolo es su simplicidad para configurarlo, solamente es poner el repositorio Git bajo el directorio raíz de documentos HTTP y especificar un punto de enganche, desde ese momento cualquiera con acceso al servidor web donde se publique el repositorio podrá clonarlo.
Para permitir acceso de lectura se deben de ejecutar los siguientes comandos:

$ cd /var/www/htdocs
$ git clone --bare /path/to/git_project gitproject.git
$ cd gitproject.git
$ mv hooks/post-update.sample hooks/post-update
$ chmod a+x hooks/post-update

Ahora las personas que quieran clonar el repositorio tienen que usar este comando:

$ git clone https://example.com/gitproject .git

En este ejemplo usamos la carpeta /var/www/htdocs que es la habitual en configuraciones, pero se puede usar cualquier servidor web estático
Ventajas
Nos centraremos en las ventajas del HTTP “inteligente.
-	Tener una única URL para todos los tipos de acceso y que el servidor pida autenticación solo cuando sea necesario
-	Permitir autenticar mediante usuario y contraseña es una ventaja sobre SSH ya que no es necesario generar claves SSH y subir la publica al servidor 

Desventajas
HTTP/S puede ser un poco más complejo de configurar comparado con SSH en algunos sitios.
 En otros casos se encuentra poca ventaja sobre el uso de otros protocolos.

Protocolo SSH

Es un protocolo muy usado para alojar repositorios Git en hostings privados, además es un protocolo de red autenticado sencillo de utilizar
Para clonar un repositorio en SSH se usa el siguiente comando:

$ git clone ssh://user@server/Project.git

También puedes usar la sintaxis estilo scp del protocolo SSH:

$ git clone user@server:project.git

Ventajas
-	Es relativamente fácil de configurar 
-	El acceso es seguro, estando todas las transferencias encriptadas y autentificadas 
-	Al igual que los protocolos HTTP, Git y Local, SSH es eficiente comprimiendo los datos lo más posible antes de transferirlos. 

Desventajas
Es imposible dar acceso anónimo al repositorio, todos los colaboradores deben tener configurado un acceso SSH al servidor. Si lo usas dentro de una red corporativa, posiblemente SSH sea el único protocolo que tengas que usar.

Protocolo Git
Es un demonio (deamon) especial que viene incorporado en Git, escucha por un puerto dedicado (9418) y funciona de manera similar a SSH pero sin ninguna medida de autentificación, para hacer público este repositorio se tiene que crear un archivo llamado “git-deamon-export-ok”.
Al agregar este archivo el repositorio estar disponible para que cualquiera lo pueda clonar, por lo que si alguien encuentra tu proyecto en internet puede hacerle un push y agregar información que no te sirva.
Ventajas
Es el más rápido de todos los disponibles, ideal para proyectos muy grandes que no requieran de autenticación.
Utiliza los mismos mecanismos de transmisión de datos que el protocolo SSH pero sin la sobrecarga de encriptación y autentificación.

Desventajas
Falta de autentificación, no es recomendado que sea el único protocolo de acceso al proyecto.
Necesita activar su propio “demonio” y necesita configurar “xinetd” o similar, lo cual no suele estar disponible en el sistema donde estes trabajando.


Configurando Git en un servidor
Demostraremos los comandos y pasos necesarios para hacer las instalaciones básicas en un servidor basado en Linux.
Para configurar por primera vez un servidor hay que exportar un repositorio existente en un nuevo repositorio vacío. Para clonar un repositorio con el fin de crear un nuevo repositorio vacío se usa el comando:

$ git clone --bare my_project my_project.git
Cloning into bare repository “my_project.git”…
done.

Al ejecutar este comando tendrás una copia de los datos del directorio Git en tu directorio my_project.git

Colocando un repositorio vacío en un servidor

Ya que tienes una copia vacía de tu repositorio, necesitas ponerlo en tu servidor y establecer sus protocolos.
Digamos que tu servidor es “git.example.com” con acceso a SSH y quieres almacenar todos tus repositorios bajo el directorio /opt/git.
Puedes configurar tu nuevo repositorio copiando tu repositorio vacío a:

$ scp -r my_project.git user@git.example.com:/opt/git

Ahora los usuarios que tienen acceso SSH con permisos de lectura en el directorio /opt/git pueden clonar tu repositorio con el comando:

$ git clone user@git.example.com:/opt/git/my_project.git

Si un usuario accede por medio de SSH a un servidor y tiene permisos de escritura en el directorio automáticamente también tendrá acceso push.
Pequeñas configuraciones
Uno de los aspectos más complicados de Git es la gestión de usuarios.
Si quieres que algunos archivos sean de solo lectura para unos usuarios y de lectura y escritura para otros, el acceso y los permisos pueden ser un poco más difíciles de organizar.
Existen algunas maneras con las cuales les puedes dar acceso a tu equipo:
-	La primera es crear cuentas para todos, es sencillo, pero si tienes un equipo muy grande puede ser tardado
-	La segunda es crear un solo usuario git en la máquina, cada usuario te tiene que enviar su llave SSH publica para que la agregues al archivo “~/.ssh/authorized_keys” 
-	La tercera manera es hacer que tu servidor SSH autentifique desde un servidor LDAP o desde alguna otra fuente de autentificación.


Generando tu clave pública SSH

Para crear una clave publica tienes que asegurarte que no tengas ya una clave, para esto te tienes que situar en el directorio “~/.ssh” y ver los archivos que tienes en ese directorio con el comando “ls”, si cuentas con un archivo con extensión “.pub” esa es tu clave publica, ahora lo único que necesitas hacer es copiar el contenido de ese archivo y compartirlo con el administrador del servidor.

En caso de que no tengas ese archivo o incluso no tienes la carpeta .ssh se ejecuta el siguiente comando

$ ssh-keygen

Al ejecutar ese comando te va a pedir confirmación de dónde vas a guardar las claves, después te va a pedir dos veces una contraseña, en caso de que no quieras estar escribiendo la contraseña cada que uses la clave la puedes dejar en blanco

Conclusión:
Vimos varias opciones para obtener un repositorio Git remoto, tener tu propio servidor te da control y te permite usar tu servidor dentro de tu propio cortafuegos, pero esto necesita mucho tiempo de configuración y mantenimiento.
Si usas un servidor hospedado es fácil de configurar y mantener, pero algunas organizaciones no permiten tener tu código en el servidor de alguien más. 
