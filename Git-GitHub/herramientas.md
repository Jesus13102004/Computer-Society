Herramientas de Git

En este capítulo veremos herramientas bastante poderosas que no necesariamente usaras todos los días, pero que puedes necesitar en algún momento.

Revisión por Selección
Git te permite especificar ciertos commits o un rango de estos de diferentes maneras.
Se puede referir a un commit por el hash SHA-1 que se le asigna, pero existen formas más amigables para referirse a los commits.

SHA-1 corto
Te puedes referir a un hash únicamente usando los primeros 4 dígitos, siempre y cuando no sea ambiguo, esto quiere decir que no exista otro commit que inicie con esos caracteres.
Si ejecutamos el comando “git log”, vamos a tener la lista de todos los commits que tenemos, si escogemos uno de esos commits, tomamos los primeros 4 dígitos y ejecutamos el comando:

$ git show num_SHA-1

Donde num_SHA-1 son los 4 dígitos del hash, este comando nos mostrara la siguiente información:
-	El hash SHA-1 completo
-	Autor y correo
-	Fecha
-	Mensaje del commit
-	Un diff entre el ancestro de ese commit y el commit

Si ejecutas este comando:

$ git log –abbrev-commit –pretty=oneline

Te mostrara una lista de todos los commits con 7 dígitos de hash manteniéndolos únicos, en caso de que haya dos que se repitan les agrega un carácter extra.

Referencias por Ramas
Para ver la información del último commit de una rama puedes ejecutar el siguiente comando:

$ git show nom_rama

Este comando mostrara la misma información del commit que se muestra cuando ponemos como parámetro el hash.
Si quieres conocer a que hash apunta una rama puedes usar una herramienta de plomería llamada “rev-parse”, esta herramienta sirve para operaciones de bajo nivel y no está diseñada para ser utilizada en operaciones diarias.

$ git rev-parse nom_rama

La salida de este comando son los 40 dígitos del hash del commit al que apunta esa rama.

Nombres cortos de RefLog
Mientras tu estas trabajando git va guardando un historial de los cambios que vas haciendo, va registrando los commits, los saltos entre ramas, etc.
Esto se puede ver con el comando:

$ git reflog

Este comando mostrara todos los cambios que has hecho, cabe destacar que este es un historial temporal, vas a ver el historial en este formato

734713b HEAD@{n}: commit: added some blame

Si quieres ver a detalle un commit o un salto de rama puedes ocupar HEAD@{n} para referenciarlo de esta manera

$ git show HEAD@{2}

Rangos de Commits

La forma más común de especificar un rango de commits es con la sintaxis de dos puntos, puedes ver los commits que no han sido fusionados a tu rama principal, pero están en otra trama puedes usar este comando.

$ git log main..nom_rama

Este comando muestra todos los commits alcanzables por nom.rama que no son alcanzables por la rama main.

La sintaxis de múltiples puntos permite hacer más de una consulta a la vez, por ejemplo, puedes ver todos los commits que son alcanzables desde refA, refB pero no desde refC.

$ git log refA refB ^refC
$ git log refA refB --not refC

La sintaxis de tres puntos muestra los commits que son alcanzables por alguna de dos referencias, pero no por las dos referencias al mismo tiempo.

$ git log refA…refB


Organización Interactiva

 Para asegurarte de que tus confirmaciones sean un conjunto de cambios lógicamente separados y puedan ser revisados fácilmente agrega el parámetro”-i” al comando add, de esta manera:

$ git add -i
staged 	unstaged path   
1: 	unchanged 	+0/-1 TODO   
2: 	unchanged 	+1/-1 index.html   
3: 	unchanged 	+5/-1 lib/simplegit.rb 

*** Commands ***   
1: status 	2: update 	3: revert 	4: add untracked   
5: patch 	6: diff 		7: quit 		8: help 
What now>

Este comando te muestra los cambios que has realizado a la izquierda y cambios que no has realizado a la derecha, después muestra una serie de comandos.
Aquí puedes ver los archivos organizados, sin organizar, partes de archivos organizados, agregar archivos sin seguimiento, y ver las diferencias de lo que se ha modificado.

Guardado Rápido y Limpieza.

Puedes estar trabajando en un proyecto dentro de una rama especifica, en este momento tienes tu código desordenado y todavía sin funcionar, ahora quieres cambiarte de rama, pero sin hacer un commit, porque no quieres confirmar un código que no esta funcionando, para esto existe el comando “stash”, esto te permite guardar tu trabajo para que te puedas mover a otra rama y cuando regreses puedas continuar trabajando sobre el código pendiente.

$ git stash

Para ver todos los stash que tienes guardados puedes usar el comando:

$ git stash list
El comando stash guarda solamente los archivos que se están rastreando, si acabas de crear un nuevo archivo y no lo has rastreado con “add” puedes guardarlo temporalmente con el comando:

$ git stash -u

Si quieres aplicar lo que guardaste para seguir trabajando puedes usar el comando:

$ git stash apply

Esto aplicara los cambios que habías hecho para que puedas seguir trabajando a partir de ahí, si quieres aplicar los cambio y al mismo tiempo eliminar el stash para que no se quede guardado un código sin funcionar puedes usar el comando:

$ git stash pop


Firmando tu trabajo
Git es criptográficamente seguro, por lo que, si estás trabajando con un repositorio de internet y quieres verificar si los commits son de fuentes seguras, tiene varias maneras de verificar y firmar utilizando GPG

