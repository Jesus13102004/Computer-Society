<p align="center">
  <img src="https://git-scm.com/images/logo@2x.png" width="200" alt="Git Logo"/>
</p>

<h1 align="center"><code>LOS ENTRESIJOS INTERNOS DE GIT</code></h1>


<h2>Introducción</h2>
<p>
    En este capítulo veremos el funcionamiento interno y la implementación de Git.
    Entenderemos por qué Git es un sistema de archivos de contenido localizable, con una interfaz de usuario de control de versiones (<code>VCS</code>) escrita sobre él.
</p>
<p>
    Mostraremos los mecanismos de transporte y algunas tareas de mantenimiento del repositorio que posiblemente necesites usar en algún momento.
</p>


---


<h2>Fontanería y porcelana</h2>
<p>
    Los comandos de <strong>fontanería</strong> son verbos creados para realizar tareas de bajo nivel, pensados para ser utilizados de forma encadenada al estilo UNIX o dentro de scripts.
</p>
<p>
    Los comandos más amigables son conocidos como comandos de <strong>porcelana</strong>.
    En los capítulos anteriores se vieron casi todos los comandos de este tipo.
</p>
<p>
    Ahora nos enfocaremos más en los comandos de fontanería. Estos comandos nos ayudan a comprender <strong>cómo y por qué Git hace lo que hace de la forma en que lo hace</strong>. 
    La mayoría están diseñados como bloques de construcción para nuevas herramientas o scripts personalizados.
</p>

<p>
    Al ejecutar el comando <code>git init</code> en un proyecto nuevo, se crea la carpeta <code>.git</code>.
    En este capítulo analizaremos el contenido de dicha carpeta.
</p>

<p>La estructura inicial de <code>.git</code> es la siguiente:</p>

```bash
HEAD
config*
description
hooks/
info/
objects/
refs/
```

<p><strong>Descripción de cada entrada:</strong></p>
<ul>
    <li><code>description</code>: se utiliza solamente en el programa GitWeb.</li>
    <li><code>config</code>: contiene las opciones de configuración específicas del proyecto.</li>
    <li><code>info/</code>: guarda un archivo global de exclusión con los patrones a ignorar, además de los que se agreguen al archivo <code>.gitignore</code>.</li>
    <li><code>hooks/</code>: contiene los scripts tanto del cliente como del servidor.</li>
    <li><code>objects/</code>: almacena el contenido de la base de datos de Git.</li>
    <li><code>refs/</code>: guarda los apuntadores a los commits.</li>
    <li><code>HEAD</code>: apunta a la rama que se encuentra activa actualmente.</li>
    <li><code>index</code>: (aún por crearse) almacena la información del área de preparación (staging).</li>
</ul>

<p>
    Las cuatro entradas más importantes son: <strong>HEAD</strong>, <strong>index</strong> (una vez creado), 
    <strong>objects</strong> y <strong>refs</strong>.
</p>


---


<h2>Los Objetos Git</h2>
<p>
    Git es un sistema de archivos <strong>orientado a contenido</strong>, lo que significa que su núcleo es un simple <em>almacén de claves y valores</em>. Cuando insertas contenido, Git te devuelve una clave que puedes usar para recuperarlo en cualquier momento.
</p>

<p>
    Para ver esto en acción, puedes usar el comando de fontanería <code>hash-object</code>. Este comando toma datos, los guarda en la carpeta <code>.git</code> y devuelve la clave (SHA-1) con la que se almacenó.
</p>

<h4>Ejemplo: Guardar texto directamente</h4>

```bash
$ echo "test content" | git hash-object -w --stdin
```

<p>
    El parámetro <code>-w</code> indica que se debe guardar el contenido. El texto <code>"test content"</code> se almacena dentro de <code>.git/objects</code> y Git te devuelve una clave SHA-1. Los primeros dos dígitos serán la subcarpeta y los restantes el nombre del archivo. Por ejemplo:
</p>

```bash
.git/objects/d6/70460b4b4aece5915caf5c68d12f560a9fe3e4
```

