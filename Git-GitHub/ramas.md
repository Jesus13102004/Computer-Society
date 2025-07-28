<p align="center">
  <img src="https://git-scm.com/images/logo@2x.png" width="200" alt="Git Logo"/>
</p>

<h1 align="center"><code>Ramificaciones en Git</code></h1>


<h2>Introducción a las Ramificaciones en Git</h2>

<p>
Trabajar con <strong>ramificaciones</strong> significa que, a partir de una rama principal (<code>main</code>), se pueden crear diferentes flujos de trabajo. 
Cualquier sistema de control de versiones moderno incluye algún mecanismo para el uso de ramas. 
Sin embargo, en muchos de estos sistemas, trabajar con ramificaciones puede resultar costoso, ya que suele requerir una copia completa del código, lo cual puede consumir mucho tiempo y recursos, especialmente en proyectos grandes.
</p>

<p>
Git destaca por su <strong>rapidez</strong> en el manejo de ramificaciones. 
Este proceso es casi instantáneo, y tanto la creación de ramas como el cambio entre ellas (avanzar o retroceder) se realiza de forma extremadamente eficiente.
</p>

<p>
Comprender y utilizar adecuadamente las ramificaciones en Git te brinda una herramienta poderosa y versátil, capaz de transformar significativamente tu flujo de desarrollo.
</p>

---

<h2>¿Qué es una rama?</h2>

<p>
Antes de profundizar en el concepto de ramas, recordemos cómo Git almacena sus datos. A diferencia de otros sistemas de control de versiones, Git no guarda únicamente las diferencias entre archivos. En su lugar, Git guarda <strong>instantáneas completas</strong> de los archivos preparados en cada confirmación (<em>commit</em>).
</p>

<p>
Cada vez que se realiza una confirmación, Git calcula una suma de control (<em>checksum</em>) para cada archivo, guarda una copia de estos archivos en el repositorio (conocidos como <strong>blobs</strong>) y almacena las sumas de control en el área de preparación. 
Cuando haces cambios adicionales y vuelves a confirmar, esa nueva confirmación incluirá un <strong>apuntador</strong> que referencia a la confirmación anterior.
</p>

<p>
Una <strong>rama</strong> en Git es, en esencia, un <strong>apuntador móvil</strong> que señala a una de estas confirmaciones. Por convención, la rama principal por defecto en Git se llama <code>main</code>.
</p>


<h3>Crear una rama nueva</h3>

<p>
Cuando creas una rama nueva en Git, simplemente estás generando un nuevo <strong>apuntador</strong> que puede moverse libremente conforme avances en el desarrollo.
</p>

<p>
Supongamos que deseas crear una nueva rama llamada <code>testing</code>. Para ello, puedes utilizar el siguiente comando:
</p>

```bash
$ git branch testing
```

<p>
Este comando crea un nuevo apuntador que señala a la confirmación actual. Git determina en qué rama estás trabajando mediante un apuntador especial llamado <code>HEAD</code>. 
Es importante destacar que <code>git branch</code> solamente crea la rama, pero no cambia tu contexto actual a ella.
</p>

<p>
Para ver hacia qué confirmación apunta cada rama, puedes ejecutar:
</p>

```bash
$ git log --pretty=oneline --decorate
```

<p>Por ejemplo, podrías ver una salida como la siguiente:</p>

```bash
f30ab (HEAD, main, testing) add feature
34ac2 fixed bug
98ca9 initial commit
```

<p>
Esto indica que tanto la rama <code>main</code> como <code>testing</code> apuntan a la confirmación <code>f30ab</code>, y que actualmente estás trabajando sobre esa misma confirmación (por la presencia de <code>HEAD</code>).
</p>



<h3>Cambiar de rama</h3>

<p>Cambiar de rama en Git implica mover el apuntador especial <code>HEAD</code> a la rama deseada. Para hacerlo, se utiliza el siguiente comando:</p>

