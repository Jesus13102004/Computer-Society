<p align="center">
  <img src="https://git-scm.com/images/logo@2x.png" width="200" alt="Git Logo"/>
</p>

<h1 align="center"><code>Git en el Servidor</code></h1>

<h2>Introducción</h2>

<p>
En este punto ya deberías ser capaz de realizar la mayoría de las tareas diarias para las cuales estarás usando Git. 
Sin embargo, para poder trabajar de forma colaborativa es necesario tener un <strong>repositorio remoto</strong> al que tengan acceso todos los miembros del proyecto y que sea una copia confiable sobre la que puedan trabajar.
</p>

<p>
Poner en funcionamiento un servidor Git es bastante sencillo. Primero tienes que elegir con qué protocolo te vas a comunicar con el servidor. 
Veremos los diferentes <strong>protocolos disponibles</strong>, así como los <strong>pros y contras</strong> de cada uno.
</p>

<p>
Lo siguiente es explicar algunas configuraciones comunes utilizando dichos protocolos y cómo poner a funcionar tu propio servidor.
</p>

<p>
Finalmente, revisaremos algunas de las <strong>opciones de alojamiento (hosting)</strong> disponibles para Git.
</p>

---


<h2>Los Protocolos</h2>

<p>
Git puede usar únicamente cuatro protocolos para transferir datos:
</p>

<ul>
  <li>Local</li>
  <li>HTTP</li>
  <li>SSH</li>
  <li>Git</li>
</ul>

<p>
A continuación, explicaremos en qué consiste cada uno, junto con sus ventajas y desventajas.
</p>

<h3>Protocolo Local</h3>

<p>
Es el más básico, donde el repositorio remoto es simplemente otra carpeta en el disco. Se usa cuando todos los miembros del equipo tienen acceso a un solo sistema, como un punto de montaje <code>NFS</code>, o en el caso menos común, que todos trabajen sobre un mismo equipo físico.
</p>

<p>
Para clonar o enviar datos a un repositorio local se utiliza la ruta del proyecto, como en los siguientes ejemplos:
</p>

```bash
$ git clone /opt/git/project.git
$ git clone file:///opt/git/project.git
```

<p> La mejor práctica es usar directamente la ruta sin el prefijo <code>file://</code>, ya que este último lanza un proceso adicional para transferencia de datos que puede ser menos eficiente. </p> 
<p> Para añadir un repositorio local a un proyecto Git existente puedes usar el siguiente comando: </p>

```bash
$ git remote add local_proj /opt/git/project.git
```

<h4>Ventajas</h4> 
<ul> 
    <li>Simplicidad en la configuración.</li> 
    <li>Aprovecha los permisos de acceso del sistema.</li> 
    <li>Útil para recuperar rápidamente el contenido del repositorio de otro usuario.</li> 
</ul>

<h4>Desventajas</h4> 
    <ul> 
    <li>Difícil acceso desde ubicaciones remotas o fuera de red.</li> 
    <li>Una carpeta compartida (como NFS) no siempre es la opción más rápida.</li> 
    <li>Un repositorio local es rápido solo si tienes acceso directo al sistema de archivos.</li> 
</ul> 

<h3>Protocolos HTTP</h3>

<p>
Git puede utilizar el protocolo HTTP de dos maneras. Antes de la versión 1.6.6, solo estaba disponible el modo de lectura conocido como <strong>HTTP tonto</strong>. A partir de la versión 1.6.6 se introdujo un nuevo protocolo más eficiente, llamado <strong>HTTP inteligente</strong>, que funciona de forma similar al protocolo SSH.
</p>

<h4>HTTP Inteligente</h4>

<p>
Este protocolo opera sobre puertos HTTP/HTTPS y utiliza mecanismos de autenticación estándar, lo que facilita el uso para los usuarios, ya que pueden identificarse con nombre de usuario y contraseña, sin necesidad de gestionar claves SSH.
</p>

<p>
Una ventaja clave del protocolo HTTP inteligente es que utiliza una única URL para todas las operaciones: clonar, enviar y recibir datos.
</p>

<h4>HTTP Tonto</h4>

<p>
Su principal virtud es la simplicidad de configuración. Basta con colocar el repositorio Git en el directorio raíz de documentos del servidor web y configurar el hook correspondiente. Desde ese momento, cualquiera con acceso al servidor podrá clonar el repositorio.
</p>

<p>Pasos para habilitar acceso de lectura:</p>

