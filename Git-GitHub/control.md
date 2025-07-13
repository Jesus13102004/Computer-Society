Control de Versiones

Inicio
En este capitulo aprenderemos a como empezar a utilizar Git, describire algunos conceptos basicos de las herramientas de control de versiones y configuraremos Git por primera vez.
Al final de este capitulo tendras que ser capaz de entender las ventajas de usar git, y tendras todo listo para empezar a usarlo.

Control de Versiones
El control de versiones es un sistema que permite gestionar los cambios realizados a un archivo o conjunto de archivos a lo largo del tiempo.
Este sistema permite:
- Regresar a versiones anteriores 
- Comparar cambios
- Saber quien y cuando modifico un archivo
- Si se pierde o arruina un archivo se puede recuperar

    Control de Versiones Locales:
    La herramienta de Control de Versiones Local mas popular fue el sistema RCS, esta herramienta funciona guardando conjuntos de parches (las diferencias entre archivos), en un formato especial en disco, es capaz de recrear como era un archivo en cualquier momento.

    Control de Versiones Centralizados:
    Este control de versiones soluciona el problema del trabajo colaborativo, ya que el proyecto se guarda en un servidor al que tienen acceso los miembros del equipo.
    Su ventaja principal es que los administradores tienen el control sobre que puede hacer cada colaborador
    Su principal desventaja es que al estar todo en un solo servidor si este servidor se cae se puede perder todo el proyecto.

    Control de Versiones Distribuido:
    Este control de versiones replica completamente el repositorio, de esta manera si un servidor deja de funcionar cualquier copia del repositorio puede restaurar los datos perdidos en el servidor, esto tambien permite establecer varios flujos de trabajo como los modelos jerarquicos.

Fundamentos de Git
- Git maneja los datos como un conjunto de copias instantaneas, cada que se guarda el estado del proyecto en git basicamente toma una foto de todos los archivos en ese momento y guarda una referencia a esa copia.
Para ser eficiente, si los archivos no se han modificado, Git no almacena el archivo de nuevo, solo hace un enlace al archivo almacenado.

- Casi todo su funcionamiento es local por lo que no necesita internet para funcionar, esto hace que el sistema sea muy rapido ya que tiene todo el historial del proyecto en el disco local, por lo que las consultas a los archivos antiguos es inmediata.

- Todo en git es verificado mediante una suma de comprobacion antes de ser almacenado. Esto ayuda a que sea imposible cambiar los contenidos de cualquier archivo sin que Git lo sepa.
El mecanismo que usa git para generar esta suma se llama **hash SHA-1**, es una cadena de 40 caracteres hexadecimales que se calcula en base a los contenidos del archivo. Un hash SHA-1 se ve asi:
    24b9da6552252987aa493b52f8696cd6d3b00373

Git tiene tres estados en los que pueden estar los archivos:
- Confirmado (commited): Los datos estan almacenados de manera segura en la base de datos
- Modificado (modified): Se modifico el archivo pero todavia no esta confirmado
- Preparado (staged): Marco un archivo modificado en su version actual para que vaya en la proxima confirmacion

Git tiene tres secciones principales:
- Directorio de Git: Se almacenan los metadatos y la base de datos de los objetos del proyecto. Es la parte mas importante
- Directorio de Trabajo: Es una copia de una version del proyecto.
- Area de Preparación: Almacena la informacion que va a ir en la siguiente confirmacion.

El flujo de trabajo basico es:
- Se modifican archivos en el directorio de trabajo
- Se preparan los archivos añadiendolos al area de preparacion
- Se confirman los cambios y se guardan permanentemente en el directorio de Git.