```bash
$ git checkout testing
```

<p>Esto mueve el apuntador <code>HEAD</code> a la rama <strong>testing</strong>. Si realizas una confirmación mientras estás en esta rama, verás que dicha rama avanza, pero la rama <code>main</code> permanece intacta.</p>

<p>Si deseas volver a la rama principal, usa el siguiente comando:</p>

```bash
$ git checkout main
```

<p>Esto ocasiona dos acciones importantes:</p>
<ul>
  <li>El apuntador <code>HEAD</code> se mueve nuevamente a la rama <code>main</code>.</li>
  <li>Los archivos del directorio de trabajo se revierten automáticamente al estado exacto de la última instantánea confirmada en la rama <code>main</code>.</li>
</ul>

<p>Cuando confirmas cambios en ramas distintas, estas comienzan a <strong>divergir</strong>, es decir, cada rama tendrá un historial de confirmaciones propio y aislado. Puedes saltar entre ramas sin perder los cambios confirmados en cada una.</p>

<p>Para visualizar de forma gráfica cómo se separan las ramas a medida que avanzas en el historial, puedes utilizar este comando:</p>

```bash
$ git log --oneline --decorate --graph --all
```

<div style="background-color: rgba(128,128,128,0.15); padding: 12px; border-left: 4px solid #888;">
  <strong>Dato técnico:</strong><br>
  Una rama en Git es simplemente un archivo que contiene el hash SHA-1 (40 caracteres) de una confirmación. Esto hace que <strong>crear y eliminar ramas en Git sea extremadamente ligero y rápido</strong>, una de las grandes ventajas frente a otros sistemas de control de versiones.
</div>

---

<h2>Procedimientos Básicos para Ramificar y Fusionar</h2>

<p>Para comprender mejor cómo funcionan las ramas en Git, vamos a simular un escenario típico de desarrollo en el que intervienen múltiples ramas.</p>

<p>Imagina que estás trabajando en un proyecto web y sigues la siguiente secuencia de pasos:</p>

<ol>
  <li>Estás desarrollando normalmente en la rama principal (<code>main</code>).</li>
  <li>Creas una nueva rama para trabajar en una funcionalidad o tema específico.</li>
  <li>Realizas algunas confirmaciones dentro de esta nueva rama.</li>
</ol>

<p>De pronto, recibes una llamada notificándote de un error crítico que debe ser resuelto de inmediato. Entonces haces lo siguiente:</p>

<ol start="4">
  <li>Regresas a la rama principal (<code>main</code>).</li>
  <li>Creas una nueva rama temporal para trabajar exclusivamente en la solución del error.</li>
  <li>Solucionas el error dentro de esa nueva rama.</li>
  <li>Fusionas la rama de corrección con la rama principal usando <code>git merge</code>.</li>
  <li>Envías los cambios corregidos al servidor remoto con <code>git push</code>.</li>
  <li>Finalmente, vuelves a la rama en la que estabas trabajando inicialmente para continuar tu desarrollo.</li>
</ol>

<div style="background-color: rgba(128,128,128,0.12); padding: 10px; border-left: 4px solid #888;">
  <strong>Tip:</strong> Esta estrategia de ramificación es muy común en flujos de trabajo colaborativos. Permite aislar desarrollos y correcciones sin afectar la estabilidad del proyecto principal.
</div>


<h3>Procedimiento Básico de Ramificación</h3>

<p>Imagina que estás trabajando en un proyecto y ya tienes varias confirmaciones realizadas. En cierto punto, decides crear una nueva rama para solucionar el error <strong>#53</strong>. Para crear esa rama y cambiarte automáticamente a ella, puedes usar el siguiente comando:</p>

```bash
$ git checkout -b iss53
Switched to a new branch 'iss53'
```

<p>Empiezas a trabajar en la rama <code>iss53</code> y haces varias confirmaciones. De esta forma, esa rama va avanzando independientemente de la rama principal.</p>