```bash
$ cd /var/www/htdocs
$ git clone --bare /path/to/git_project gitproject.git
$ cd gitproject.git
$ mv hooks/post-update.sample hooks/post-update
$ chmod a+x hooks/post-update
```

<p> Una vez configurado, los usuarios pueden clonar el repositorio con: </p>

```bash
$ git clone https://example.com/gitproject.git
```

<p> En este ejemplo se usa <code>/var/www/htdocs</code>, que es una ruta común en configuraciones estándar, pero puede usarse cualquier servidor web estático. </p> 

<h4>Ventajas del HTTP Inteligente</h4> 
<ul>
    <li>Usa una única URL para todas las operaciones (clonar, enviar, recibir).</li> 
    <li>Solicita autenticación solo cuando es necesario.</li> 
    <li>Permite autenticarse con usuario y contraseña, evitando la necesidad de claves SSH.</li> 
</ul> 

<h4>Desventajas</h4> 
<ul>
    <li>La configuración de HTTP/S puede ser más compleja en comparación con SSH.</li> 
    <li>En algunos entornos no ofrece ventajas significativas sobre otros protocolos.</li> 
</ul>





<h3>Protocolo SSH</h3>

<p>
El protocolo SSH es ampliamente utilizado para alojar repositorios Git en servidores privados. Se trata de un protocolo de red seguro y autenticado que resulta relativamente sencillo de usar.
</p>

<p>Para clonar un repositorio utilizando SSH, se puede usar el siguiente comando:</p>

```bash
$ git clone ssh://user@server/Project.git
```

<p>O bien, usar la sintaxis estilo <code>scp</code>:</p>

```bash
$ git clone user@server:project.git
```

<h4>Ventajas</h4> 
<ul>
    <li>Relativamente fácil de configurar.</li> 
    <li>Ofrece un acceso seguro, con todas las transferencias encriptadas y autenticadas.</li> 
    <li>Es eficiente, ya que comprime los datos antes de transferirlos (al igual que HTTP, Git y Local).</li> 
</ul> 

<h4>Desventajas</h4> 
<ul> 
    <li>No permite acceso anónimo al repositorio.</li> 
    <li>Cada colaborador debe tener configurado su acceso SSH al servidor.</li> 
</ul> 
<p class="nota"> <strong>Nota:</strong> En entornos corporativos, es común que SSH sea el único protocolo permitido para acceso remoto seguro. </p>


<h3>Protocolo Git</h3>

<p>
El protocolo Git utiliza un <em>demonio</em> especial incluido en Git que escucha en un puerto dedicado (9418). Funciona de forma similar a SSH, pero <strong>sin ninguna medida de autenticación</strong>.
</p>

<p>
Para hacer público un repositorio utilizando este protocolo, se debe agregar un archivo llamado <code>git-daemon-export-ok</code> en el directorio del repositorio. Una vez hecho esto, el repositorio estará disponible para ser clonado por cualquier persona.
</p>

<p class="advertencia">
<strong>Advertencia:</strong> Si alguien encuentra tu repositorio en línea, podrá clonarlo sin restricciones y, si tienes configuraciones incorrectas, incluso hacer <code>push</code> con contenido no deseado.
</p>

<h4>Ventajas</h4>
<ul>
  <li>Es el protocolo más rápido disponible.</li>
  <li>Ideal para proyectos de gran tamaño donde no se requiere autenticación.</li>
  <li>Utiliza los mismos mecanismos de transmisión que SSH, pero sin la sobrecarga de encriptación y autenticación.</li>
</ul>

<h4>Desventajas</h4>
<ul>
  <li>No cuenta con autenticación, lo que representa un riesgo de seguridad.</li>
  <li>No es recomendable como único método de acceso.</li>
  <li>Requiere levantar su propio demonio y configurar servicios como <code>xinetd</code> o similares, lo cual no siempre está disponible por defecto.</li>
</ul>

---


<h2>Configurando Git en un Servidor</h2>

<p>
A continuación, se mostrarán los pasos y comandos necesarios para realizar una configuración básica de un servidor Git en un entorno basado en Linux.
</p>

<p>
Cuando se configura un servidor por primera vez, es necesario exportar un repositorio existente en forma de repositorio vacío (<em>bare repository</em>). Para ello, se utiliza el siguiente comando:
</p>

```bash
$ git clone --bare my_project my_project.git
Cloning into bare repository 'my_project.git'…
done.
```

<p>
Al ejecutar este comando, se genera una copia de los datos del repositorio original en un nuevo directorio llamado <code>my_project.git</code>, el cual contiene exclusivamente el historial de versiones y metadatos, sin archivos de trabajo. Este tipo de repositorio es ideal para ser usado como repositorio central en un servidor.
</p>


