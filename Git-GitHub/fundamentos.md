<p align="center">
  <img src="https://git-scm.com/images/logo@2x.png" width="200" alt="Git Logo"/>
</p>

<h1 align="center"><code>FUNDAMENTOS DE GIT</code></h1>

<h2>Introducción a los comandos básicos</h2>

En este capítulo se presentan los comandos fundamentales para comenzar a trabajar con Git en proyectos locales y remotos.

Al finalizar esta sección, serás capaz de:

<ul>
  <li>Configurar e iniciar un repositorio local con <code>git init</code></li>
  <li>Iniciar o detener el seguimiento de archivos</li>
  <li>Preparar (<i>stage</i>) y confirmar (<i>commit</i>) cambios</li>
  <li>Ignorar archivos y patrones con <code>.gitignore</code></li>
  <li>Solucionar errores comunes de forma rápida y eficaz</li>
  <li>Navegar por el historial del proyecto con <code>git log</code></li>
  <li>Comparar cambios entre confirmaciones</li>
  <li>Enviar (<code>push</code>) y recibir (<code>pull</code>) archivos desde y hacia repositorios remotos</li>
</ul>

---

<h2> Obtener un repositorio Git</h2>

<p>Existen dos formas principales de comenzar a trabajar con Git en un proyecto:</p>

---

###  1. Iniciar un repositorio en un proyecto existente
<hr style="height:1px; border:none; background-color:rgba(128, 128, 128, 0.4);"/>

Si ya cuentas con un proyecto local y deseas comenzar a gestionarlo con Git, solo necesitas inicializar el repositorio dentro del directorio raíz del proyecto:

```bash
$ git init
```
Esto crea un directorio oculto llamado **.git**, que contiene la base de datos de Git (historial, objetos y configuraciones). Es el "esqueleto" del repositorio.

Una vez inicializado, puedes comenzar a registrar archivos existentes con:

```bash
$ git add nombre_archivo
$ git commit -m "Descripción del primer commit"
```

Estos comandos serán explicados con más detalle en las siguientes secciones.

<p align="center"> <img src="https://www.thecreativedev.com/wp-content/uploads/2017/08/to-use-git-init-command-545x300.png" width="600" alt="git init ejemplo"/> </p>


### 2. Clonando un repositorio existente en Git
<hr style="height:1px; border:none; background-color:rgba(128, 128, 128, 0.4);"/>

<p>Para obtener una copia local de un repositorio remoto ya existente (por ejemplo, en GitHub), se utiliza el siguiente comando:</p>

```bash
$ git clone [URL]
```
Este comando realiza las siguientes acciones:
<ul> 
    <li>Descarga todo el historial del proyecto almacenado en el servidor.</li>
    <li>Crea un nuevo directorio con el nombre del repositorio.</li> 
    <li>Dentro de ese directorio, genera el archivo oculto <code>.git</code>, que contiene toda la información interna del repositorio.</li> 
    <li>Extrae y guarda una copia exacta de la última versión confirmada del proyecto.</li> 
</ul> <p align="center"> <img src="https://res.cloudinary.com/hy4kyit2a/f_auto,fl_lossy,q_70/learn/projects/develop-app-with-salesforce-cli-and-source-control/add-salesforce-dx-project-to-source-control/images/bf546ec3acd964673bf5f6302125fd93_step-4-github-and-git-clones.png" width="550" alt="git clone imagen"/> </p>

---

<h2> Guardar cambios en el repositorio</h2>

<p>Los archivos de un repositorio pueden encontrarse en dos estados principales:</p>

<ul>
    <li><strong>Rastreados (tracked):</strong> Archivos que forman parte de la última confirmación. Pueden estar sin modificar, modificados o preparados.</li>
    <li><strong>No rastreados (untracked):</strong> Archivos nuevos que no existían en la última versión del proyecto y aún no han sido añadidos al área de preparación.</li>
</ul>

<p>Cuando editas un archivo, Git lo detecta como <i>modificado</i>. Para registrar este cambio debes:</p>

<ol>
    <li>Preparar el archivo (<code>git add</code>).</li>
    <li>Confirmar los cambios (<code>git commit</code>).</li>
</ol>



### Revisando los estados de los archivos
<hr style="height:1px; border:none; background-color:rgba(128, 128, 128, 0.4);"/>