<p>Mientras estás trabajando, te notifican que hay un error urgente en el sitio web que debes solucionar inmediatamente. Para evitar mezclar tu trabajo actual con los cambios del nuevo error, simplemente regresas a la rama principal y creas una nueva rama a partir de ella.</p>

<div style="background-color: rgba(128,128,128,0.12); padding: 10px; border-left: 4px solid #888;">
  <strong>Advertencia:</strong> Si tienes cambios sin confirmar en tu directorio de trabajo, Git no te permitirá cambiar de rama. Asegúrate de confirmarlos o almacenarlos temporalmente con <code>git stash</code>.
</div>

<p>Una vez en la rama principal (<code>main</code>), el directorio de trabajo vuelve a estar como estaba antes de comenzar con el error <code>#53</code>. Entonces creas una nueva rama llamada <code>hotfix</code> para resolver el problema urgente:</p>

```bash
$ git checkout -b hotfix
```

<p>Después de realizar varias pruebas y resolver el problema, necesitas incorporar esos cambios en la rama principal. Para ello, primero cambias a la rama <code>main</code> y luego haces un <strong>merge</strong>:</p>

```bash
$ git checkout main
$ git merge hotfix
```

Updating f42c576..3a0874c
Fast-forward
 Index.html | 2 ++
 1 file changed, 2 insertions(+)


<p>Cuando Git puede avanzar el puntero de la rama directamente porque no hay divergencias, realiza un <strong>fast-forward</strong>. Esto simplifica el historial de confirmaciones.</p>

<p>Después de haber fusionado los cambios, es buena práctica eliminar la rama <code>hotfix</code> si ya no la necesitas:</p>

```bash
$ git branch -d hotfix
```

<p><strong>Nota:</strong> Los cambios realizados en <code>hotfix</code> no se verán reflejados en la rama <code>iss53</code>, ya que se realizaron en paralelo. Si deseas traer esos cambios, puedes hacerlo desde <code>iss53</code> con:</p>

```bash
$ git checkout iss53
$ git merge main
```

<h3>Procedimientos Básicos de Fusión</h3>

<p>Supongamos que ya terminaste de trabajar en la rama <code>iss53</code> que resolvía el error <strong>#53</strong>. Al igual que hicimos con la rama <code>hotfix</code>, ahora vas a fusionar el contenido de <code>iss53</code> con la rama principal <code>main</code>. Para hacerlo, ejecuta los siguientes comandos:</p>

<pre><code>$ git checkout main
Switched to branch 'main'

```bash
$ git merge iss53
Merge made by the 'recursive' strategy.
 index.html | 1 +
 1 file changed, 1 insertion(+)
```

<p>En este caso, los registros de desarrollo de ambas ramas divergieron desde un punto anterior. Git realizará automáticamente una <strong>fusión a tres bandas</strong> (three-way merge), utilizando:</p>
<ul>
  <li>La instantánea final de cada una de las ramas</li>
  <li>El ancestro común de ambas ramas</li>
</ul>

<p>En lugar de simplemente avanzar el puntero de la rama como en un <em>fast-forward</em>, Git crea una nueva instantánea resultado de la combinación de los cambios y genera automáticamente una nueva confirmación de fusión.</p>

<div style="background-color: rgba(128,128,128,0.12); padding: 10px; border-left: 4px solid #888;">
  <strong>Tip:</strong> Git determina de forma automática cuál es el mejor ancestro común entre ambas ramas para hacer la fusión, lo cual elimina errores y decisiones manuales que en otros sistemas quedan a criterio del desarrollador.
</div>

<p>Una vez fusionadas ambas ramas y confirmados los cambios, puedes eliminar la rama <code>iss53</code> si ya no la necesitas:</p>

```bash
$ git branch -d iss53
```


<h3>Principales Conflictos que Pueden Surgir en las Fusiones</h3>

