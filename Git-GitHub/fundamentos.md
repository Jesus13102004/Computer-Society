En este capitulo veremos todos los comandos basicos para empezar a trabajar con git.
Al final de este capitulo seras capaz de 
- Configurar e iniciar un repositorio
- Comenzar y detener el seguimiento de archivos
- Preparar (stage) y confirmar (commit) cambios
- Ignorar ciertos archivos y patrones
- Como solucionar errores rapido y facilmente
- Como navegar por el historial del proyecto
- Como ver cambios entre confirmaciones
- Como enviar (push) y recibir (pull) archivos de repositorios remotos

*Obtener un repositorio Git
Para tener un proyecto en git existen dos maneras
- Trabajar con un proyecto existente e importarlo en git:
Para iniciar el proyecto con git necesitas estar en el directorio del proyecto y ejecutar el comando
$ git init
Esto creara un archivo oculto llamado .git que es el esqueleto de un repositorio git
Para empezar a controlar archivos existentes necesitas usar los comandos
$ git add nom_arch
$ git commit -m "Descripcion"
Explicaremos estos comandos a detalle mas adelante

- Clonando un repositorio existente en Git
Para clonar un repositorio se usa el comando
$ git clone [URL]
Este comando crea una copia de todos los datos que tiene el servidor, crea un directorio con el nombre del repositorio y dentro de esa carpeta se crea el archivo .git, ese archivo contiene todo el historial del proyecto y saca una copia de la ultima version guardada del proyecto


* Guardar cambios en el repositorio
Los archivos del repositorio pueden tener dos estados:
- Rastreados (tracked files): Son todos los archivos que estaban en la ultima version guardada del proyecto, pueden ser archivos sin modificar, modificados o preparados.
- Sin rastrear: Son todos los archivos que no estaban en la ultima version guardada del proyecto y que no estan en el area de preparacion
Cuando se editan los archivos Git los identifica como modificados, luego tienes que preparar estos archivos modificados y finalmente confirmar todos los cambios preparados

-Revisando los estados de los archivos
Para ver el estado de los archivos se usa el comando
$ git status
Si ejecutas este comando sin haber echo ninguna modificacion se mostrara lo siguiente
$ git status
On branch master
nothing to commit, working directory clean
Eso quiere decir que el directorio de trabajo esta limpio, en otras palabras, que no hay archivos astreados ni modificados, este comando tambien muestra en que rama se esta trabajando
Si añades un archivo o lo modificas y vuelves a ejecutar el comando te saldra lo siguiente.
$ git status
On branch master
Untracked files:
    (use "git add <file>..." to i nclude in what will be committed)
    nom_arch
nothing added to commit but untracked files present (use "git add" to track)

Lo que muestra este comando es algo extenso, si quieres ver elestado de los archivos de una forma mas compacta puedes usar alguno de los siguientes comandos
$ git status -s
$ git status --short
Los archivos que no estan rastreados saldran con ??
Los preparados con A
Los modificados con M

- Rastrear archivos nuevos
Para rastrear o preparar un archivo se usa:
$ git add nom_arch
Si tienes que preparar varios archivos puedes usar el siguiente comando que prepara todos los archoivos modificados.
$ git add .