<p>Para ver el estado actual de los archivos en tu proyecto, se utiliza el siguiente comando:</p>

```bash
$ git status
```

Si ejecutas este comando sin haber hecho ninguna modificación, se mostrará algo como:

```bash
$ git status
On branch master
nothing to commit, working directory clean
```

Esto indica que el directorio de trabajo está limpio: no hay archivos nuevos, modificados ni pendientes por confirmar. Además, muestra en qué rama se está trabajando actualmente.
Ahora bien, si agregas o modificas un archivo y luego vuelves a ejecutar <code>git status</code>, verás algo como esto:

```bash
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)

    nom_arch

nothing added to commit but untracked files present (use "git add" to track)
```

Esto significa que existe un archivo nuevo que Git aún no está rastreando.
La salida del comando <code>git status</code> puede ser extensa.  
Si deseas ver un resumen más compacto del estado de los archivos, puedes utilizar alguno de los siguientes comandos:

```bash
$ git status -s
$ git status --short
```
Ambos comandos producen una salida abreviada que resume el estado de cada archivo mediante códigos:
<table>
    <thead>
        <tr>
            <th>Código</th>
            <th>Significado</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>??</code></td>
            <td>Archivo no rastreado (untracked)</td>
        </tr>
        <tr>
            <td><code>A</code></td>
            <td>Archivo preparado (added to staging)</td>
        </tr>
        <tr>
            <td><code>M</code></td>
            <td>Archivo modificado (modified)</td>
        </tr>
    </tbody>
</table>

Este modo es ideal para revisiones rápidas y limpieza visual en proyectos con múltiples archivos en seguimiento

### Rastrear archivos nuevos
<hr style="height:1px; border:none; background-color:rgba(128, 128, 128, 0.4);"/>


Para comenzar a rastrear un archivo nuevo y agregarlo al área de preparación (staging), se utiliza el siguiente comando:

```bash
$ git add nom_arch
```
Si deseas preparar <strong>todos los archivos modificados</strong> de una sola vez, puedes usar:
```bash
$ git add .
```

Después de ejecutar alguno de estos comandos, si vuelves a ejecutar <code>git status</code>, verás una salida similar a la siguiente:

```bash
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

    new file:   nom_arch
```
Esto indica que el archivo <code>nom_arch</code> ya se encuentra preparado para ser confirmado en el próximo commit.


### Ignorar archivos
<hr style="height:1px; border:none; background-color:rgba(128, 128, 128, 0.4);"/>

<p>En la mayoría de los proyectos existen archivos que no es necesario preparar ni confirmar, como:</p>

<ul>
    <li>Archivos temporales</li>
    <li>Archivos generados automáticamente por compiladores o editores</li>
    <li>Archivos personales o específicos de entorno</li>
</ul>

Para excluir estos archivos del control de versiones, se utiliza el archivo oculto <code>.gitignore</code>.

####  Reglas comunes en <code>.gitignore</code>
<hr style="height:1px; border:none; background-color:rgba(128, 128, 128, 0.4);"/>


<ul>
    <li>Se ignoran las <strong>líneas en blanco</strong> y las que comienzan con <code>#</code> (comentarios).</li>
    <li>Se utilizan <strong>patrones glob</strong> estándar para definir qué ignorar.</li>
    <li>Los patrones se aplican <strong>recursivamente</strong> a todo el directorio del repositorio.</li>
    <li>Un patrón que inicia con <code>/</code> aplica solo a la raíz del repositorio.</li>
    <li>Un patrón que termina con <code>/</code> indica un directorio.</li>
    <li>Un patrón precedido por <code>!</code> anula una regla anterior (lo incluye de nuevo).</li>
</ul>

#### Patrones glob en Git
<hr style="height:1px; border:none; background-color:rgba(128, 128, 128, 0.4);"/>


Los patrones glob son una forma simplificada de expresiones regulares utilizadas comúnmente en terminales.