<p>
Cuando existen modificaciones distintas en una misma sección de un archivo en las ramas que deseas fusionar, Git no podrá realizar la fusión automáticamente y mostrará un mensaje de error como este:
</p>

```bash
$ git merge iss53
Auto-merging index.html
CONFLICT (content): Merge conflict in index.html
Automatic merge failed; fix conflicts and then commit the result


<p>
En estos casos, Git pausa la operación de fusión y espera a que tú resuelvas manualmente los conflictos. Para identificar qué archivos están en conflicto puedes utilizar el comando <code>git status</code>, el cual te mostrará algo como:
</p>

```bash
$ git status
On branch main
You have unmerged paths
  (fix conflicts and run “git commit”)

Unmerged paths:
  (use “git add &lt;file&gt;…” to mark resolution)
  
    both modified:   index.html

no changes added to commit (use “git add” and/or “git commit -a”)
```

<p>
Los archivos en conflicto se marcarán como <strong>unmerged</strong>. Git inserta marcas especiales dentro de los archivos afectados para ayudarte a localizar y resolver los conflictos. Al abrir el archivo con un conflicto, verás algo como esto:
</p>

```bash
&lt;&lt;&lt;&lt;&lt;&lt;&lt; HEAD:index.html
&lt;div id="footer"&gt;contact : email.support@github.com&lt;/div&gt;
=======
&lt;div id="footer"&gt;
  Please contact us at support@github.com
&lt;/div&gt;
&gt;&gt;&gt;&gt;&gt;&gt;&gt; iss53:index.html
```

<p>
Esto indica que la versión actual (HEAD) contiene el bloque superior, mientras que la rama <code>iss53</code> tiene el bloque inferior. Tú debes decidir con cuál versión quedarte o cómo combinar ambas.
</p>

<div style="border-left: 4px solid #aaa; padding: 0.5em; background-color: rgba(200,200,200,0.15); margin: 1em 0;">
<strong>Nota:</strong> Una vez que hayas resuelto el conflicto, guarda los cambios, utiliza <code>git add</code> para marcar el archivo como resuelto y luego realiza un <code>git commit</code> para finalizar la fusión.
</div>

---


<h2>Gestión de ramas</h2>

<p>Vamos a ver algunas herramientas de gestión muy útiles cuando comienzas a utilizar ramas de manera más avanzada.</p>

<p>El comando <code>branch</code> tiene varias funciones que veremos a continuación:</p>

<ul>
  <li><strong>Listar ramas:</strong> Si ejecutas el comando sin ningún parámetro, te muestra la lista de las ramas que tienes en el proyecto:</li>
</ul>

```bash
$ git branch
  iss53
* main
  testing
```

<p>El símbolo <code>*</code> indica la rama a la que apunta actualmente <code>HEAD</code>.</p>

<ul>
  <li><strong>Ver últimas confirmaciones:</strong> Para ver la última confirmación registrada en cada rama, se usa el comando:</li>
</ul>

```bash
$ git branch -v
  iss53     93b412c fix javascript issue
* main      7a98805 Merge branch iss53
  testing   782fd34 add Scott to the author
