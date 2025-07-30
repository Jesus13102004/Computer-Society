<p align="center">
  <img src="https://git-scm.com/images/logo@2x.png" width="200" alt="Git Logo"/>
</p>

<h1 align="center"><code>HERRAMIENTAS DE GIT</code></h1>


<h2>Introducción</h2>
<p>
En este capítulo exploraremos herramientas avanzadas que Git pone a tu disposición. 
Aunque no son de uso cotidiano, pueden ser extremadamente útiles en situaciones específicas o complejas. 
Estas funciones te permitirán resolver conflictos, depurar errores o rehacer cambios de manera más eficiente 
cuando lo requieras durante el desarrollo de tus proyectos.
</p>

---

<h2>Revisión por Selección</h2>
<p>
Git te permite especificar ciertos <em>commits</em> o un rango de estos de diferentes maneras. Aunque se puede hacer referencia 
a un commit por su hash SHA-1 completo, también existen formas más amigables y prácticas de identificarlos. Estas opciones 
facilitan la revisión y manipulación del historial sin necesidad de recordar identificadores largos.
</p>

<h3>SHA-1 corto</h3>
<p>
Puedes referirte a un <code>commit</code> utilizando solo los primeros 4 dígitos de su hash SHA-1, siempre y cuando no haya ambigüedad, es decir, que no exista otro commit cuyo hash inicie con los mismos caracteres.
</p>

<p>
Si ejecutas el comando <code>git log</code>, obtendrás una lista de todos los commits del proyecto. Selecciona uno, toma los primeros 4 dígitos de su hash y ejecuta el siguiente comando:
</p>

```bash
$ git show num_SHA-1
```

<p>
Donde <code>num_SHA-1</code> representa los 4 dígitos del hash. Este comando mostrará:
</p>

<ul>
  <li>El hash SHA-1 completo</li>
  <li>Autor y correo electrónico</li>
  <li>Fecha del commit</li>
  <li>Mensaje de confirmación</li>
  <li>Un <em>diff</em> entre ese commit y su ancestro</li>
</ul>

<p>
Si deseas ver una lista más concisa de los commits, puedes ejecutar:
</p>

```bash
$ git log --abbrev-commit --pretty=oneline
```

<p>
Este comando muestra los hashes abreviados a 7 caracteres. En caso de que existan colisiones, Git añadirá más caracteres hasta que cada hash sea único.
</p>


<h3>Referencias por Ramas</h3>

<p>
Para ver la información del último <code>commit</code> de una rama, puedes ejecutar el siguiente comando:
</p>

```bash
$ git show nombre_rama
```

<p>
Este comando mostrará la misma información que si proporcionaras directamente el hash del commit: el identificador SHA-1 completo, el autor, la fecha, el mensaje de confirmación y el <em>diff</em> correspondiente.
</p>

<p>
Si deseas conocer a qué <code>commit</code> (es decir, a qué hash) apunta una rama, puedes utilizar una herramienta de bajo nivel llamada <code>rev-parse</code>:
</p>

```bash
$ git rev-parse nombre_rama
```

<p>
El resultado será el hash SHA-1 completo (40 caracteres) del commit al que apunta dicha rama.
</p>

<div style="border-left: 4px solid #f44336; background: #fff3f3; padding: 0.8em; margin: 1em 0;">
  <strong>Nota técnica:</strong> <code>git rev-parse</code> es una herramienta de plomería de Git, utilizada principalmente para scripts o tareas internas. No es común en flujos de trabajo diarios, pero resulta útil cuando necesitas operar directamente con hashes y referencias internas.
</div>


<h3>Nombres cortos de RefLog</h3>

<p>
Mientras trabajas, Git va guardando un historial interno de los cambios que realizas: commits, cambios de rama, fusiones, etc. Este historial se conoce como <strong>RefLog</strong> y se puede visualizar con el siguiente comando:
</p>

```bash
$ git reflog
```