<table>
    <thead>
        <tr>
            <th>Patrón</th>
            <th>Descripción</th>
            <th>Ejemplo</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>*</code></td>
            <td>Cero o más caracteres</td>
            <td><code>*.log</code> → ignora todos los archivos .log</td>
        </tr>
        <tr>
            <td><code>[abc]</code></td>
            <td>Cualquier carácter dentro de los corchetes</td>
            <td><code>file[123].txt</code> → file1.txt, file2.txt, file3.txt</td>
        </tr>
        <tr>
            <td><code>?</code></td>
            <td>Un solo carácter cualquiera</td>
            <td><code>?.txt</code> → a.txt, b.txt, etc.</td>
        </tr>
        <tr>
            <td><code>[0-9]</code></td>
            <td>Cualquier dígito entre 0 y 9</td>
            <td><code>log[0-9].txt</code> → log1.txt, log7.txt</td>
        </tr>
        <tr>
            <td><code>a/**/z</code></td>
            <td>Directorios anidados entre <code>a</code> y <code>z</code></td>
            <td><code>a/z</code>, <code>a/b/z</code>, <code>a/b/c/z</code></td>
        </tr>
    </tbody>
</table>

Colocar correctamente el archivo <code>.gitignore</code> desde el inicio de un proyecto ayuda a mantener limpio el historial de versiones y evita errores comunes al subir archivos innecesarios o privados.


### Ver los cambios preparados y no preparados
<hr style="height:1px; border:none; background-color:rgba(128, 128, 128, 0.4);"/>


Para revisar en detalle qué líneas han sido modificadas, añadidas o eliminadas en los archivos del proyecto, se utiliza el comando:

```bash
$ git diff
```

Este comando compara el contenido del <strong>directorio de trabajo</strong> con el <strong>área de preparación (staging)</strong>, y muestra únicamente los cambios que <strong>aún no han sido preparados</strong>.
Si los archivos ya fueron preparados con <code>git add</code>, <code>git diff</code> no mostrará ninguna diferencia.

Para ver los archivos que ya han sido añadidos al área de preparación y que serán incluidos en la próxima confirmación (<i>commit</i>), se pueden usar cualquiera de los siguientes comandos:

```bash
$ git diff --stage
$ git diff --cached
```

Ambos comandos comparan los archivos preparados con la última instantánea confirmada en el repositorio. Esto permite revisar exactamente qué será incluido en el próximo commit antes de ejecutarlo.


### Confirmar los cambios
<hr style="height:1px; border:none; background-color:rgba(128, 128, 128, 0.4);"/>


Una vez que los cambios han sido preparados con <code>git add</code>, puedes confirmarlos (guardarlos en el historial del repositorio) utilizando el siguiente comando:

```bash
$ git commit -m "Descripción del cambio"
```

Al ejecutar este comando, Git registrará el commit y devolverá una salida similar a la siguiente:

```bash
[master 463dc4f] Descripción del cambio
    2 files changed, 2 insertions(+)
    create mode 100644 README
```
Esta salida indica:

<ul> 
    <li><strong>Rama:</strong> En qué rama se realizó la confirmación (por ejemplo, <code>master</code>).</li> 
    <li><strong>Checksum SHA-1:</strong> Identificador único del commit.</li> 
    <li><strong>Archivos cambiados:</strong> Cuántos archivos fueron afectados.</li> 
    <li><strong>Estadísticas:</strong> Cantidad de líneas añadidas y eliminadas.</li> 
</ul>

Si deseas preparar y confirmar todos los archivos modificados (pero rastreados) en un solo paso, puedes utilizar:

```bash
$ git commit -a -m "Descripción"
```
Este comando omite el uso de <code>git add</code> para archivos ya rastreados, pero <strong>no añade archivos nuevos</strong> no rastreados previamente.


### Eliminar archivos</h4>
<hr style="height:1px; border:none; background-color:rgba(128, 128, 128, 0.4);"/>


Para eliminar un archivo del proyecto y reflejar esa eliminación en el historial de Git, es necesario:

<ol>
  <li>Preparar la eliminación con <code>git rm</code></li>
  <li>Confirmar el cambio con <code>git commit</code></li>
</ol>

<p>Comando para eliminar un archivo:</p>

```bash
$ git rm nom_arch
```
Después de ejecutar ese comando, realiza un commit para registrar la eliminación:

```bash
$ git commit -m "Eliminado nom_arch"
```

Si deseas que Git <strong>deje de rastrear</strong> un archivo, pero sin eliminarlo del sistema de archivos (disco), puedes usar:

```bash
$ git rm --cached nom_arch
```

Esto conservará el archivo en tu proyecto local, pero ya no será rastreado por Git en futuros commits.

