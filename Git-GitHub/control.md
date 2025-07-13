<p align="center">
  <img src="https://git-scm.com/images/logo@2x.png" width="200" alt="Git Logo"/>
</p>

<h1 align="center"><code>CONTROL DE VERSIONES</code></h1>

## Introducción

En este capítulo aprenderás a utilizar Git desde cero. Se presentarán los conceptos fundamentales del control de versiones y se configurará Git por primera vez.  
Al finalizar esta sección, comprenderás las ventajas de utilizar Git y estarás listo para comenzar a trabajar con tu propio repositorio local.

---

## ¿Qué es el control de versiones?

<p align="center">
  <img src="https://dinahosting.com/blog/upload/2018/06/Control-de-versiones.jpg" width="600" alt="Version Control Diagram"/>
</p>

El **control de versiones** es un sistema que permite gestionar los cambios realizados a uno o varios archivos a lo largo del tiempo.  
Este tipo de herramienta es fundamental en proyectos de software, diseño, documentación y cualquier entorno donde sea necesario.
El control de versiones puede:

- Recuperar versiones anteriores de archivos.
- Comparar cambios entre versiones.
- Identificar quién y cuándo se realizaron modificaciones.
- Restaurar archivos dañados o eliminados accidentalmente.

---

## Tipos de sistemas de control de versiones

###  Control de versiones local

<p align="center">
  <img src="https://miro.medium.com/v2/resize:fit:998/0*1Dnudw5qEB7yaXvd.jpg" width="500" alt="Local Version Control"/>
</p>

En este modelo, los cambios se registran únicamente en el equipo local del usuario.

> Uno de los sistemas más populares fue **RCS (Revision Control System)**, que almacenaba las diferencias entre versiones (conjuntos de parches) en archivos especiales.  
Esto permitía reconstruir cualquier versión de un archivo a partir de sus cambios.

**Ventajas:**
- Rápido acceso a cambios locales.
- No requiere conexión a red.

**Desventajas:**
- No está diseñado para colaboración.
- Riesgo de pérdida total si se daña el equipo.

---

###  Control de versiones centralizado (CVCS)

<p align="center">
  <img src="https://aulasoftwarelibre.github.io/taller-de-git/images/git-central.png" width="400" alt="Centralized Version Control"/>
</p>

Este modelo introdujo un **servidor central** que almacena la versión principal del proyecto. Los colaboradores se conectan a él para obtener y enviar cambios.

**Ventajas:**
- Coordinación más sencilla entre equipos.
- Permite establecer permisos por usuario.

**Desventajas:**
- Si el servidor falla o se pierde la conexión, se bloquea todo el trabajo.
- El historial puede perderse si no se hacen respaldos.

Ejemplos de CVCS: Subversion (SVN), CVS.

---

###  Control de versiones distribuido (DVCS)

<p align="center">
  <img src="https://pressroom.hostalia.com/contents/ui/theme/images/sites/4/control-versiones-distribuidos-blog-hostalia-hosting.jpg" width="400" alt="Distributed Version Control"/>
</p>

En un DVCS como Git, **cada colaborador tiene una copia completa del repositorio**, incluyendo su historial completo.

**Ventajas:**
- Si el servidor principal falla, cualquier copia puede restaurar el proyecto.
- Permite flujos de trabajo descentralizados y colaborativos.
- Mayor velocidad de operación: los comandos se ejecutan localmente.

**Ejemplo principal:** Git.

---

## Fundamentos del funcionamiento de Git

Git no guarda versiones como diferencias entre archivos. En su lugar, **almacena capturas completas ("snapshots") del estado del proyecto** en momentos clave.

### 📌 Instantáneas y eficiencia

Cada vez que confirmas un cambio (commit), Git toma una instantánea de todos los archivos y guarda una referencia a esa imagen.  
Si un archivo no ha cambiado, Git simplemente referencia la versión ya almacenada, sin duplicarlo.

---

### 📌 Operaciones locales

Casi todas las operaciones de Git se realizan localmente. Esto significa que:

- No necesitas conexión a internet para trabajar con el historial o realizar commits.
- Las búsquedas, comparaciones y restauraciones son muy rápidas.

---

### 📌 Seguridad y verificación

Git utiliza un sistema de **suma de comprobación** (hash) para garantizar la integridad de los datos.  
Cada archivo y commit es identificado de forma única mediante un **hash SHA-1**, una cadena de 40 caracteres generada a partir del contenido.

Ejemplo de hash SHA-1:


    24b9da6552252987aa493b52f8696cd6d3b00373



Este mecanismo hace prácticamente imposible modificar archivos sin que Git lo detecte.

---

## Estados de los archivos en Git

Git clasifica los archivos en tres **estados**:

| Estado       | Descripción                                                                 |
|--------------|-----------------------------------------------------------------------------|
| Confirmado   | El archivo ha sido almacenado de forma permanente en el repositorio (commit). |
| Modificado   | El archivo ha cambiado, pero aún no ha sido preparado para el commit.         |
| Preparado    | El archivo ha sido marcado para incluirse en el siguiente commit.             |

---

## Áreas de trabajo en Git

Git organiza su funcionamiento en tres **áreas principales**:

| Área                     | Función                                                                 |
|--------------------------|-------------------------------------------------------------------------|
| Directorio de Git        | Contiene la base de datos interna con todos los objetos y versiones.    |
| Directorio de trabajo    | Es la versión actual del proyecto, visible y editable.                  |
| Área de preparación      | Zona donde se agrupan los cambios que se incluirán en el próximo commit. |

<p align="center">
  <img src="https://gahd.net/media/2021/10/git-areas-5fa84808-0acb-440b-95be-cb384b161869.png" width="550" alt="Git staging area"/>
</p>

---

## Flujo de trabajo básico en Git

```text
1. Modificas archivos en tu directorio de trabajo.
2. Añades los cambios al área de preparación (staging).
3. Confirmas los cambios (commit) y Git los almacena en el repositorio.
```

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
