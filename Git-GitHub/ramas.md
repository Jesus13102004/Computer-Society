Ramificaciones en Git
Trabajar con ramificaciones significa que a partir de una rama principal (main) se van creando diferentes flujos de trabajo, cualquier sistema de versiones moderno tiene algún mecanismo que soporta el uso de ramas, pero este suele ser muy costoso por que a menudo requiere una nueva copia del código y en proyectos grandes puede tomar mucho tiempo.
Git destaca por su rapidez al manejar ramificaciones al hacer este proceso casi instantáneo, hace todas las operaciones de ramificación al igual que el avance o retroceso entre distintas ramas tremendamente rápido.
Entender y manejar las ramificaciones te proporciona una poderosa y exclusiva herramienta que puede cambiar la forma en la que desarrollas.

¿Qué es una rama?

Empezaremos recordando como git almacena sus datos, no los almacena guardando solo diferencias, sino que los almacena como copias puntuales de los archivos completos.
En cada confirmación de datos Git almacena una instantánea de los archivos preparados, realiza una suma de control de cada uno de ellos, almacena una copia de cada uno en el repositorio (“blobs”) y guarda cada suma de control en el área de preparación.
Si haces más cambios y vuelves a confirmar, la siguiente confirmación guardara un apuntador a su confirmación precedente.

Una rama en Git es simplemente un apuntador móvil apuntando a una de esas confirmaciones, la rama principal por defecto de Git es “main”

Crear una rama nueva

Cuando creas una rama nueva simplemente se crea un apuntador para que se pueda mover libremente.
Supongamos que quieres crear una nueva rama llamada “testing”, para esto usamos el comando:

$ git branch testing

Esto crea un apuntador apuntando a la confirmación donde estés actualmente.
Git identifica en que rama estas en cada momento por el apuntador especial HEAD, el comando “Branch” solo crea la rama, pero no salta a dicha rama.
Para saber a dónde apunta cada rama se puede hacer lo siguiente:

$ git log  --pretty=oneline --decorate
f30ab (HEAD, main, testing) add feature
34ac2 fixed bug
98ca9 initial commit

Esto quiere decir que la rama “main” y la rama “testing” están junto a la confirmación f30ab.

Cambiar de Rama

Para saltar de rama se usa el comando:

$ git checkout testing

Esto mueve el apuntador HEAD a la rama testing, si hacemos una confirmación estando en la rama “testing” veremos que la rama avanza, pero la rama main no se mueve.

Si regresamos a la rama principal con este comando:

$ git checkout main

Van a pasar dos cosas, primero el apuntador HEAD se mueve a la rama main y segundo, revierte los archivos del directorio de trabajo dejándolos justo como estaban en la última instantánea confirmada en donde se encuentra la rama main.

Si creamos una confirmación dentro de la rama main veremos que las ramas van a comenzar a divergir, los cambios realizados en cada rama están aislados, puedes saltar de una a otra según estimes oportuno.

Para ver gráficamente como se van separando las ramas conforme vayas haciendo confirmaciones puedes ocupar este comando.

$ git log --online --decorate --graph --all

Debido a que una rama en Git es simplemente un archivo que contiene los 40 caracteres de una suma de control, no cuesta nada el crear y eliminar ramas en Git.


Procedimientos Básicos para Ramificar y Fusionar

Para explicar a detalle el funcionamiento de las ramas vamos a simular un escenario de la vida real.
Imagina que sigues estos pasos:
-	Trabajas en un sitio web
-	Creas una rama para un nuevo tema sobre el que estás trabajando
-	Realizas algo de trabajo en esa rama
Recibes una llamada en la que te avisan que hay un error critico que tienes que resolver y haces lo siguiente:
-	Vuelves a la rama principal
-	Creas una nueva rama para trabajar sobre el error
-	Después de resolverlo fusionas esa rama con la rama principal y envías los cambios al servidor
-	Regresas a la rama en la que estabas trabajando inicialmente