_El comando <code>git rm</code> también acepta patrones glob, permitiendo eliminar múltiples archivos que cumplan un patrón determinado._


### Cambiarle el nombre a un archivo
<hr style="height:1px; border:none; background-color:rgba(128, 128, 128, 0.4);"/>


Para cambiarle el nombre a un archivo se usa el comando:

```bash
$ git mv nombre_archivo nuevo_nombre_archivo
```
Esto le indica a Git que renombre el archivo y lo registre como un cambio en el historial.

Esto también puede usarse para **mover archivos entre carpetas**. Por ejemplo:
```bash
git mv archivo.txt carpeta/archivo.txt
```

---

<h2> Ver el historial de confirmaciones</h2>

Después de haber hecho varias confirmaciones, probablemente quieras ver cuáles se han registrado. Para esto se usa el comando:
```bash
$ git log
```


Este comando muestra la lista de todas las confirmaciones que se han hecho en el proyecto. La salida que verás en la terminal incluye:

<ul>
    <li>La confirmación más reciente hasta la más antigua.</li>
    <li>La suma de comprobación <strong>SHA-1</strong> (identificador único del commit).</li>
    <li>El <strong>nombre y correo del autor</strong>.</li>
    <li>La <strong>fecha</strong> de la confirmación.</li>
    <li>El <strong>mensaje</strong> del commit.</li>
</ul>

### Parámetros útiles para <code>git log</code></h3>
<hr style="height:1px; border:none; background-color:rgba(128, 128, 128, 0.4);"/>


<p>Al comando <code>git log</code> se le pueden agregar ciertos parámetros para limitar o hacer más precisa la búsqueda. Algunos de los más comunes son:</p>

<ul>
    <li><code>-p</code> &rarr; Muestra la diferencia entre cada confirmación (diff).</li>
    <li><code>-2</code> &rarr; Muestra las dos últimas confirmaciones. Puedes poner cualquier número.</li>
    <li><code>--stat</code> &rarr; Muestra los archivos modificados, cuántas líneas se añadieron o eliminaron, y un resumen general.</li>
    <li><code>--pretty</code> &rarr; Modifica el formato de la salida. Algunos ejemplos:</li>
</ul>

```bash
$ git log --pretty=oneline
$ git log --pretty=short
$ git log --pretty=full
$ git log --pretty=fuller
```

### Comandos para limitar la salida de <code>git log</code>
<hr style="height:1px; border:none; background-color:rgba(128, 128, 128, 0.4);"/>


<Puedes filtrar la salida del historial usando los siguientes parámetros:

<ul>
  <li>
    <code>--since</code> &rarr; Limita los resultados por año, mes, semana, día o tiempo relativo.<br>
    <code>$ git log --since=2.weeks</code>
  </li>
  <li>
    <code>--author</code> &rarr; Muestra solo las confirmaciones hechas por un autor específico.<br>
    <code>$ git log --author="Nombre"</code>
  </li>
  <li>
    <code>--grep</code> &rarr; Busca palabras clave dentro del mensaje de confirmación.<br>
    <code>$ git log --grep="bugfix"</code>
  </li>
  <li>
    <code>--all-match</code> &rarr; Combina filtros como <code>--author</code> y <code>--grep</code> para que ambos se cumplan.<br>
    <code>$ git log --author="Juan" --grep="login" --all-match</code>
  </li>
</ul>

---

<h2>Deshacer cosas</h2>

### Deshacer una confirmación
<hr style="height:1px; border:none; background-color:rgba(128, 128, 128, 0.4);"/>


Uno de los casos más comunes es deshacer una confirmación, ya sea porque te equivocaste en el mensaje o porque olvidaste agregar un archivo. Para modificar la última confirmación se usa:

```bash
$ git commit --amend
```

Si no has hecho cambios desde la última confirmación, al ejecutar <code>--amend</code> se mantendrá el mismo contenido, pero te permitirá cambiar el mensaje.

Ejemplo si olvidaste agregar un archivo antes del commit:

```bash
$ git commit -m "initial commit"
$ git add nombre_archivo
$ git commit --amend
```

La segunda confirmación reemplaza el resultado de la primera y Git lo tratará como si todo se hubiera hecho en un solo commit.


### Deshacer un archivo preparado
<hr style="height:1px; border:none; background-color:rgba(128, 128, 128, 0.4);"/>