<p>
El comando mostrará una lista temporal de las acciones recientes realizadas en tu repositorio. Cada entrada del RefLog se muestra con un identificador similar a este:
</p>

```bash
734713b HEAD@{2}: commit: added some blame
```

<p>
Cada elemento <code>HEAD@{n}</code> representa una posición anterior de HEAD, donde <code>n</code> es el número de pasos hacia atrás en el tiempo.
</p>

<p>
Si deseas inspeccionar en detalle uno de estos estados anteriores (por ejemplo, un commit o un cambio de rama), puedes referenciarlo así:
</p>

```bash
$ git show HEAD@{2}
```

<p>
Este comando mostrará toda la información de ese punto específico del historial, incluyendo el commit, mensaje, autor, fecha y diferencias de contenido.
</p>

<div style="border-left: 4px solid #2196f3; background: #eaf4fd; padding: 0.8em; margin: 1em 0;">
  <strong>Consejo:</strong> El RefLog es extremadamente útil para recuperar commits perdidos o para entender cómo ha cambiado el estado de tu repositorio tras varias operaciones complejas.
</div>


<h3>Rangos de Commits</h3>

<p>
Git permite trabajar con rangos de commits utilizando una sintaxis muy flexible. Esto es útil para inspeccionar qué cambios existen entre ramas o entre múltiples referencias.
</p>

<h4>Rango con dos puntos</h4>

<p>
La forma más común es usar dos puntos (<code>..</code>) para ver los commits que están en una rama pero no en otra:
</p>

```bash
$ git log main..nom_rama
```

<p>
Este comando mostrará todos los commits que son alcanzables desde <code>nom_rama</code> pero que no están en <code>main</code>.
</p>

<h4>Rango con múltiples referencias</h4>

<p>
Puedes especificar múltiples referencias para ver commits combinados o excluir explícitamente ciertos commits. Las siguientes sintaxis son equivalentes:
</p>

```bash
$ git log refA refB ^refC
$ git log refA refB --not refC
```

<p>
Ambos comandos muestran todos los commits que están en <code>refA</code> o <code>refB</code>, pero que no están en <code>refC</code>.
</p>

<h4>Rango con tres puntos</h4>

<p>
Cuando usas tres puntos (<code>...</code>), Git mostrará los commits que están en <strong>una u otra</strong> rama, pero <strong>no en ambas</strong>:
</p>

```bash
$ git log refA...refB
```

<p>
Esto es útil para visualizar las diferencias entre dos ramas cuando han tenido desarrollos paralelos.
</p>

<div style="border-left: 4px solid #4caf50; background: #edf7ed; padding: 0.8em; margin: 1em 0;">
  <strong>Nota:</strong> Esta sintaxis también puede utilizarse en otros comandos como <code>git diff</code> o <code>git cherry-pick</code> para aplicar o comparar rangos de commits específicos.
</div>


---

<h2>Organización Interactiva</h2>

<p>
Para asegurarte de que tus confirmaciones estén organizadas de forma lógica y separadas por conjuntos de cambios significativos, puedes usar el modo interactivo del comando <code>git add</code>. Esto se hace añadiendo el parámetro <code>-i</code>:
</p>

```bash
$ git add -i
```

<p>
Esto abrirá una interfaz interactiva en la terminal, en donde se mostrarán los cambios detectados divididos en archivos organizados (<em>staged</em>) y no organizados (<em>unstaged</em>), junto con el resumen de líneas añadidas o eliminadas:
</p>

```bash
staged     unstaged    path
1:         unchanged   +0/-1 TODO
2:         unchanged   +1/-1 index.html
3:         unchanged   +5/-1 lib/simplegit.rb

*** Commands ***
1: status     2: update       3: revert        4: add untracked
5: patch      6: diff         7: quit          8: help

What now>
```