Procedimiento Básico de Ramificación
 Imagina que estás trabajando en un proyecto y ya tienes varias confirmaciones, decides crear una nueva rama para solucionar el error #53, Para crear una nueva rama y saltar automáticamente puedes usar este comando:

$ git checkout -b iss53
Switched to a new branch “iss53”

Trabajas en el error y haces varias confirmaciones, con ello la rama “iss53” va avanzando.

Mientras estas trabajando en esa rama te notifican que hay un error en el sitio web que tienes que solucionar inmediatamente, para no mezclar tus cambios con los del nuevo error o deshacer todo tu trabajo para solucionar el error que te están notificando simplemente regresas a la rama principal y empiezas a trabajar a partir de allí.
Advertencia. Si tienes cambios que no han sido confirmados git no te permitirá cambiar de rama.

Al estar en la rama principal tendrás el directorio tal y como estaba antes de empezar a trabajar con el error #53, creas otra rama llamada “hotfix” en la que resolverás el problema.
Después de haber hecho varias pruebas y tener el problema solucionado necesitas incorporar esos cambios sobre la rama principal, para esto tienes que saltar a la rama principal y hacer un “merge” de esta forma:

$ git checkout main
$ git merge hotfix
Updating f42c576..3ª0874c
Fast-forward
   Index.html | 2 ++
   1 file changed, 2 insertions (+)

Cuando fucionas dos confirmaciones git simplifica las cosas avanzando el puntero, ya que no hay otro trabajo divergente a fusionar, a esto se le denomina “fast-forward”.
Después de haber resuelto el problema y haberlo fusionado con la rama principal es importante eliminar la rama ya que no la vamos a necesitar más puesto que apunta exactamente a la rama main, para esto usamos el comando:

$ git branch -d hotfix

Nota: El trabajo realizado en la rama hotfix no está en los archivos de la rama iss53, si es necesario fusionarlos te puedes posicionar en la rama iss53 y usar el comando

$ git merge main

Procedimientos Básicos de Fusión

Supongamos que ya terminaste de trabajar con el error #53, al igual que como lo hicimos con la rama hotfix vamos a fusionar el contenido de la rama “iss53” con la rama “main”, para esto ejecutamos los siguientes comandos

$ git checkout main
switched to Branch “main”
$ git merge iss53
merge made by the “recursive” strategy.
index.html |	1 +
1 file changed, 1 insertion (+)

En este caso el registro de desarrollo había divergido en un punto anterior, Git realizara una fusión a tres bandas, utilizando las dos instantáneas apuntadas por el extremo de cada una de las ramas y por el ancestro común a ambas.
En lugar de simplemente avanzar el apuntador a la rama, Git crea una nueva instantánea resultado de la fusión a tres bandas y crea automáticamente una nueva confirmación de cambios

Git es quien determina automáticamente quien es el mejor ancestro común para realizar la fusión, a diferencia de otros sistemas donde es el desarrollador quien determina cual puede ser el mejor ancestro común.

Ya que fusionaste las dos ramas ya puedes eliminar la rama “iss53”

Principales Conflictos que Pueden Surgir en las Fusiones

Si hay modificaciones dispares en una misma porción de un mismo archivo en las dos ramas distintas que deseas fusionar Git no será capaz de fusionarlas directamente y aparecerá un error asi:

$ git merge iss53
Auto-merging index.html
CONFLICT (content): Merge conflicto in index.html
Automatic merge failed; fix conflicts and then commit the result

Git no crea automáticamente una nueva fusión, hace una pausa en el proceso esperando a que tú lo soluciones. Para ver que archivos no se están fusionando se usa el comando “status” y muestra algo así:

$ git status
On branch main
You have unmerged paths
   (fix conflicts and run “git commit”)

Unmerged paths:
   (use “git add <file>…” to mark resolution)
       
        Both modified:           index.html

no changes added to commit (use “git add” and/or  “git commit -a”)  

Todos los archivos que estén causando problemas se marcaran como (unmerged), Git añade a los archivos unos marcadores especiales de resolución de conflictos que te guiaran cuando abras los archivos y se verán algo así:

<<<<<<< HEAD:index.html
<div id= “footer”>contact : email.support@github.com</div>
= = = = = = = 
<div id= “footer”>
  Please contact us at support@github.com
</div>
>>>>>>>  iss53:index.html

Esto indica que la version en HEAD contiene lo que esta encima de (= = = = = = =) y la version de iss53 es la que esta abajo, tu tienes que elegir manualmente con cual te quieres quedar 



Gestion de ramas

Vamos a ver algunas herramientas de gestion muy utiles cuando comienzas a utilizar ramas de manera avanzada

El comando branch tiene mas funciones que veremos a continuacion:
-	Si ejecutas el comando sin ningún parámetro te da la lista de las ramas que tienes en el proyecto

$ git branch
iss53
*main
testing 

El (*) muestra la rama a la que apunta HEAD

-	Para ver la última confirmación de cada rama se usa el comando:

$ git branch -v
     iss53 93b412c fix javascript issue
     *main 7ª98805 Merge branch iss53
     testing 782fd34 add scott to the autor

-	Para ver las ramas que han sido fusionadas o las que no existen dos comandos
$ git branch --merged
$ git branch --no-merged



Flujos de trabajo Ramificados

Ya que has visto los procedimientos básicos de ramificacion y fusión, vamos a ver algunos de los flujos de trabajo más comunes, de tal forma que puedas decidir si te gustaria incorporar alguno de ellos a tu ciclo de desarrollo.

Ramas de largo contenido

Podria ser mas sencillo pensar en las ramas como si fueran silos de almacenamiento, donde las confirmaciones van siendo promocionadas hacia silos mas estables a medida que son probados y depurados.
Este sistema de trabajo se puede ampliar para diversos grados de estabilidad, algunos proyectos grandes suelen tener una ramma llamada “proposed updates” en donde esta todo lo integrado por otras ramas pero que aun no esta listo para ser incorporado a la rama principal.
La idea es siempre mantener diversas ramas en diversos grados de estabilidad; pero cuando una alcance un grado mas estable se fuciona con la rama inmediatamente superior a ella.
Las ramas de larga duracion son mas practicas y utiles en proyectos largos y complejos


Ramas Puntuales

Las ramas puntuales son útiles en proyectos de cualquier tamaño, una rama puntual es una rama que se abre para trabajar en algo especifico y despues se cierra, por lo general son de corta duracion.
Esta tecnica te ayuda a realizar cambios de contecto rapidos y completos, al estar todos los cambios seccionados en cada rama sera mas sencillo revisar el codigo, puedes tener los cambios el tiempo que sea y fucionarlos cuando realmente esten terminados


Nota: Es importante recordar que todas las ramas son completamente locales, cuando ramificas y fusionas todo se realiza en el repositorio Git, no hay ninguna comunicación con un servidor



Ramas Remotas
Son ramas locales que no puedes mover, se mueven automaticamente cuando estableces comunicación en la red.
Funcionan como marcadores para recordarte en que estado se encontraban tus repositorios remotos la ultima vez que te conectaste a ellos.
#Agregar mas informacion


Publicar

Si quieres compartir tu rama tienes que hacerle un push hacia un remoto donde tengas permisos de escritura. Las ramas locales no se sincronizan automaticamente con los remotos en los que escribes, sino que se tienen que mandar expresamente las ramas que deseas compartir.
De esta manera puedes tener ramas privadas que no deseas compartir, llevando a un remoto solo las que quieres compartir
El comando para enviar una rama al servidor es :

$ git push nom_remote branch 

Cuando recuperas una rama remota no obtienes una copia local editable, solo tienes un puntero no editable a “remote/rama”

Si quieres integrar tu rama remota a tu trabajo actual usa el comando

$ git merge remote/rama

Y si quieres tener tu propia rama para trabajar puedes crearla basandote en la rama remota.

$ git checkout -b rama remote/rama

Esto te da una rama local en la que puedes trabajar que inicia en donde remote/rama estaba en ese momento


Hacer Seguimiento a las Ramas