Introducción a GPG
Para empezar a firmar con GPG necesitas generar una llave personal instalado, para eso tienes que ejecutar el siguiente comando.

$ gpg --gen-key

Ahora tienes que configurar tu llave privada para firmar, esto lo haces con el comando.

$ git config --global user.signingkey [llave]

Ahora Git usara tu llave por defecto para firmar tags y commits.

Firmando Tags
Para firmar un tag necesitas usar -s en lugar de -a

$ git tag -s nom_tag -m “Descripción”

Para ver tu firma GPG en el tag tienes que ejecutar el siguiente comando.

$ git show nom_tag

Verificando Tags
Para verificar un tag firmado usa el siguiente comando.

$ git tag -v nom_tag

Necesitas tener guardada la llave publica del usuario para que esto funcione de manera apropiada.

Firmando y Verificando commits
Para firmar un commit se tiene que agregar -S al comando de esta manera.

$ git commit -S -m “descripción”

Para verificar la firma del commit se usa el parámetro --show-signature en el comando “log” de esta manera

$ git log --show-signature



Buscando
A menudo necesitas buscar en dónde se define una función, o encontrar el historial de un método. Git tiene unas herramientas que examinan el código y hacen commit a unas instantáneas almacenadas en su base de datos de forma rápida.

Git Grep
El comando “grep” busca fácilmente a través de cualquier árbol o directorio de trabajo con commit por una cadena o expresión regular, el comando grep se usa de la siguiente manera

$ git grep -n [palabra]

Este comando va a buscar todas las líneas en las que aparezca la palabra que pasaste como parámetro y te dará una lista detallada con el directorio y archivo en los que encontró dicha coincidencia.

Para tener una salida más limpia existe un comando que te muestra que archivos coinciden y cuantas coincidencias hay en cada archivo, el comando es el siguiente.

$ git grep --count [palabra]

Las ventajas de hacer búsquedas con Grep es que es muy rápido y puede buscar a través de cualquier árbol.


Rerere

El nombre se refiere a “reuse recorded resolution”, te permite pedirle a Git que recuerde como solucionaste un problema de hunk para que cuando se vuela a presentar el problema Git lo resuelva automáticamente.

Para activar la funcionalidad de “rerere” tienes que ejecutar el siguiente comando.

$ git config –global rerere.enabled true

Cuando intentas fusionar dos ramas y te marca algún error, en lugar de ejecutar “git status” ejecuta el siguiente comando.

$ git rerere status

Este comando te dirá lo que ha registrado el estado pre-unión.

Si ya resolvimos un problema, la solución se guardará en el caché de rerere, cuando volvamos a tener un problema igual solo tenemos que ejecutar el siguiente comando para que quede solucionado.

$ git rerere
 

Haciendo debug con Git

Si encuentras un bug en tu código y quieras saber en que commit se introdujo, quien escribió esa parte del código y cuando, existe el comando “blame”, si le pasas como parámetro “-L” a este comando te da una lista detallada de cada línea de código de un rango especifico, este comando funciona de la siguiente manera, supongamos que tenemos un archivo que se llama file.txt y queremos saber quién ingreso las líneas de la 12 a la 22.

$ git blame -L 12,22 file.txt

Nos va a dar los primeros caracteres del SHA-1, nombre del autor, la fecha del commit y la línea del código.

Submódulos
Los submódulos le permiten mantener un repositorio de Git como un subdirectorio de otro repositorio de Git, esto le permite clonar otro repositorio en su proyecto y mantener sus commits separados.

Para crear un nuevo submódulo se ejecuta el comando “submodule add” con la URL del repositorio que quieres empezar a rastrear.

$ git submodule add https://github.com/chaconinc/DbConnector

Si ejecutas ahora el comando “git status” veras que aparece un archivo llamado .gitmodules, este archivo de configuración almacena la asignación entre la URL del proyecto y el subdirectorio local en el que lo ha insertado.
El siguiente archivo que aparece es la entrada de la carpeta del proyecto.

Para clonar un proyecto con submódulos se le tiene que pasar el parámetro “--recursive” al comando “git clone” para que inicie y actualice cada submódulo en el repositorio, ejemplo.

$ git clone --recursive https://github.com/chaconinc/MainProject

Para mantener el submódulo actualizado solamente ejecutas “git fetch” y “git merge origin/main”, esto va a actualizar el submódulo y lo va a fusionar con tu rama principal, estos comandos se tienen que ejecutar en el submódulo, no en tu proyecto principal.
Otra manera de mantener actualizado el submódulo es con el siguiente comando.

$ git submodule update --remote nom_submodule

Este comando asumirá de forma predeterminada que desea actualizar la rama main del repositorio de submódulos. Si no agrega el nombre del submódulo a ese comando y tiene varios submódulos en su proyecto, todos los submódulos se actualizarán.

Para subir los cambios que se hicieron en un submódulo se usa el siguiente comando.

$ git push --recurse-submodules=on-demand

Lo que hace este comando es entrar al submódulo y lo empuja antes de empujar el proyecto principal.


Conclusiones
Vimos varias herramientas avanzadas que permiten manipular tus commits y el área de staging de una manera más precisa, también aprendimos a solucionar errores comunes al fusionar dos ramas y el uso de submódulos.