<h3>Recuperar el contenido</h3>
<p>Para ver el contenido almacenado, usa el comando:</p>

```bash
$ git cat-file -p d670460b4b4aece5915caf5c68d12f560a9fe3e4
```

<p>Esto imprimirá:</p>

```bash
test content
```

<h3>Guardar archivos</h3>
<p>
    Para almacenar un archivo completo en lugar de texto directo, simplemente pasa el nombre del archivo como argumento:
</p>

```bash
$ git hash-object -w test.txt
```

<p>
    En este caso, <strong>Git no guarda el nombre del archivo, solo su contenido</strong>. A este tipo de objeto se le llama un <code>blob</code> (Binary Large Object).
</p>


<h3>Objetos tipo Árbol</h3>
<p>
    El contenido en Git se puede guardar como <strong>objetos binarios</strong> (blobs) u <strong>objetos tipo árbol</strong>. 
    Los objetos tipo árbol <strong>también guardan el nombre del archivo</strong>, a diferencia de los blobs.
</p>

<p>
    Para ver un objeto árbol puedes ejecutar el siguiente comando:
</p>

```bash
$ git cat-file -p main^{tree}
```

<p>
    El parámetro <code>main^{tree}</code> indica el objeto árbol apuntado por el último commit en la rama <code>main</code>. 
    Este árbol puede contener archivos (blobs) o apuntadores a otros árboles.
</p>

<p>
    En el ejemplo anterior guardamos un archivo llamado <code>test.txt</code> en la base de datos. 
    Para crear un árbol, es necesario primero crear un índice preparando archivos para su almacenamiento.
</p>

<p>
    Esto se hace con el comando de fontanería <code>update-index</code>, utilizando los parámetros:
</p>
<ul>
    <li><code>--add</code>: porque el archivo aún no está en el área de preparación.</li>
    <li><code>--cacheinfo</code>: porque el archivo no está físicamente, solo en la base de datos.</li>
</ul>

```bash
$ git update-index --add --cacheinfo 100644 \</code></pre>
```

<p>
    En este caso, <code>100644</code> indica que es un archivo normal. Otros modos válidos son:
</p>
<ul>
    <li><code>100755</code>: archivo ejecutable</li>
    <li><code>120000</code>: enlace simbólico</li>
</ul>

<p>
    Una vez actualizado el índice, se puede usar el comando <code>write-tree</code> para convertir el estado actual del área de preparación en un <strong>objeto tipo árbol</strong>:
</p>

```bash
$ git write-tree</code></pre>
```
<p>
    Si no existía previamente, Git <strong>creará automáticamente un objeto árbol</strong> con la información del índice actual.
</p>

<h3>Objetos de Confirmación de Cambios</h3>

<p>
    Los <strong>objetos de confirmación</strong> (commits) en Git almacenan información esencial como:
</p>
<ul>
    <li><strong>Quién</strong> guardó la instantánea (nombre y correo del autor).</li>
    <li><strong>Cuándo</strong> se realizó la confirmación.</li>
    <li><strong>Por qué</strong> se guardaron los cambios (mensaje del commit).</li>
</ul>

<p>
    Para crear un commit manualmente desde un objeto árbol, se utiliza el comando de fontanería <code>commit-tree</code>.
    Este comando requiere el <strong>SHA-1 del árbol</strong> que deseas confirmar y opcionalmente los commits padres si los hay.
</p>

```bash
$ echo "first commit" | git commit-tree d8329f
```

<p>
    Esto genera un nuevo objeto de confirmación y devuelve su hash, por ejemplo:
</p>

```bash
fdf4fc3344e67ab068f836878b6c4951e3b15f3d
```

<p>
    Puedes inspeccionar el contenido de este commit con:
</p>

```bash
$ git cat-file -p fdf4fc3
```

<p>
    La salida incluirá:
</p>
<ul>
    <li>El <strong>SHA-1</strong> del árbol al que apunta.</li>
    <li>Datos del autor: <code>user.name</code> y <code>user.email</code>.</li>
    <li>El mensaje de confirmación.</li>
