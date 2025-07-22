GitHub

GitHub es el servidor más grande usado por Git, y es el punto de reunión de millones de desarrolladores que hacen trabajo colaborativo en proyectos open sorce.
En este capítulo veremos el uso correcto de GitHub, como crear y gestionar una cuenta, crear y gestionar repositorios, flujos de trabajo para colaborar en proyectos y para aceptar nuevos participantes en los tuyos. 

Creación y configuración de la cuenta

Para crear una cuenta necesitas ingresar a https://github.com, elije un nombre de usuario que esté disponible, proporciona un correo, una contraseña, selecciona tu Ciudad o Región y selecciona el botón “Create acount”


 

Así ya tendrás tu cuenta de GitHub, desde ahorita ya puedes acceder a Git con el protocolo HTTP identificándote con el usuario y contraseña que acabas de escoger. Ahora explicaremos como tener acceso SSH.

Acceso SSH

Como lo vimos en el capítulo pasado, para configurar SSH necesitas una llave publica, para esto selecciona el icono que se encuentra en la parte superior derecha y busca “Ajustes”, en el panel que te abre selecciona “Claves SSH y GPG”. Esta opción te va a abrir otra pantalla y selecciona la opción de “Nueva clave SSH”
 

Dale un nombre a tu clave que puedas recordar como “Cuenta de trabajo” de modo que si tienes que revocar alguna clave te resulte más fácil saber cuál es, después pega el contenido de tu clave privada y selecciona el botón “Agregar clave SSH”
 

Tu icono

En el mismo panel de Ajustes puedes cambiar el icono que se te genero por uno de tu elección, selecciona la opción de “Perfil público” y sobre el icono viene un botón que dice “Editar” con la opción de subir una foto. Esto te permitirá subir una foto que tengas en los archivos de tu computadora. 
 

Tus direcciones de correo

Para identificar tus contribuciones en proyectos, Git usa el correo electrónico, para agregar tus correos electrónicos selecciona la opción de “Correos Electrónicos” dentro de Ajustes. 

 


Participando en Proyectos
Después de tener tu cuenta configurada, veremos como contribuir a un proyecto.

Bifurcación (fork) de proyectos

Si quieres colaborar en un proyecto en el que no tienes permisos de escritura puedes hacer un “fork”, esto consiste en crear una copia del proyecto en la que puedas hacer los cambios que quieras y enviarlos al administrador del proyecto, él te puede dar retroalimentación para que hagas unos ajustes, integrar al proyecto los cambios que hiciste o simplemente rechazarlos.
Para hacer esto tienes que ingresar al proyecto en el que quieres participar y buscar el botón “Fork” que generalmente se encuentra en la parte superior derecha.
Esto generara algo llamado “pull request” que explicaremos más adelante.

Flujo de Trabajo en GitHub
GitHub está diseñado con un flujo de trabajo de colaboración especifico, centrado en las solicitudes de integración (“pull request”). Este flujo de trabajo funciona así:
-	Se crea una rama a partir de main
-	Se realizan algunos commits hacia esa rama
-	Se envía esa rama hacia tu copia (fork) del proyecto
-	Abres un Pull Request en GitHub
-	Se participa en la discusión asociada y opcionalmente se realizan nuevos commits
-	El propietario del proyecto original cierra el PullRequest, fusionando tus cambios con la rama o rechazándolos 

Este es básicamente el flujo de trabajo “Administrador-Integración”, pero en lugar de comunicarse por correo se usa GitHub como medio de comunicación. 

El flujo completo que tienes que seguir para hacer un Fork es el siguiente:
-	Clonar el fork en tu equipo
-	Realizar los cambios
-	Comprobar los cambios
-	Realizar un commit de los cambios 
-	Enviar el commit al fork
-	Te saldrá un aviso en el que te saldrá la opción de hacer una solicitud de integración con el proyecto original.


Pull Requests como parches
Los Pull Requests son colas de parches perfectos que se pueden aplicar limpiamente en orden, casi todos consideran las ramas de pull requests como conversaciones evolutivas acerca de un cambio propuesto.
Cuando el cambio llega con un pull requests y los colaboradores sugieren un cambio, los parches no son directamente alterados, se realiza un nuevo commit en la rama para enviar la diferencia que materializa esas sugerencias.

Manteniéndonos actualizados
Si el pull reuqests se queda anticuado o no se puede fusionar limpiamente lo normal es corregirlo para que el responsable pueda fusionarlo.
Para solucionar esto puedes reorganizar la rama con el contenido de la rama main o fusionar la rama objetivo con la tuya.
La forma más común es fusionar la rama objetivo con tu rama, para hacer esto tienes que seguir los siguientes pasos:
-	Añadir el repositorio original como un nuevo remoto
-	Fusionar la rama principal con la tuya
-	Corregir los errores
-	Enviarla a la rama en donde hiciste la solicitud de integración