<p>
Con este menú puedes realizar varias acciones como:
</p>
<ul>
  <li>Ver el estado de los archivos (<code>status</code>).</li>
  <li>Actualizar los archivos para agregarlos al área de preparación (<code>update</code>).</li>
  <li>Revertir los cambios pendientes (<code>revert</code>).</li>
  <li>Agregar archivos no rastreados (<code>add untracked</code>).</li>
  <li>Seleccionar fragmentos específicos de cambios en un archivo (<code>patch</code>).</li>
  <li>Ver las diferencias entre versiones (<code>diff</code>).</li>
</ul>

<div style="border-left: 4px solid #2196f3; background: #e3f2fd; padding: 0.8em; margin: 1em 0;">
  <strong>Consejo:</strong> Este método es ideal para separar cambios no relacionados en diferentes commits y mantener tu historial limpio y comprensible.
</div>

---

<h2>Guardado Rápido y Limpieza</h2>

<p>
Imagina que estás trabajando en una rama específica y tu código aún está incompleto o desordenado. Si necesitas cambiar de rama pero no quieres hacer un <em>commit</em> de un código que no funciona, Git te permite guardar temporalmente tu trabajo con el comando <code>stash</code>. Esto te permite retomar tu progreso más adelante sin perder tus cambios.
</p>

```bash
$ git stash
```

<p>
Este comando guarda todos los archivos <strong>rastreados</strong> y limpia tu área de trabajo, permitiéndote cambiar de rama sin conflictos.
</p>

<p>Para listar todos los <code>stash</code> que has guardado usa el comando:</p>

```bash
$ git stash list
```

<p>
Si estás trabajando con archivos nuevos que aún no han sido rastreados con <code>git add</code>, puedes incluirlos en el stash con:
</p>

```bash
$ git stash -u
```

<p>
Cuando estés listo para continuar con tu trabajo guardado, puedes aplicar los cambios con:
</p>

```bash
$ git stash apply
```

<p>
Este comando aplica el último stash, pero <strong>no lo elimina</strong> de la lista. Si deseas aplicar los cambios y eliminar el stash al mismo tiempo, puedes usar:
</p>

```bash
$ git stash pop
```

<div style="border-left: 4px solid #FF9800; background: #FFF3E0; padding: 0.8em; margin: 1em 0;">
  <strong>Nota:</strong> <code>git stash</code> solo guarda los archivos rastreados. Usa <code>-u</code> si deseas incluir los no rastreados también.
</div>


---

<h2>Firmando tu trabajo</h2>

<p>
Git es una herramienta criptográficamente segura. Si trabajas en repositorios compartidos a través de internet y deseas verificar que los <em>commits</em> provienen de una fuente confiable, Git ofrece la posibilidad de <strong>firmar confirmaciones</strong> utilizando <a href="https://gnupg.org" target="_blank">GPG (GNU Privacy Guard)</a>.
</p>


<h3>Introducción a GPG</h3>

<p>
Para comenzar a firmar tus confirmaciones con GPG, necesitas generar una llave personal. Esto se hace ejecutando el siguiente comando:
</p>

```bash
$ gpg --gen-key
```

<p>
Una vez generada tu llave, debes configurar Git para que utilice esa llave al firmar tus commits o etiquetas. Para ello, usa el siguiente comando, reemplazando <code>[llave]</code> por el ID de tu llave GPG:
</p>

```bash
$ git config --global user.signingkey [llave]
```

<p>
Después de esta configuración, Git utilizará por defecto tu llave privada para firmar tus confirmaciones y etiquetas.
</p>


<h3>Firmando Tags</h3>

<p>
Para firmar una etiqueta (tag) con GPG, debes utilizar el parámetro <code>-s</code> en lugar de <code>-a</code> al crearla. Por ejemplo:
</p>

```bash
$ git tag -s nom_tag -m "Descripción"
```

<p>
Esto creará una etiqueta firmada con tu clave GPG configurada previamente.
</p>