</ul>

<p>
    En esencia, esto es lo que realiza Git cuando usas <code>git add</code> y <code>git commit</code>, pero aquí se hace utilizando comandos de bajo nivel (fontanería).
</p>



<h3>Almacenamiento de los objetos</h3>

<p>
    Ahora veremos cómo almacena <strong>Git</strong> sus objetos. Supongamos que tenemos un archivo binario llamado <code>blob</code>. Git construye la cabecera comenzando por el tipo de objeto, después el tamaño del contenido y termina con un byte nulo:
</p>

```bash
>>header = "blob #{content.length}\0"
=> "blob 16\u0000"
```

<p>
    Luego, Git concatena la cabecera y el contenido original para calcular la suma de control <strong>SHA-1</strong>.
</p>


---

<h2>Referencias Git</h2>

<p>
    Lo que hacen las <strong>referencias</strong> de Git es crear un archivo en donde se almacenan los valores de las sumas de comprobación <strong>SHA-1</strong> junto con nombres simples que puedas usar como enlaces.
</p>

<p>
    En la carpeta <code>.git/refs</code> puedes encontrar esos archivos con valores SHA-1 y sus nombres correspondientes.
</p>

<p>
    Para crear una nueva referencia, puedes usar el siguiente comando:
</p>

```bash
$ echo "1a410efbd13591db07496601ebc7a059dd55cfe9" > .git/refs/heads/main
```

<p>
    Desde ese momento, puedes usar esa referencia en lugar del valor SHA-1 completo.
</p>

<p>
    Si necesitas actualizar una referencia, puedes utilizar el comando <code>update-ref</code> de esta manera:
</p>

```bash
$ git update-ref refs/heads/main 1a410efbd13591db07496601ebc7a059dd55cfe9
```

---

<h2>La CABEZA (HEAD)</h2>

<p>
    El archivo <code>HEAD</code> es una <strong>referencia simbólica</strong> a la rama en la que te encuentras. Este archivo no contiene un valor <code>SHA-1</code>; en su lugar, contiene un enlace a otra referencia.
</p>

<p>
    Si observamos el contenido del archivo <code>HEAD</code>, veremos algo como lo siguiente:
</p>

```bash
$ cat .git/HEAD
ref: refs/heads/main
```

<p>
  Para editar esta referencia, existe el comando <code>symbolic-ref</code>, que se usa de la siguiente forma:
</p>

```bash
$ git symbolic-ref HEAD refs/heads/test
$ cat .git/HEAD
ref: refs/heads/test
```

---

<h2>Etiquetas</h2>

<p>
    El objeto tipo <strong>etiqueta</strong> en Git es muy similar al tipo <strong>confirmación de cambios</strong>. Contiene:
</p>
<ul>
    <li>Un marcador</li>
    <li>Una fecha</li>
    <li>Un mensaje</li>
    <li>Un enlace</li>
</ul>

<p>
    La diferencia principal es que <strong>una etiqueta apunta a un commit</strong>, y no a un objeto tipo árbol.
</p>

<p>
    Puedes crear una <strong>etiqueta ligera</strong> (una referencia que nunca se mueve) con el siguiente comando:
</p>

```bash
$ git update-ref refs/tags/v1.0 cac0cab538b970a37ea1e769cbbde608743bc96d
```


---

<h2>Sitios remotos</h2>

<p>
    Si añades un <strong>sitio remoto</strong> y le envías contenido, Git almacenará en ese sitio remoto el último valor de cada rama presente en la carpeta <code>.git/refs/remotes</code>.
</p>

<p>
    Las <strong>referencias a sitios remotos</strong> son diferentes a las ramas locales normales, ya que se consideran <strong>de solo lectura</strong>.
    Git las utiliza únicamente como <em>marcadores</em> del último estado conocido de cada rama en cada servidor remoto declarado.
</p>

---

<h2>Archivos empaquetados</h2>