Si agregaste un archivo al área de preparación (staging area) con <code>git add</code>, pero decidiste que no quieres confirmarlo aún, puedes sacarlo del área de preparación usando:

```bash
$ git reset HEAD nombre_archivo
```

Esto no elimina el archivo ni sus cambios, simplemente lo remueve del área de staging. Seguirá modificado, pero Git no lo incluirá en el próximo commit.


### Deshacer un archivo modificado
<hr style="height:1px; border:none; background-color:rgba(128, 128, 128, 0.4);"/>



Si modificaste un archivo y quieres descartar todos los cambios no confirmados (sin guardarlos), puedes regresar a la última versión confirmada usando:

```bash
$ git checkout -- nombre_archivo
```

⚠️ <strong>Advertencia:</strong> Este comando <strong>elimina permanentemente</strong> todos los cambios que no se hayan confirmado. No se pueden recuperar.

***Nota: En versiones recientes de Git, se recomienda usar:***
```bash
$ git restore nombre_archivo
```

---

<h2> Trabajar con repositorios remotos</h2>

Los <strong>repositorios remotos</strong> son versiones de tu proyecto que están alojadas en servidores como GitHub, GitLab o Bitbucket.  
Permiten trabajar en equipo, sincronizar cambios y mantener respaldos del código.

Puedes tener múltiples repositorios remotos configurados en tu proyecto. Algunos remotos pueden tener solo permisos de lectura, y otros de lectura y escritura.


### Ver tus remotos
<hr style="height:1px; border:none; background-color:rgba(128, 128, 128, 0.4);"/>


Para ver los repositorios remotos configurados en tu proyecto se usa:

```bash
$ git remote
```

Si clonaste el repositorio desde un servidor, verás un remoto llamado <code>origin</code> por defecto.
Para ver las URLs asociadas a cada remoto (lectura y escritura) existe el comando:

```bash
$ git remote -v
```

### Añadir repositorios remotos
<hr style="height:1px; border:none; background-color:rgba(128, 128, 128, 0.4);"/>

Para vincular tu proyecto local con un repositorio remoto (por ejemplo, en GitHub o GitLab), se utiliza el siguiente comando:

```bash
$ git remote add nombre_remoto URL
```

Ejemplo:

```bash
$ git remote add upstream https://github.com/otro_usuario/proyecto.git
```
Ahora puedes referirte a ese remoto mediante el nombre que asignaste (por ejemplo, <code>upstream</code>).

### Traer y combinar datos desde un remoto
<hr style="height:1px; border:none; background-color:rgba(128, 128, 128, 0.4);"/>

Para obtener actualizaciones desde un repositorio remoto sin integrarlas directamente en tu rama actual se usa el siguiente comando:

```bash
$ git fetch nombre_remoto
```

Ejemplo:

```bash
$ git fetch origin
```

Este comando descargará los datos nuevos desde el repositorio remoto, pero no los combinará con tu trabajo local.
Si deseas traer y <strong>combinar automáticamente</strong> los cambios con tu rama actual:

```bash
$ git pull
```
Este comando es útil cuando tu rama local está conectada (trackeando) una rama remota.


### Enviar cambios a un remoto
<hr style="height:1px; border:none; background-color:rgba(128, 128, 128, 0.4);"/>
Para enviar tus confirmaciones locales a un repositorio remoto se usa el comando:

```bash
$ git push nombre_remoto nombre_rama
```
Ejemplo:
```bash
$ git push origin main
```
Si tu rama actual ya está configurada para rastrear una rama remota, puedes usar simplemente:

```bash
$ git push
```

### Inspeccionar detalles de un remoto
<hr style="height:1px; border:none; background-color:rgba(128, 128, 128, 0.4);"/>
Para ver información detallada de un remoto específico se utiliza el comando:

```bash
$ git remote show nombre_remoto
```
Este comando muestra la URL del repositorio, ramas rastreadas y detalles de configuración.


### Renombrar o eliminar un remoto
<hr style="height:1px; border:none; background-color:rgba(128, 128, 128, 0.4);"/>
Para cambiar el nombre de un remoto existente se usa el comando:
```bash
$ git remote rename nombre_actual nuevo_nombre
```
Para eliminar un remoto del proyecto se usa el comando:
```bash
$ git remote rm nombre_remoto
```