<p>
Si deseas ver la firma GPG de una etiqueta, puedes ejecutar el siguiente comando:
</p>

```bash
$ git show nom_tag
```

<h3>Verificando Tags</h3>

<p>
Para verificar una etiqueta (tag) firmada con GPG, utiliza el siguiente comando:
</p>

```bash
$ git tag -v nom_tag
```

<p>
Este comando valida que la firma del tag coincida con la clave GPG del autor. Si la firma es válida, Git mostrará un mensaje indicando que el tag fue firmado correctamente por un usuario confiable.
</p>

<p>
<strong>Nota:</strong> Para que esta verificación funcione correctamente, debes tener importada y confiada la clave pública GPG del autor que creó el tag. Puedes obtener esta clave desde un servidor de claves públicas o directamente del autor.
</p>


<h3>Firmando y Verificando Commits</h3>

<p>
Para firmar un commit con tu clave GPG, debes utilizar la opción <code>-S</code> al momento de confirmar los cambios:
</p>

```bash
$ git commit -S -m "Descripción"
```

<p>
Esto agrega una firma criptográfica al commit, permitiendo validar su autenticidad y origen.
</p>

<p>
Para verificar la firma de un commit, puedes usar el parámetro <code>--show-signature</code> junto con el comando <code>git log</code>:
</p>

```bash
$ git log --show-signature
```

<p>
Este comando mostrará información sobre la firma GPG de cada commit, incluyendo si es válida y a qué clave pertenece.
</p>


---

<h2>Buscando</h2>

<p>
A menudo necesitas buscar dónde se define una función o encontrar el historial de un método específico en tu proyecto. Git proporciona herramientas que permiten examinar el código de forma eficiente utilizando las instantáneas almacenadas en su base de datos.
</p>

<p>
Estas herramientas te permiten rastrear cambios a lo largo del tiempo, facilitando el análisis del historial de archivos, funciones o bloques de código en particular.
</p>


<h3>Git Grep</h3>

<p>
El comando <code>git grep</code> permite buscar rápidamente dentro de cualquier árbol de commits o en el directorio de trabajo utilizando una cadena o una expresión regular.
</p>

<p>Para buscar una palabra específica y ver en qué línea aparece, puedes usar:</p>

```bash
$ git grep -n [palabra]
```

<p>
Este comando mostrará todas las líneas donde aparece la palabra, junto con la ruta del archivo y el número de línea.
</p>

<p>Si deseas una salida más limpia que indique cuántas coincidencias hay por archivo, puedes usar:</p>

```bash
$ git grep --count [palabra]
```

<p>
Entre las ventajas de <code>git grep</code> se encuentran su velocidad y su capacidad para buscar a través de cualquier árbol del repositorio, no solo en el estado actual del directorio de trabajo.
</p>


---

<h2>Rerere</h2>

<p>
El nombre <strong>rerere</strong> proviene de <em>"reuse recorded resolution"</em>, y permite que Git recuerde cómo resolviste un conflicto de fusión (hunk), para que si se vuelve a presentar el mismo conflicto en el futuro, Git pueda resolverlo automáticamente.
</p>

<p>Para habilitar esta funcionalidad, ejecuta el siguiente comando:</p>

```bash
$ git config --global rerere.enabled true
```

<p>
Cuando intentes fusionar dos ramas y se produzca un conflicto, en lugar de usar <code>git status</code>, puedes utilizar el siguiente comando para ver el estado registrado antes de la fusión:
</p>

```bash
$ git rerere status
```

<p>
Una vez que resuelves un conflicto, la solución queda guardada en la caché de <strong>rerere</strong>. Si vuelves a enfrentar el mismo conflicto en el futuro, puedes usar el siguiente comando para que Git lo resuelva automáticamente:
</p>

```bash
$ git rerere
```