Al activar una rama local a traves de una rama remota se crea automaticamente una “rama de seguimiento”
Las ramas de seguimiento son ramas locales que tienen relacion cirecta con una rama remota y al usar el comando “pull” Gita sabe de que servidor recuperar y fusionar datos.
Cuando clonas un repositorio se crea la rama main que hace segimiento de origin/main, sin embargo puedes crear mas ramas de seguimiento, esta operación es tan comun que git ofrece el parametro –track

$ git checkout --track remote/rama
Explicar que hace el parametro --track

Si ya tienes una rama local y quieres asignarla a una rama remota que acabas de traer o quieres cambiar la rama a la que le hace seguimiento puedes usar el comando:

$ git branch -u origin/serverfix
Branch serverfix set up to track remote branch serverfix from origin
 
Si quieres ver las ramas de seguimiento que tienes asignadas puedes usar el comando:

$ git branch -vv

Esto listara tus ramas locales con mas informacion incluyendo a que sigue cad rama y si tu rama esta por delante, por detrás o ambas


Traer y Fusionar

Para traer y fusionar los cambios que no has recuperado del servidor existen dos maneras, la primera e como ya lo habiamos visto, utilizando los ccomandos “git fetch” para traer los daros del servidor y “git merge” para fusionar los datos, pero existe un comando que hace las dos cosas al mismo tiempo y ese es el comando:

$ git pull

Aunque este comando simplifica el proceso es mas recomendado hacer el proceso completo, ya que el resultado de “git pull” puede ser confuso.


Eliminar ramas remotas

Al igual que las ramas locales despues de fusionarlas con tu rama principal es necesario eliminarla ya que no se volvera a usar, para eliminar la rama remota se usa el parametro “--delete” del comando “git push”, por ejemplo si quieres eliminar una rama que se llame serverfix se usa el siguiente comando:

$ git push --delete serverfix

Lo que hace este comando es eliminar el apuntador al servidor, el servidor Git suele almacenar los datos por un tiempo asi que si la eliminaste por error suele ser facil recuperarla



Reorganizar el Trabajo Realizado
En Git existen dos formas de integrar los cambios, una de ellas es fusionando (merged) y la otra es reorganizando (rebase): Veremos en que consiste la reorganizacion y en que casos no es conveniente usarla.


Reorganizacion Basica
Se trata de capturar los cambios introducidos en una confirmacion de una rama y replicarlos en la confirmacion de otra, un ejemoplo de uso es el siguiente:

$ git checkout experiment
$ git rebase master

Esto hace que git vaya al ancestro comun de ambas ramas, saque las diferencias introducidas por cada confirmacion en la rama en la que estas, guarde esas diferencias en archivos temporales, reinicie la rama actual hasta llevarla a la misma confirmacion que la rama de donde quieres reorganizar y finalmente vuelva aplicar ordenadamente los cambios.
Ahora ya puedes regresar a la rama main y ejecutar el comando “git merge”

$ git checkout main
$ fit merge experiment

Si examinas el historial de una rama reorganizada, veras que aparece en forma lineal como si todo se hubiera realizado en serie, pero realmente se realizo en paralelo


Los Peligros de Reorganizar

Nota:Nunca reorganices confirmaciones que hayas enviado a un repositorio publico.

Cuando reorganizas algo se borran las confirmaciones ya creadas y se crean unas nuevas que son similares pero diferentes. Si envias una confirmacion al servidor y alguien la recoje de ahí y despues tu las reescribes con “git rebase” y las vuelves a enviar, los colaboradores tendran que refusionar su trabajo y todo se volvera complicado cuando intentes recoger su trabajo de vuelta sobre el tuyo


Conclusiones
Aprendimos los procedimientos basicos de ramificacion y fusion, ya podras crear nuevas ramas, saltando entre ramas para trabajar y fusionando ramas entre ellas. Tambien sabras como compartir tus ramas enviandolas a un servidor, como trabajar colaborativamente en ramas compartidas y como reorganizar tus ramas antes de compartirlas
 