Si despues de este comando se vuelve a ejeutar git status se vera que el archivo esta siendo rastreado.
$ git status
On branch master
Changes to be commited
    (use "git reset HEAD <file>..." to unstage
    new file: nom_arch


- Ignorar archivos
En los proyectos existen archivos que no es necesario estarlos preparando y confirmando, como los archivos temporales o los que se crean al compilar el codigo
Para esto existe el archivo .gitignore que es un archivo oculto en el que se pone que archivos ignorar
Las reglas de los patrones que se pueden incluir son:
Ignorar las lineas en blanco y las que inicien con #
Usar patrones glob estandar que se aplicaran recursivamente a todo el directorio del repositorio local
Los patrones pueden iniciar con (/) para evitar recursividad
Los patrones pueden terminar con (/) para especificar un directorio
Los patrones pueden negarse si se añade al principio el signo de exclamacion (!)

Los patrones glob son una especie de expresion regular simplificada usada por los terminales
- (*): Cero o mas caracteres
- ([abc]): Cualquier caracter dentro de los corchetes
- (?): Un caracter cualquiera
- ([0-9]): Cualquier caracter del 0 al 9
- (a/**/z) Directorios anidados a/z, a/b/z, a/b/c/z


- Ver los cambios preparados y no preparados
Para ver a detalle las modificaciones de los archivos se usa
$ git diff
Este comando muestra las lineas exactas que fueron añadidas y eliminadas, es decir el parche.
Compara lo que esta en el directorio de trabajo con lo que esta en el area de preparacion
Este comando solo muestra los cambios que no estan preparados, si preparas los cambios este comando no mostrara nada

Para ver lo que esta preparado y sera incluido en la siguiente confirmacion se puede usar cualquiera de los siguientes comandos:
$ git diff --stage
$ git diff --cached
Compara los cambios preparados con la ultima instantanea confirmada


-Confirmar los cambios
Para confirmar los cambios que se prepararon previamente con el comando git add se usa el siguiente comando
$ git commit -m "Descripcion"
Al ejecutar este comando los cambios quedan confirmados y va a devolver algo asi:
[master 463dc4f] Descripcion
    2 files changed, 2 insertions (+)
    crate mode 100644 README

Indica que rama se confirmo
El checksum SHA-1
Cuantos archivos han cambiado
Estadistica sobre las lineas añadidas y eliminadas en el commit 

Si quieres preparar y confirmar en un solo comando puedes usar
$ git commit -a -m "Descripcion"


-Eliminar archivos
Para eliminar un archivo se necesita preparar la eliminacion y despues confirmarla, el comando para hacer esto es:
$ git rm nom_arch
Despues de ejecutar ese comando y hacer un git commit queda confirmada la eliminacion del archivo

Si solo quieres eliminar el archivo del area de preparacion y dejarlo en el disco se usa el comando:
$ git rm --cached nom_arch
El comando git rm puede recibir como parametro patrones glob


- Cambiarle el nombre a un archivo
Para cambiarle el nombre a un archivo se usa el comando
$ git mv nom_arch new_nom_arch


* Ver el historial de confirmaciones
Despues de haber echo varias confirmaciones probablemente quieras ver que confirmaciones se han echo, para esto usamos el comando
$ git log
Este comando muestra la lista de todas las confirmaciones que se le han echo al proyecto, lo que muestra en terminal este comando es:
- Muestra de la confirmacion mas reciente a la mas antigua
- Muestra la suma de comprobacion SHA-1
- Muestra el nombre y correo del autor
- Muestra la fecha de la confirmacion
- Muestra el mensaje de confirmacion

Al comando git log se le pueden agregar ciertos parametros para limitar o hacer mas precisa la busqueda, algunos parametros son:
-p = Muestra la diferencia entre cada confirmacion
-2 = Muestra las dos ultimas confirmaciones, se puede poner el numero que sea
--stat = Muestra la lista de archivos modificados, cuantas lineas han sido añadidas o eliminadas y un resumen de toda la informacion.
--pretty = Modifica el formato de la salida, algunos ejemplos de uso son:
    $ git log --prety=oneline
    $ git log --prety=short
    $ git log --prety=full
    $ git log --prety=fuller

Para limitar la salida existen varios comandos:
--since = Puede limitar por año, mes, semana, dia o tiempo
    $ git log --since=2.weeks
--author = Muestra las confirmaciones de un autor
--grep = Busca palabras dentro del mensaje de confirmacion
--all-match = Para usar dos filtros simultaneamente se usa este comando


* Deshacer cosas
- Deshacer una confirmacion
Uno de los casos mas comunes es deshacer una confirmacion, ya sea por que te equivocaste en el mensaje o te falto subir un archivo, para deshacer un commit se usa el comando
$ git commit --amend

Si no has echo cambios desde la ultima confirmacion al ejecutar --ammend la version actual quedara igual, solo te permitira cambiar el mensaje
Si confirmaste y olvidaste agregar otro archivo se pueden usar estos comandos:
$ git commit -m "initial comit"
$ git add nom_arch
$ git commit --amend

La segunda confirmacion reemplaza el resultado de la primera

- Deshacer un archivo preparado
Si preparaste un archivo pero no quieres que se confirme en este momento, para sacarlo del area de preparacion se usa el comando:
$ git reset HEAD nom_arch

- Deshacer un archivo Modificado
Si modificaste un archivo y por alguna razon quieres regresar a la vercion pasada sin guardar las modificaciones que le hiciste, se usa el comando
$ git checkout -- nom_arch
Al ejecutar este comando todos los datos que no se confirmaron se perderan permanentemente

* Trabajar con remotos
Los repositorios remotos son versiones de tu proyecto que estan hospedadas en internet. Puedes tener varios repositorios remotos, algunos tendran solo permiso de lectura y otros de lectura y escritura.

- Ver tus remotos
Para ver los repositorios remotos que tienes configurados se usa el comando:
$ git remote
Si clonaste el repositorio te saldra la palabra "origin"

Para ver las URLs que se usan para leer y escribir en los archivos se usa el comando.
$ git remote -v

- Añadir repositorios remotos
Para añadir repositorios remotos al proyecto se ejecuta el comando
$ git remote add nom_remote URL
Ahora puedes usar el nom_remote para referirte al repositorio en la terminal

- Traer y combinar remotos
Para recuperar los archivos remotos del repositorio que acabas de agregar se usa el comando:
$ git fetch nom_remote
Este comando ira al repositorio remoto y traera todos los datos que no tienes de dicho remoto. Por lo tanto:
$ git fetch origin
Trae todos los archivos nuevos que se agregaron al repositorio remoto despues de ser clonado
Si tienes una rama que rastre una rama remota usa el comando:
$ git pull
Este comando trae los datos y los combina automaticamente con la rama actual

- Enviar a tus remotos
Si quieres enviar tus modificaciones a un servidor se usa el comando
$ git push nom_remote nom_rama
Este comando sube la rama que escojas al remoto que especificaste.
Si quieres subir los comandos de la rama en la que estas a su remoto asociado usa 
$ git push

- Inspeccionar un remoto
Si quieres saber informacion detallada de un remoto usa el comando 
$ git remote show nom_remote
Este comando muestra la URL dle repositorio remoto y la informacion de rastreo de ramas

- Eliminar y renombrar remotos
Para renombrar un remoto se usa el comando
$ git remote rename nom_remote new_nom_remote

Para eliminar un remoto se usa el comando
$ git remote rm nom_remote


*Etiquetado 
Sirve para marcar puntos importantes del historial, se usa tipicamente para marcar versiones de lanzamiento. En esta seccion veremos como listar las etiquetas disponibles, como crear nuevas etiquetas y cuales son los distintos tipos de etiquetas.

- Listar las etiquetas
Para listar las etiquetas en orden alfabetico se usa el comando 
$ git tag
Si quieres listar solo algunas etiquetas puedes hacer esto
$ git tag -l "v1.8.5*"
Esre comando muestra las etiquetas d ela version v1.8.5

- Crear etiqueta
Git tiene dos tipos de etiquetas
    Etiqueta ligera: Es parecida a una rama que no cambia, simplemente es un puntero a un commit en especifico. para crearla se usa el comando
    $ git tag nom_tag
    
    Etiquetas anotadas: Se guardan en la base de datos de Git como objetos enteros
        - Tiene checksum
        - Nombre del etiquetador
        - Correo electronico
        - Fecha
        - Tiene un mensaje asociado
        - Pueden ser firmadas y verificadas con GNU Privacy Guard (GPG)
    Para crear una etiqueta anotada se le agrega -a al comando git tag
    $ git tag -a v1.4 -m "my version 1.4"

    El -m especifica el mensaje de la etiqueta, si no se pone el -m se abrira el editor de texto para que lo escribas 
    Para ver la informacion de la etiqueta se usa el comando 
    $ git show nom_tag

- Etiquetado tardio
Para etiquetrar un commit despues de mucho tiempo se tiene que poner parte del checksum para referenciar el commit que vas a etiquetar
$ git tag -a nom_tag checksum
Recuerda que el check sum se obtiene con el comando
$ git log

- Compartir etiquetas
Hay dos formas de mandar las etiquetas, si quieres mandar solo una se usa
$ git push nom_remote nom_tag
Si quieres mandar todas las etiquetas que no estan en el servidor usa el comando
$ git push nom_remote --tags


* Alias de git
Los alias sirven para tener una experiencia mas simpl, sencilla y familiar con git.
Pondremos el ejemplo de como crearle un alias al comando commit
Para crear el alias se usa el comando
$ git config --global alias.ci commit
Ahora puedes hacer commit de estas dos formas
$ git ci -m "my commit"
$ git commit -m "my commit"

Conclusion
Ahora ya sabes hacer las operaciones basicas de git, crear o clonar repositorios, hacer cambios, preparar y confirmasr esos cambios y ver el historial de los cambios