<p>
    Git utiliza la librería <code>zlib</code> para <strong>comprimir los archivos</strong> y así ahorrar espacio. Almacena la versión más reciente de un archivo de forma completa, y las versiones anteriores las guarda como <strong>diferencias (deltas)</strong>, ya que es más común recuperar la versión actual.
</p>

<p>
    Cuando tienes varios objetos, Git los <strong>empaqueta automáticamente</strong>. Sin embargo, puedes forzar este proceso manualmente utilizando el siguiente comando:
</p>

```bash
$ git gc
```

<p>
    Este comando ejecuta una limpieza ("garbage collection") que <strong>empaqueta todos los objetos</strong>, excepto aquellos que aún no han sido confirmados.
</p>


---

<h2>Protocolos de transferencia</h2>

<p>
    Git tiene dos mecanismos principales para <strong>transferir datos entre repositorios</strong>: el <strong>protocolo tonto</strong> y el <strong>protocolo inteligente</strong>.
</p>

<p>
    A continuación veremos cómo funciona cada uno.
</p>


<h3>Protocolo Tonto</h3>

<p>
    El <strong>Protocolo Tonto</strong> permite trabajar únicamente en <strong>modo de solo lectura</strong>. 
    Se le llama "tonto" porque <strong>no requiere que el servidor tenga Git instalado</strong> ni ejecutando ningún código de Git para el proceso de transferencia.
</p>

<p>
    La recuperación de datos se realiza mediante una <strong>serie de solicitudes HTTP GET</strong>, accediendo directamente a los archivos del repositorio remoto.
</p>

<p><strong>Nota:</strong> Este protocolo está en desuso porque <strong>no proporciona mecanismos adecuados de confidencialidad ni autenticación</strong>.</p>




<h3>Protocolo Inteligente</h3>

<p>
    El <strong>Protocolo Inteligente</strong> es el método más común y eficiente para la transmisión de datos en Git. 
    A diferencia del protocolo tonto, este <strong>puede leer datos localmente</strong>, determinar qué información ya tiene el cliente y generar un <strong>paquete optimizado</strong> con solo los datos necesarios.
</p>

<p>
    Este protocolo cuenta con <strong>dos procesos distintos</strong>:
</p>

<ul>
    <li><code>send-pack</code>: se ejecuta en el lado del cliente y se encarga de <strong>enviar datos</strong> al servidor remoto.</li>
    <li><code>receive-pack</code>: se ejecuta en el lado del servidor remoto y <strong>recibe los datos</strong> enviados por el cliente.</li>
</ul>

<p>
    Gracias a esta comunicación más eficiente, el Protocolo Inteligente es ideal tanto para clonar, hacer <code>fetch</code>, como para enviar confirmaciones mediante <code>push</code>.
</p>

---

<h2>Conclusiones</h2>

<p>
    En este capítulo exploramos varios <strong>comandos de fontanería</strong> que operan a bajo nivel dentro de Git. 
    Estos comandos nos permitieron entender cómo Git maneja internamente los objetos, referencias y estructuras de datos.
</p>

<p>
    Git no solo es una herramienta para control de versiones, sino también un <strong>sistema poderoso de gestión de contenido</strong>, capaz de adaptarse a diferentes flujos de trabajo y necesidades avanzadas. 
    Conocer su funcionamiento interno amplía significativamente las posibilidades de automatización, personalización y optimización en proyectos profesionales.
</p>

---

## <span style="color:#9E9D24"><strong>Licencia</strong></span>

Este contenido está licenciado bajo [Creative Commons Attribution-NonCommercial 4.0 (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/).  
Puedes compartirlo, adaptarlo y utilizarlo con fines educativos y no comerciales, siempre que des crédito al autor original:

> **Jesús Eduardo Arciniega Tlacomulco**

---

<p align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Git-logo.svg/1024px-Git-logo.svg.png" width="160" alt="Git footer logo"/>
</p>

<p align="center"><i>Desarrollado por Jesús Eduardo Arciniega Tlacomulco – Curso de Git y GitHub</i></p>