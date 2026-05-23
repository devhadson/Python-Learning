## CONTENIDO

[REGRESAR README](../README.md)

[CLONAR O SINCRONIZAR CODIGO DESDE GITHUB](#clonar-o-sincronizar-codigo-desde-github)

[ENTORNO VIRTUAL PYTHON](#entorno-virtual-python)

# CLONAR O SINCRONIZAR CODIGO DESDE GITHUB

GitHub es la plataforma de control de versiones más utilizada del mundo, basada en Git. Para trabajar con ella, el flujo fundamental consiste en **descargar** el código a tu máquina local y, tras realizar modificaciones, **subir** tus componentes o cambios de vuelta al repositorio.

A continuación, encontrarás los comandos esenciales para dominar este flujo y cómo ejecutar tus scripts de Python 3 en las dos terminales principales.

---

## 1. Descarga de Código desde GitHub (Clonar o Sincronizar)

Para traer el código de un repositorio a tu computadora, el método principal es la **clonación**. Si el repositorio ya existe en tu máquina y solo quieres traer los últimos cambios del equipo, usas una **sincronización**.

### Clonar un repositorio por primera vez

Abre tu terminal (Bash o PowerShell), navega hasta la carpeta donde quieras guardar el proyecto y ejecuta:

```bash
git clone https://github.com/devhadson/Python-Learning.git
```

*Esto creará una carpeta con el nombre del proyecto y descargará todos los archivos.*

### Actualizar tu código local

Si alguien más subió cambios y necesitas actualizar tu carpeta local, muévete dentro del proyecto y ejecuta:

```bash
git pull origin main

```

*(Nota: Reemplaza main por master o el nombre de la rama correspondiente si tu repositorio usa otra configuración).*

---

## 2. Carga de Componentes y Cambios a GitHub

Cuando creas un nuevo archivo de Python o modificas componentes existentes, debes seguir el "ciclo de vida" de Git para enviarlos a la nube: **Rastrear $\rightarrow$ Registrar $\rightarrow$ Subir**.

```bash
# Paso 1: Añadir los archivos modificados o nuevos al área de preparación (Staging)
git add nombre_del_archivo.py

# Si quieres añadir todos los archivos nuevos y modificados de golpe:
git add .

# Paso 2: Registrar los cambios con un mensaje descriptivo (Commit)
git commit -m "Añade componente de procesamiento de datos"

# Paso 3: Subir los cambios a tu repositorio remoto en GitHub (Push)
git push origin main
```

---

## 3. Ejecución de Archivos Python 3

Una vez que tienes el código en tu máquina, la forma de invocar el intérprete de Python varía ligeramente según la terminal y el sistema operativo. Asumiendo que tienes un archivo llamado app.py:

### Desde Bash (Linux / macOS / Git Bash en Windows)

En entornos basados en Unix o emuladores como Git Bash, el comando por defecto para la versión 3 suele requerir especificar el 3 de forma explícita para distinguirlo de versiones obsoletas.

```bash
python3 app.py
```

*Si estás usando Git Bash en Windows y el comando anterior no responde, intenta con:*

```bash
python app.py
```

### Desde PowerShell (Windows)

PowerShell generalmente reconoce el comando estándar de Windows o el lanzador de Python (py), el cual busca automáticamente la versión más reciente instalada en el sistema.

```powershell
python app.py
```

*Si tienes múltiples versiones instaladas y quieres forzar explícitamente el uso de Python 3, el lanzador py es la mejor opción:*

```powershell
py -3 app.py
```

### Verificación de la ruta (Tip de solución de problemas)

Si al ejecutar los comandos anteriores recibes un error del tipo *"command not found"* o *"no se reconoce como un comando interno"*, significa que Python no está en las variables de entorno de tu sistema (PATH). Asegúrate siempre de marcar la casilla **"Add Python to PATH"** durante la instalación.

Un **entorno virtual** en Python es, en esencia, un espacio aislado dentro de tu computadora dedicado a un proyecto específico.

# ENTORNO VIRTUAL PYTHON

Imagina que tienes dos proyectos: el Proyecto A necesita una librería de analítica de datos en su versión 1.0, y el Proyecto B necesita la versión 2.0 de esa misma librería porque la antigua ya no es compatible. Si instalaras todo de forma global en tu sistema, ambos proyectos chocarían. El entorno virtual resuelve esto creando una carpeta independiente con su propio ejecutable de Python y sus propias librerías instaladas.

---

## 1. ¿Para qué sirve un entorno virtual?

* **Evita conflictos:** Cada proyecto tiene sus propias dependencias sin importar lo que requieran otros proyectos.
* **Mantiene limpio tu sistema:** No saturas la instalación global de Python con paquetes que solo usarás una vez.
* **Facilita la replicación:** Te permite generar un archivo de texto (normalmente llamado requirements.txt) con la lista exacta de lo que tu código necesita para que otra persona —o un servidor en la nube— lo ejecute sin problemas.

---

## 2. Creación del Entorno Virtual (Común para ambos)

Primero, abre tu terminal y muévete con el comando cd a la carpeta de tu proyecto. El comando para *crear* el entorno es prácticamente el mismo en cualquier terminal, ya que invoca al módulo interno venv de Python.

**En Bash (Linux/macOS) o Git Bash (Windows):**

```bash
python3 -m venv .venv
```

**En PowerShell (Windows):**

```powershell
python -m venv .venv
```

*(Nota: .venv es el nombre de la carpeta que se creará. Puedes llamarla como quieras, pero .venv o env son las convenciones estándar y el punto inicial la mantiene oculta en sistemas Unix).*

---

## 3. Activación del Entorno

Aquí es donde los caminos se separan, ya que cada terminal utiliza un script diferente para modificar las variables de entorno de tu sesión actual. Sabrás que se activó correctamente porque verás el nombre del entorno entre paréntesis (.venv) al inicio de la línea de comandos.

### Desde Bash (Linux / macOS / Git Bash)

Para indicarle a Bash que use los binarios del entorno local, ejecutamos el script activate mediante el comando source:

```bash
source .venv/bin/activate
```

*Si estás usando Git Bash en Windows, la ruta cambia ligeramente a:*

```bash
source .venv/Scripts/activate
```

### Desde PowerShell (Windows)

En PowerShell, ejecutamos directamente el script de activación diseñado para esta terminal:

```powershell
.venv\Scripts\Activate.ps1
```

> ⚠️ **Error común en PowerShell (Restricción de scripts):**
> Si te aparece un error en rojo que dice *"Script execution is disabled on this system"*, se debe a la política de seguridad interna de Windows. Puedes solucionarlo de manera temporal para esa ventana ejecutando:
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
> Y luego vuelve a lanzar el comando de activación.

---

## 4. ¿Cómo se usa una vez activo?

Una vez que ves el (.venv) en tu terminal, cualquier paquete que instales mediante pip se quedará guardado únicamente dentro de esa carpeta.

```bash
# Ejemplo: Instalar una librería de manera aislada
pip install requests

# Guardar la lista de dependencias para tus repositorios de GitHub
pip freeze > requirements.txt
```

### Para salir del entorno (Desactivar)

Cuando termines de trabajar y quieras volver al Python global de tu sistema, no importa si estás en Bash o PowerShell, simplemente escribe:

```bash
deactivate
```

---

*Documentación elaborado por [Hadson Paredes](https://www.linkedin.com/in/hadson-paredes/) - 2026*

<hr>
<h4 align="center"> Publicaciones en mis redes sociales y repositorio GitHub</h4>

<div align="center">
  <h3>Sígueme en mis redes sociales</h3>
  <a href="https://github.com/devhadson">
    <img src="https://img.shields.io/badge/GitHub-devhadson-black?logo=GitHub&style=flat-square" target="_blank" alt="GitHub">
  </a>
  <a href="https://www.linkedin.com/in/hadson-paredes/">
    <img src="https://img.shields.io/badge/LinkedIn-Hadson%20Paredes-blue?logo=linkedin&style=flat-square" target="_blank" alt="LinkedIn">
  </a>
  <a href="https://www.facebook.com/hadson.paredescordova/">
    <img src="https://img.shields.io/badge/Facebook-Hadson%20Paredes%20Cordova-Gree?logo=facebook&style=flat-square" target="_blank" alt="Facebook">
  </a>
  <a href="https://x.com/hadson_paredes">
    <img src="https://img.shields.io/badge/Hadson%20Paredes-black?logo=x&style=flat-square" target="_blank" alt="X">
  </a>
</div>