<p align="center">
  <img src="https://git-scm.com/images/logo@2x.png" width="200" alt="Git Logo"/>
</p>

<h1 align="center"><code>Ramificaciones en Git</code></h1>


<h2>Introducción a las Ramificaciones en Git</h2>

<p>
Trabajar con <strong>ramificaciones</strong> significa que a partir de una rama principal (<code>main</code>), se pueden crear diferentes flujos de trabajo. 
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


Updating f42c576..3a0874c
Fast-forward
 Index.html | 2 ++
 1 file changed, 2 insertions(+)
```

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

```bash
$ git checkout main
Switched to branch 'main'

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
```

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
<<<<<<< HEAD:index.html
<div id="footer">;contact : email.support@github.com</div>;
=======
<div id="footer">;
  Please contact us at support@github.com
</div>;
>>>>>>> iss53:index.html
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

---

<h2>Ramas Remotas</h2>

<p>
Las ramas remotas son referencias a ramas que existen en un repositorio remoto, como puede ser GitHub, GitLab o Bitbucket. Aunque técnicamente se almacenan en tu repositorio local, no puedes desplazarte directamente a ellas ni modificarlas como lo harías con una rama local. Se actualizan automáticamente cada vez que realizas una operación de red como <code>git fetch</code> o <code>git pull</code>.
</p>

<p>
Estas ramas sirven como marcadores de referencia que indican el último estado conocido de una rama remota. Por ejemplo, si clonas un repositorio desde GitHub, verás ramas como <code>origin/main</code>, <code>origin/dev</code>, etc. Estas no son ramas locales, pero puedes usarlas como base para crear las tuyas propias.
</p>

<div class="note">
<strong>Consejo:</strong> Las ramas remotas no se actualizan automáticamente con los cambios hechos en el servidor. Es buena práctica ejecutar <code>git fetch</code> con regularidad para mantener tus referencias remotas sincronizadas.
</div>




<h3>Publicar</h3>

<p>
Si deseas compartir tu trabajo con otros, necesitas publicar tu rama local enviándola a un repositorio remoto en el que tengas permisos de escritura. Git no sincroniza automáticamente tus ramas locales con los remotos; tú decides explícitamente qué ramas enviar.
</p>

<p>
Esto permite mantener ramas privadas en tu entorno local y publicar únicamente aquellas que realmente deseas compartir. Para enviar una rama al servidor remoto, utiliza el siguiente comando:
</p>

```bash
$ git push nombre_remoto nombre_rama
```

<p>
Cuando clonas o haces <code>git fetch</code>, Git trae las ramas remotas, pero no las convierte en ramas locales editables. En su lugar, crea un apuntador de solo lectura como <code>origin/rama</code>.
</p>

<p>
Si deseas incorporar esa rama remota a tu trabajo actual sin editarla directamente, puedes hacer un merge:
</p>

```bash
$ git merge origin/rama
```

<p>
Y si quieres trabajar con una copia editable basada en la rama remota, puedes crear una nueva rama local desde ella con:
</p>

```bash
$ git checkout -b mi-rama origin/rama
```

<div class="note">
<strong>Nota:</strong> Las ramas remotas funcionan como referencia, pero todo el trabajo y las confirmaciones deben realizarse en una rama local. Solo entonces podrás publicar tus avances con <code>git push</code>.
</div>




<h3>Hacer Seguimiento a las Ramas</h3>

<p>
Al activar una rama local a partir de una rama remota, Git crea automáticamente una <strong>rama de seguimiento</strong>. Estas ramas locales tienen una relación directa con su contraparte remota, lo que permite que, al usar el comando <code>git pull</code>, Git sepa desde qué servidor recuperar y fusionar los datos.
</p>

<p>
Cuando clonas un repositorio, se crea por defecto la rama <code>main</code>, que realiza seguimiento a <code>origin/main</code>. Sin embargo, puedes crear otras ramas de seguimiento. Esta operación es tan común que Git proporciona un parámetro específico para ello: <code>--track</code>.
</p>

```bash
$ git checkout --track remote/rama
```

<div class="note">
<strong>Nota:</strong> El parámetro <code>--track</code> crea una nueva rama local que sigue automáticamente a la rama remota especificada.
</div>

<p>
Si ya tienes una rama local y deseas asignarle una rama remota existente como destino de seguimiento, o deseas cambiarla, puedes usar el siguiente comando:
</p>

```bash
$ git branch -u origin/serverfix
Branch serverfix set up to track remote branch serverfix from origin
```

<p>
Para ver todas las ramas de seguimiento que tienes configuradas, puedes utilizar:
</p>

```bash
$ git branch -vv
```

<p>
Este comando listará tus ramas locales junto con información adicional, incluyendo la rama remota que siguen y si están adelantadas, atrasadas o ambas con respecto a ella.
</p>



<h3>Traer y Fusionar</h3>

<p>
Para obtener y fusionar los cambios más recientes desde el servidor, existen dos formas de hacerlo:
</p>

<ol>
  <li>
    Usar el comando <code>git fetch</code> para traer los datos desde el servidor.
  </li>
  <li>
    Luego, emplear <code>git merge</code> para fusionar esos datos en tu rama actual.
  </li>
</ol>

<p>
Sin embargo, existe un comando que combina ambos pasos en uno solo:
</p>

```bash
$ git pull
```

<div class="note">
<strong>Consejo:</strong> Aunque <code>git pull</code> simplifica el proceso, se recomienda realizar ambos pasos por separado (<code>fetch</code> y <code>merge</code>). Esto te da mayor control sobre los cambios y evita confusiones, ya que el comportamiento de <code>git pull</code> puede no ser del todo claro si hay conflictos o diferencias inesperadas.
</div>


<h3>Eliminar ramas remotas</h3>

<p>
Al igual que con las ramas locales, una vez que se ha fusionado una rama remota con la rama principal y ya no se utilizará, lo ideal es eliminarla para mantener limpio el repositorio. 
</p>

<p>
Para eliminar una rama remota se utiliza el parámetro <code>--delete</code> del comando <code>git push</code>. Por ejemplo, si deseas eliminar una rama llamada <code>serverfix</code>, debes ejecutar:
</p>

```bash
$ git push origin --delete serverfix
```

<div class="warning">
<strong>Nota:</strong> Este comando elimina el apuntador a la rama en el servidor remoto. Los servidores Git suelen conservar los datos durante un tiempo, por lo que si la rama fue eliminada por error, puede ser relativamente sencillo recuperarla si se actúa pronto.
</div>

---

<h2>Reorganizar el Trabajo Realizado</h2>

<p>
En Git existen dos formas principales de integrar los cambios de una rama en otra: la <strong>fusión</strong (<em>merge</em>) y la <strong>reorganización</strong (<em>rebase</em>). 
</p>

<p>
En esta sección exploraremos en qué consiste el comando <code>rebase</code>, cómo funciona y en qué casos <strong>no es recomendable</strong> utilizarlo.
</p>


<h3>Reorganización Básica</h3>

<p>
La reorganización (<em>rebase</em>) consiste en tomar las confirmaciones de una rama y aplicarlas sobre otra, como si hubieran sido creadas en secuencia. 
Este proceso es útil para mantener un historial lineal y limpio, especialmente cuando trabajas con ramas paralelas.
</p>

<p>
Un ejemplo típico de uso es el siguiente:
</p>

```bash
$ git checkout experiment
$ git rebase master
```

<p> Este comando realiza los siguientes pasos: </p> 
<ul> 
   <li>Git identifica el ancestro común entre <code>experiment</code> y <code>master</code>.</li> 
   <li>Extrae las diferencias generadas por cada confirmación en <code>experiment</code> desde ese punto común.</li> 
   <li>Guarda temporalmente esos cambios.</li> 
   <li>Reinicia la rama <code>experiment</code> para que comience desde la última confirmación de <code>master</code>.</li> 
   <li>Aplica, una por una, las confirmaciones guardadas sobre la nueva base.</li> 
</ul> 
<p> Una vez finalizado el rebase, puedes volver a la rama <code>main</code> y fusionar los cambios: </p>

```bash
$ git checkout main
$ git merge experiment
```

<p> Si revisas el historial después del <code>rebase</code>, notarás que las confirmaciones aparecen en línea recta, como si todo el trabajo se hubiera realizado en serie, aunque en realidad se desarrolló en paralelo. </p>

<h3>Los Peligros de Reorganizar</h3>

<div class="nota">
  <strong>Nota:</strong> <em>Nunca reorganices confirmaciones que ya hayas enviado a un repositorio público.</em>
</div>

<p>
El uso de <code>git rebase</code> puede traer complicaciones serias si se aplica sobre confirmaciones que ya han sido compartidas con otros colaboradores. Al reorganizar, Git elimina las confirmaciones existentes y genera nuevas confirmaciones que pueden parecer iguales, pero son técnicamente distintas (con diferentes identificadores).
</p>

<p>
Si ya compartiste tu historial y luego lo reorganizas con <code>git rebase</code> para subirlo de nuevo, tus compañeros tendrán que refusionar su trabajo porque el historial que ellos tienen no coincidirá con el nuevo. Esto puede causar conflictos innecesarios y dificultar la colaboración.
</p>

<p>
Por ello, <strong>usa <code>rebase</code> solo en ramas locales y privadas</strong>, donde tú tienes el control completo del historial.
</p>

---

<h2>Conclusiones</h2>

<p>
En esta sección aprendiste los procedimientos básicos de ramificación y fusión en Git. Ahora sabes cómo crear nuevas ramas, cambiar entre ellas para desarrollar distintas funcionalidades o corregir errores, y cómo fusionar ramas de forma segura.
</p>

<p>
También estás capacitado para compartir tus ramas a través de un servidor remoto, colaborar con otras personas en ramas compartidas y reorganizar tu historial de trabajo antes de hacerlo público.
</p>

<p>
Dominar estas herramientas te permitirá llevar un control más claro, flexible y profesional sobre tus proyectos, facilitando el trabajo en equipo y manteniendo un historial limpio y comprensible.
</p>