<div style="border-left: 5px solid #e74c3c; background-color: #fbeaea; padding: 1em; margin-top: 1.5em;">
  <strong>Advertencia:</strong> Aunque <code>rerere</code> puede ahorrar tiempo, es importante revisar los resultados con atención. Git podría aplicar una resolución pasada que ya no sea válida en el nuevo contexto. Asegúrate de verificar que el conflicto se haya resuelto correctamente antes de hacer commit.
</div>

---

<h2>Haciendo Debug con Git</h2>

<p>
Si encuentras un bug en tu código y quieres saber en qué commit se introdujo, quién escribió esa parte del código y cuándo, puedes usar el comando <code>blame</code>.
</p>

<p>
Si además le pasas el parámetro <code>-L</code>, puedes obtener una lista detallada de cada línea de código en un rango específico. Por ejemplo, supongamos que tienes un archivo llamado <code>file.txt</code> y quieres saber quién escribió las líneas de la 12 a la 22. Puedes ejecutar el siguiente comando:
</p>

```bash
$ git blame -L 12,22 file.txt
```

<p>
Este comando te mostrará para cada línea:
</p>
<ul>
  <li>Los primeros caracteres del hash <strong>SHA-1</strong> del commit</li>
  <li>El nombre del autor</li>
  <li>La fecha en que se hizo el commit</li>
  <li>Y el contenido de la línea correspondiente del archivo</li>
</ul>

---

<h2>Submódulos</h2>

<p>
Los submódulos permiten mantener un repositorio de Git como un subdirectorio dentro de otro repositorio. Esto permite clonar otro repositorio dentro de tu proyecto y mantener sus commits separados.
</p>

<p>
Para crear un nuevo submódulo, se utiliza el comando <code>submodule add</code> con la URL del repositorio que deseas rastrear:
</p>

```bash
$ git submodule add https://github.com/chaconinc/DbConnector
```

<p>
Al ejecutar <code>git status</code>, verás que aparece un archivo llamado <code>.gitmodules</code>. Este archivo almacena la relación entre la URL del submódulo y el subdirectorio local donde se ha insertado. También aparecerá la entrada correspondiente a la carpeta del submódulo.
</p>

<p>
Para clonar un proyecto que contiene submódulos, se debe usar el parámetro <code>--recursive</code> con el comando <code>git clone</code>, así:
</p>

```bash
$ git clone --recursive https://github.com/chaconinc/MainProject
```

<p>
Para mantener el submódulo actualizado, puedes ejecutar <code>git fetch</code> y luego <code>git merge origin/main</code> dentro del submódulo. Estos comandos no deben ejecutarse desde el proyecto principal.
</p>

<p>
Otra forma de actualizar un submódulo es utilizando:
</p>

```bash
$ git submodule update --remote nom_submodule
```

<p>
Este comando actualizará por defecto la rama <code>main</code> del submódulo. Si omites el nombre del submódulo y tienes varios, se actualizarán todos.
</p>

<p>
Para subir los cambios realizados en un submódulo, puedes usar:
</p>

```bash
$ git push --recurse-submodules=on-demand
```

<p>
Este comando empujará primero los cambios del submódulo antes de empujar el proyecto principal.
</p>



---

<h2>Conclusiones</h2>

<p>
En este capítulo exploramos herramientas avanzadas de Git que permiten una manipulación más precisa del área de staging y de los commits. Aprendimos a resolver conflictos comunes durante fusiones de ramas, a rastrear errores mediante herramientas como <code>blame</code> y <code>reflog</code>, y a realizar búsquedas eficientes en el historial del proyecto.
</p>

<p>
Además, se explicó el uso de submódulos, una funcionalidad útil para mantener repositorios separados dentro de un proyecto mayor, así como los comandos necesarios para gestionarlos correctamente.
</p>

<p>
Estas herramientas, aunque no se utilizan diariamente, pueden marcar la diferencia al trabajar en proyectos colaborativos o de larga duración, facilitando el control y mantenimiento del código fuente.
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

