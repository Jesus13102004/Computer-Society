<p align="center">
  <img src="https://git-scm.com/images/logo@2x.png" width="200" alt="Git Logo"/>
</p>

<h1 align="center"><code>GIT EN ENTORNOS DISTRIBUIDOS</code></h1>


<h2>Introducción</h2>

<p>
En este capítulo aprenderás cómo trabajar con Git en un entorno distribuido, ya sea como colaborador o como integrador. 
Veremos cómo contribuir de forma adecuada a un proyecto, asegurando buenas prácticas tanto para quien aporta cambios como para quien mantiene el repositorio. 
También abordaremos cómo gestionar eficientemente un proyecto con múltiples desarrolladores, facilitando la colaboración y la integración continua.
</p>

---

<h2>Flujos de trabajo distribuidos</h2>

<p>
En Git, cada desarrollador es potencialmente un nodo o un repositorio completo. Esto significa que cada integrante del equipo puede contribuir a otros repositorios y, al mismo tiempo, mantener su propio repositorio público, el cual puede servir como base para el trabajo de otros desarrolladores.
</p>

<p>
Esta arquitectura distribuida permite una gran variedad de flujos de trabajo posibles. A continuación, exploraremos los más comunes y efectivos para entornos colaborativos.
</p>

<h3>Flujo de trabajo centralizado</h3>

<p>
Un sistema centralizado se basa en un único repositorio central que acepta código. Todos los desarrolladores sincronizan su trabajo con este punto central.
</p>

<p>
Esto significa que si dos desarrolladores clonan el repositorio y ambos realizan cambios, solo el primero que haga <code>push</code> podrá subir sus cambios directamente. El segundo desarrollador tendrá que realizar una fusión (<code>merge</code>) para integrar los cambios del primero con los suyos, evitando sobrescribir el trabajo ya publicado.
</p>

<p align="center">
  <img src="https://www.sergiorus.com/images/blog/2015/centralized-vcs.png" alt="Flujo de trabajo centralizado" width="500"/>
</p>


<h3>Flujo de trabajo Administrador-Integración</h3>

<p>
Git permite trabajar con múltiples repositorios remotos, lo que habilita un flujo en el que cada desarrollador tiene acceso de escritura a su propio repositorio público y acceso de lectura a los demás. Este flujo de trabajo suele seguir estos pasos:
</p>

<ol>
  <li>El administrador del proyecto realiza un <code>push</code> al repositorio principal.</li>
  <li>Un colaborador clona el repositorio y realiza sus cambios localmente.</li>
  <li>El colaborador publica sus cambios en su propio repositorio público mediante un <code>push</code>.</li>
  <li>El administrador realiza un <code>pull</code> para obtener los cambios del colaborador.</li>
  <li>El administrador agrega el repositorio del colaborador como remoto y fusiona ambos repositorios localmente.</li>
  <li>Finalmente, el administrador hace un <code>push</code> de la fusión al repositorio principal.</li>
</ol>

<p>
Este flujo permite que el colaborador continúe trabajando sin interrupciones, mientras que el administrador tiene control total sobre qué cambios integrar y cuándo hacerlo.
</p>

<p><strong>Ventaja:</strong> El contribuidor puede seguir trabajando de manera independiente y el administrador puede incorporar los cambios cuando lo considere oportuno.</p>


<p align="center">
  <img src="https://git-scm.com/book/es/v2/images/integration-manager.png" alt="Flujo de trabajo Administrador-Integración" width="500"/>
</p>


<h3>Flujo de trabajo Dictador-Tenientes</h3>

<p>
Este flujo de trabajo es común en proyectos de gran escala con cientos de colaboradores. Se estructura en varios niveles de integración para facilitar la gestión del código. 
</p>

<p>
En este modelo, existen varios administradores de integración llamados <strong>"tenientes"</strong>, quienes se encargan de coordinar los cambios en distintas áreas del proyecto. Todos los tenientes reportan a un gerente de integración conocido como el <strong>"dictador benévolo"</strong>. El repositorio del dictador actúa como el repositorio principal del proyecto.
</p>

<p>El flujo de trabajo se desarrolla de la siguiente manera:</p>

<ol>
  <li>Los desarrolladores trabajan en sus propias ramas y eventualmente fusionan sus cambios con la rama <code>main</code>, la cual es una copia de la rama <code>main</code> del dictador.</li>
  <li>Los tenientes revisan y fusionan el código de las ramas <code>main</code> de los desarrolladores hacia sus propias ramas <code>main</code>.</li>
  <li>El dictador revisa y fusiona las ramas <code>main</code> de los tenientes en su propia rama <code>main</code> del repositorio principal.</li>
  <li>Finalmente, el dictador realiza un <code>push</code> al repositorio principal para que todos los colaboradores puedan actualizar sus copias con los cambios más recientes.</li>
</ol>

<p>
Este enfoque jerárquico permite escalar la colaboración en proyectos muy grandes, manteniendo al mismo tiempo un alto nivel de control sobre qué cambios se integran en el repositorio central.
</p>


<p align="center">
  <img src="https://git-scm.com/book/es/v2/images/benevolent-dictator.png" alt="Flujo de trabajo dictador-tenientes" width="550"/>
</p>

---

<h2>Conclusión</h2>

<p>
Trabajar con Git en un entorno distribuido ofrece una gran flexibilidad para colaborar de manera eficiente y estructurada, independientemente del tamaño del equipo o la escala del proyecto.
</p>

<p>
Hemos explorado diversos flujos de trabajo:
</p>

<ul>
  <li><strong>Flujo centralizado</strong>: ideal para equipos pequeños que trabajan sobre un único repositorio principal.</li>
  <li><strong>Flujo administrador-integración</strong>: permite a cada colaborador tener su repositorio público y al administrador centralizar los cambios.</li>
  <li><strong>Flujo dictador-tenientes</strong>: altamente escalable y se adapta bien a comunidades grandes y distribuidas, permitiendo una delegación jerárquica del control del proyecto.</li>
</ul>

<p>
Cada uno de estos enfoques tiene ventajas específicas según el contexto. Lo importante es elegir el modelo que mejor se ajuste a la estructura de tu equipo y a la naturaleza de tu desarrollo, asegurando una colaboración fluida, un historial limpio y un código bien integrado.
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