<h3>Colocando un Repositorio Vacío en un Servidor</h3>

<p>
Una vez que tienes una copia vacía de tu repositorio (<em>bare repository</em>), necesitas trasladarla a tu servidor y establecer el protocolo de acceso.
</p>

<p>
Supongamos que tu servidor se llama <code>git.example.com</code>, que tienes acceso vía SSH y deseas almacenar todos tus repositorios en el directorio <code>/opt/git</code>. Puedes subir el repositorio utilizando el siguiente comando:
</p>

```bash
$ scp -r my_project.git user@git.example.com:/opt/git
```

<p>
Después de copiar el repositorio al servidor, cualquier usuario con acceso SSH y permisos de lectura sobre el directorio <code>/opt/git</code> podrá clonar el repositorio con:
</p>

```bash
$ git clone user@git.example.com:/opt/git/my_project.git
```

<div class="nota">
<strong>Nota:</strong> Si un usuario accede mediante SSH al servidor y tiene permisos de escritura sobre el repositorio, automáticamente también podrá hacer <code>push</code> de sus cambios.
</div>



<h3>Pequeñas Configuraciones</h3>

<p>
Uno de los aspectos más complejos al trabajar con Git en servidores es la <strong>gestión de usuarios y permisos</strong>. 
Si necesitas que algunos archivos sean de solo lectura para ciertos usuarios y de lectura y escritura para otros, organizar correctamente los accesos puede ser un reto.
</p>

<p>
A continuación, se presentan algunas estrategias para gestionar el acceso de tu equipo al repositorio:
</p>

<ul>
  <li>
    <strong>Crear cuentas individuales para cada usuario:</strong> Es una solución sencilla y directa, pero puede volverse lenta y poco escalable si tu equipo es muy grande.
  </li>
  <li>
    <strong>Usar un único usuario <code>git</code> en el servidor:</strong> Cada miembro del equipo debe enviarte su <em>clave pública SSH</em>, la cual deberás agregar al archivo 
    <code>~/.ssh/authorized_keys</code> del usuario <code>git</code>. Esta es una forma común y efectiva de control de acceso.
  </li>
  <li>
    <strong>Integración con sistemas de autenticación externos:</strong> Puedes configurar tu servidor SSH para que autentique contra un servidor LDAP u otra fuente de autenticación 
    centralizada. Esta opción es más compleja, pero más robusta para entornos corporativos.
  </li>
</ul>

---

<h2>Generando tu Clave Pública SSH</h2>

<p>
Antes de generar una nueva clave SSH, es importante verificar si ya cuentas con una. Para ello, navega al directorio <code>~/.ssh</code> y lista su contenido con el siguiente comando:
</p>

```bash
$ ls ~/.ssh
```

<p>
Si ves un archivo con extensión <code>.pub</code> (por ejemplo, <code>id_rsa.pub</code>), significa que ya tienes una clave pública generada. 
En ese caso, basta con abrir ese archivo, copiar su contenido y compartirlo con el administrador del servidor.
</p>

<p>
En caso de que no tengas una clave generada o el directorio <code>.ssh</code> no exista, puedes crear una nueva con el siguiente comando:
</p>

```bash
$ ssh-keygen
```

<p>
Al ejecutarlo, se te pedirá confirmar la ubicación para guardar la clave. Si no deseas cambiarla, simplemente presiona <kbd>Enter</kbd>. 
Luego se te solicitará establecer una contraseña opcional para proteger tu clave privada.
</p>

<div class="nota">
  <strong>Nota:</strong> Puedes dejar la contraseña en blanco si no deseas escribirla cada vez que utilices tu clave, aunque esto reduce el nivel de seguridad.
</div>

---

<h3>Conclusión</h3>

<p>
Exploramos distintas formas de configurar y acceder a un repositorio Git remoto. 
Tener tu propio servidor Git te brinda un mayor control, además de la posibilidad de operar dentro de tu propio cortafuegos, lo cual puede ser fundamental para ciertos entornos empresariales. 
Sin embargo, esto implica mayor tiempo de configuración y tareas de mantenimiento constantes.
</p>

<p>
Por otro lado, utilizar servicios de hospedaje como GitHub, GitLab o Bitbucket simplifica el proceso de configuración y reduce la carga administrativa. 
No obstante, algunas organizaciones tienen políticas que restringen el almacenamiento de código en servidores externos, por lo que esta opción no siempre es viable.
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
