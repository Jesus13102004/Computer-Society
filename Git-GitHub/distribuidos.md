Git en entornos distribuidos

En este capítulo veremos como trabajar con Git en un entorno distribuido, como colaborador o como integrador, es decir, aprenderemos a contribuir adecuadamente a un proyecto tanto para ti como para el responsable del proyecto y también como mantener adecuadamente un proyecto con múltiples desarrolladores 

Flujos de trabajo distribuidos 

En Git cada desarrollador es potencialmente un nodo o un repositorio, es decir, cada desarrollador puede contribuir a otros repositorios y mantener un repositorio público en el cual otros pueden basar su trabajo y al cual pueden contribuir.
Esto permite un enorme rango de posibles flujos de trabajo que veremos a continuación.

Flujo de trabajo centralizado

Un sistema centralizado es un repositorio o punto central que acepta código y todos sincronizan su trabajo con él. Esto ocasiona que, si dos desarrolladores clonan el punto central y ambos hacen cambios, solo el primero podrá subir sus cambios sin problemas, mientras que el segundo tendrá que fusionar el trabajo del primero con el suyo para no sobrescribir los cambios del primero.

Flujo de trabajo Administrador-Integración
 
Git permite tener varios repositorios remotos, es posible tener un flujo de trabajo donde cada desarrollador tenga acceso de escritura a su propio repositorio publico y acceso de lectura a todos los demás, el proceso funcional de este flujo de trabajo es el siguiente:
-	El administrador del proyecto hace un push al repositorio publico
-	El contribuidor clona el repositorio y realiza cambios
-	El contribuidor realiza un push con su copia publica del proyecto
-	El administrador hace un pull a los cambios
-	El administrador agrega el repositorio del contribuidor como remoto y fusiona ambos localmente
-	El administrador realiza un push con la fusión del código al repositorio principal
La principal ventaja de este flujo de trabajo es que el contribuidor puede seguir haciendo cambios y el administrador puede incorporar los cambios en cualquier momento

Flujo de trabajo Dictador-Tenientes
Este flujo de trabajo es utilizado en proyectos en donde hay cientos de colaboradores, tiene. Varios administradores de integración que están a cargo de ciertas partes del proyecto, a estos se les llama “tenientes”, todos los tenientes tienen un gerente de integración conocido como el “dictador benévolo”. El repositorio del dictador funciona como el repositorio principal. 
El flujo de trabajo funciona así:
-	Los desarrolladores trabajan en su propia rama y fusionan su código con la rama main, la cual es una copia de la rama del dictador
-	Los tenientes fusionan el código de las ramas main de los desarrolladores con las ramas main de tenientes
-	El dictador fusiona la rama main de los tenientes a su rama main de dictador
-	El dictador hace push del contenido de su rama main al repositorio para que otros fusionen los cambios a sus ramas

Conclusiones
 