```

<ul>
  <li><strong>Ramas fusionadas o no fusionadas:</strong> Para ver cuáles ramas ya han sido fusionadas o cuáles aún no, puedes usar los siguientes comandos:</li>
</ul>

```bash
$ git branch --merged
$ git branch --no-merged
```

---

<h2>Flujos de trabajo Ramificados</h2>

<p>Ahora que ya conoces los procedimientos básicos de ramificación y fusión, es momento de explorar algunos de los <strong>flujos de trabajo más comunes</strong> en proyectos que utilizan Git.</p>

<p>Estos flujos te ayudarán a organizar mejor tus procesos de desarrollo, facilitar la colaboración en equipo y mantener un historial limpio y estructurado. A continuación, revisaremos distintos enfoques para que puedas evaluar cuál se adapta mejor a tu proyecto y decidir si deseas incorporarlo en tu ciclo de desarrollo.</p>


<h3>Ramas de largo contenido</h3>

<p>Podrías imaginar las ramas como <strong>silos de almacenamiento</strong>, donde las confirmaciones van siendo promovidas hacia silos más estables a medida que son probadas y depuradas.</p>

<p>Este enfoque se puede extender para reflejar distintos grados de estabilidad. Por ejemplo, en proyectos grandes es común encontrar una rama llamada <code>proposed-updates</code>, que actúa como contenedor de todas las integraciones provenientes de otras ramas, pero que aún no están listas para incorporarse a la rama principal.</p>

<p>La idea general consiste en <strong>mantener múltiples ramas con distintos niveles de estabilidad</strong>. Cuando una rama alcanza un nivel suficiente de confianza y solidez, se fusiona con la siguiente rama "superior" en el flujo de trabajo.</p>

<p>Este modelo resulta especialmente útil en proyectos <strong>de larga duración y alta complejidad</strong>, donde mantener un control riguroso sobre el código en producción es esencial.</p>

<img src="https://blog.softtek.com/hs-fs/hubfs/blogs/innovationlabs/4-1.png?width=1100&name=4-1.png" alt="Flujo de ramas de largo contenido" width="600"/>



<h3>Ramas Puntuales</h3>

<p>
Las ramas puntuales son útiles en proyectos de cualquier tamaño. Se trata de ramas que se crean para trabajar en una tarea específica y se eliminan una vez finalizada. Por lo general, son de corta duración.
</p>

<p>
Esta técnica permite realizar cambios aislados de forma rápida y organizada. Al tener los cambios contenidos dentro de una rama, resulta mucho más sencillo revisar y validar el código. Puedes mantener estos cambios el tiempo que necesites y fusionarlos con la rama principal solo cuando estén completamente listos.
</p>

<div class="note">
<strong>Nota:</strong> Todas las ramas son completamente locales. Cuando creas, cambias o fusionas ramas, todo sucede en tu repositorio local de Git. No se establece ninguna comunicación con un servidor remoto a menos que realices una acción como <code>push</code> o <code>fetch</code>.
</div>

<img src="https://mascandobits.es/blog/wp-content/uploads/2021/03/git_develop_flow.png" alt="Flujo de ramas puntuales en Git" width="600"/>



<h3>Ramas Remotas</h3>

<p>
Las ramas remotas son referencias a ramas que existen en un repositorio remoto, como puede ser GitHub, GitLab o Bitbucket. Aunque técnicamente se almacenan en tu repositorio local, no puedes desplazarte directamente a ellas ni modificarlas como lo harías con una rama local. Se actualizan automáticamente cada vez que realizas una operación de red como <code>git fetch</code> o <code>git pull</code>.
</p>

<p>
Estas ramas sirven como marcadores de referencia que indican el último estado conocido de una rama remota. Por ejemplo, si clonas un repositorio desde GitHub, verás ramas como <code>origin/main</code>, <code>origin/dev</code>, etc. Estas no son ramas locales, pero puedes usarlas como base para crear las tuyas propias.
</p>

<div class="note">
<strong>Consejo:</strong> Las ramas remotas no se actualizan automáticamente con los cambios hechos en el servidor. Es buena práctica ejecutar <code>git fetch</code> con regularidad para mantener tus referencias remotas sincronizadas.
</div>

<img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhDdpSASI_4s8-6wo5Y-H-b0fuE74Pgx-meKA9UscEryTct3diK_UHiQGEpdQHIpww8mWc8wtpFIIsutKqgsZlWchL11vH6axQLAfHSso2MFE8XWYVtXM8VNI6F35PElXaCPwAtpM2VGOwc/s1600/trabajo-git.jpg" alt="Ramas remotas en Git" width="600"/>

---











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
 