Markdown
El formato markdown de GitHuib es como escribir en texto plano pero que luego se convierte en texto con formato, a este formato s ele puede agregar código HTML para hacer tablas, listas, etc.

Lista de tareas
Es una lista de cosas con su marcador para indicar que han terminado, nos sirve para anotar la lista de cosas pendientes a realizar, puedes crear una lista de tareas así:

-	[X] Write the code
-	[ ] Write all the test
-	[ ] Document the code
Puedes pulsar los marcadores para actualizar el comentario indicando que tareas se finalizaron, sin necesidad de editar el código.

Fragmentos de código
Puedes pegar partes de código que quieras documentar o mencionar un error en un cierto bloque de código, también puedes pegar las salidas de los comandos bash, para añadir un fragmento de código se hace de esta manera:

```java 
for(int i=0 ; i < 5 ; i++) 
{   
System.out.println("i is : " + i); 
}
 ```
Si mencionas el lenguaje de programación GitHub intentara hacer el resaltado de la sintaxis del lenguaje, en este caso el fragmento de código es Java

Emojis
Son muy usados para transmitir gracia y emoción en un medio que es muy complicado transmitir las emociones, para agregar un emoji se usa la sintaxis “:nombre:”, por ejemplo: “:happy_face:”

 
Mantenimiento de un proyecto
Ahora que ya sabes cómo colaborar en un proyecto, veremos cómo puedes crear, administrar y mantener tu propio proyecto.

Creación de un repositorio
En tu página principal, en el menú que se encuentra a la derecha busca un botón verde que dice “New”.
 

Ese botón te abrirá un menú en el que tendrás que darle un nombre al repositorio, dar una descripción de lo que contendrá ese repositorio, si tu repositorio será público o privado, te da la opción de agregar un archivo README (es recomendable agregarlo, más adelante explicaremos en que consiste este archivo), te permite agregar un .gitignore y la posibilidad de agregar una licencia.
 
Al terminar de crear el repositorio, podrás compartir la URL del repositorio ya sea como HTTP o como SSH para que los demás puedan ver lo que subes en ese repositorio.

Añadir colaboradores
Si necesitas trabajar con otras personas en ese repositorio necesitas agregarlas como colaboradores, para esto las personas que quieran colaborar necesitan tener su cuenta de GitHub.
Para añadir colaboradores dentro de tu repositorio tendrás una barra de herramientas, busca la opción de “Ajustes” y dentro de Ajustes encontraras la opción de “Colaboradores”, selecciona la opción de “Agregar personas” y búscalas por su nombre de usuario.
 


Gestión de los Pull Requests
Los pull request pueden ser de una rama del mismo repositorio o de una bifurcación del repositorio, en la bifurcación son cambios de gente que no tiene acceso de escritura a tu proyecto y quiere integrar en el tuyo cambios interesantes.
Cuando alguien hace un pull requests te llegara una notificación por correo electrónico, este correo contiene un pequeño “diffsta” y un enlace al Pull Request y algunas URL que puedes usar desde línea de comandos.
Las URL que terminan en .diff y .patch proporcionan “diff unificados” y formatos de parche.

Colaboración con Pull Request
Puedes participar en una discusión con la persona que creo el Pull Request, puedes comentar líneas de código, comentar commits, o comentar el Pull Request completo, en cualquier momento puedes usar el formato Markdown.
Cuando termines la discusión puedes fusionar los cambios con tu rama principal o simplemente cerrar el Pull Request y la persona que lo creo será notificada.

README
El archivo readme puede tener varias extensiones, la más común es README.md, cuando GitHub identifica este archivo lo muestra en la página principal con el renderizado que corresponde a su formato, en este archivo se puede usar Markdown.
Este archivo general ente se usa para incluir información del repositorio, por ejemplo:
-	Para que es el proyecto
-	Como se configura y se instala
-	Ejemplo de uso
-	Licencia del código del proyecto
-	Como participar en el desarrollo
Puedes agregar imágenes y enlaces para facilitar su comprensión. 

CONTRIBUING
Este archivo le especifica a los colaboradores los requisitos para participar en el proyecto, algunas de las cosas que incluye este archivo son:
-	Instrucciones para contribuir
-	Requisitos técnicos 
-	Estilo de código
-	Herramientas necesarias
-	Criterios de aceptación
-	Cosas por evitar 

Conclusiones
En este momento ya tienes creada y configurada una cuenta de GitHub, aprendiste como crear y enviar repositorios, participar en los proyectos de otras personas y aceptar contribuciones de terceros en tus proyectos.