---

<h2>Etiquetado</h2>

El <strong>etiquetado</strong> en Git sirve para marcar puntos importantes dentro del historial del repositorio, como versiones de lanzamiento relevantes.

<p>Existen dos tipos de etiquetas:</p>

<ul>
    <li><strong>Etiquetas ligeras (lightweight tags):</strong> Punteros directos a un commit.</li>
    <li><strong>Etiquetas anotadas (annotated tags):</strong> Objetos completos con metadatos y mensajes.</li>
</ul>


### Listar etiquetas
<hr style="height:1px; border:none; background-color:rgba(128, 128, 128, 0.4);"/>

Para listar todas las etiquetas definidas en el repositorio, utiliza el siguiente comando:

```bash
$ git tag
```
Para listar etiquetas filtradas por patrón (por ejemplo, las que comienzan con <code>v1.8.5</code>) se usa el siguiente comando:

```bash
$ git tag -l "v1.8.5*"
```

### Crear una etiqueta
<hr style="height:1px; border:none; background-color:rgba(128, 128, 128, 0.4);"/>

###Etiqueta ligera
Este tipo de etiqueta funciona como una rama inmutable, simplemente apunta a un commit:

```bash
$ git tag nombre_tag
```

###Etiqueta anotada
Este tipo de etiqueta contiene información adicional y puede ser firmada:

```bash
$ git tag -a v1.4 -m "Versión 1.4 estable"
```
Incluye: 
<ul>
    <li>Checksum SHA-1</li>
    <li>Nombre del etiquetador</li>
    <li>Correo electrónico</li>
    <li>Fecha</li>
    <li>Mensaje asociado</li>
</ul>

<p>Para ver los detalles de una etiqueta anotada:</p>

```bash
$ git show nombre_tag
```


### Etiquetado tardío
<hr style="height:1px; border:none; background-color:rgba(128, 128, 128, 0.4);"/>
Si necesitas etiquetar un commit anterior, puedes especificarlo con su checksum (parcial o completo):
```bash
$ git tag -a nombre_tag <checksum>
```

Recuerda que para obtener el checksum del commit deseado se usa:

```bash
$ git log
```

### Compartir etiquetas
<hr style="height:1px; border:none; background-color:rgba(128, 128, 128, 0.4);"/>

Las etiquetas no se comparten automáticamente con los repositorios remotos, por lo que debes enviarlas explícitamente.
Para enviar las etiquetas existen dos comandos:
### Enviar una etiqueta específica

```bash
$ git push origin nombre_tag
```

### Enviar todas las etiquetas
```bash
$ git push origin --tags
```

---
<h2>Alias de Git</h2>

Git permite configurar <strong>alias</strong> personalizados para simplificar comandos largos o repetitivos, haciendo tu experiencia más fluida, rápida y familiar.

Por ejemplo, puedes abreviar <code>git commit</code> como <code>git ci</code> mediante un alias:


### Crear un alias
<hr style="height:1px; border:none; background-color:rgba(128, 128, 128, 0.4);"/>

Para configurar un alias global:

```bash
$ git config --global alias.ci commit
```

Con esto, puedes utilizar:
```bash
$ git ci -m "my commit"
```

En lugar de:
```bash
$ git commit -m "my commit"
```

Puedes definir alias para cualquier comando de Git, por ejemplo:
```bash
$ git config --global alias.st status
$ git config --global alias.co checkout
$ git config --global alias.br branch
```

Y consultarlos en el archivo de configuración:

```bash
$ git config --global --edit
```
---

<h2>Conclusión</h2>
<hr style="height:1px; border:none; background-color:rgba(128, 128, 128, 0.4);"/>

Con lo aprendido en este capítulo, ya tienes el conocimiento necesario para realizar las operaciones básicas con Git, entre ellas:

<ul>
  <li>Inicializar o clonar un repositorio.</li>
  <li>Realizar cambios en tus archivos de trabajo.</li>
  <li>Preparar (stage) y confirmar (commit) esos cambios.</li>
  <li>Visualizar el historial y el estado de tus archivos.</li>
  <li>Colaborar utilizando repositorios remotos.</li>
</ul>

<p>Estos fundamentos son la base para trabajar de manera profesional en cualquier entorno de desarrollo colaborativo.</p>

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