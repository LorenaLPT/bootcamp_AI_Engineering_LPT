<!-- Generado desde fuenrk.md con buirk.py. No lo edites a mano. -->
# Taller · Entornos virtuales en Python (venv + uv)

Taller de 90 minutos del bootcamp de AI Engineering. Al terminar sabrás **para qué sirve** un entorno virtual, **cómo crearlo** con `venv` y con `uv` y **cómo trabajar con él**: instalar paquetes, compartirlo con Git y usarlo en un notebook de VS Code.

## Qué hay en esta carpeta

| Fichero | Para qué |
|---------|----------|
| `prework.md` | **Hazlo antes de la sesión** (≈ 30 min): instalar Python, uv, Git y VS Code |
| `Entornos_Virtuales.ipynb` | El material de la sesión (el mismo contenido que este README) |
| `README.md` | Este fichero: el material completo para leer en GitHub o en el navegador |
| `check_entorno.py` | Revisa en un segundo si tu proyecto está bien montado |

> 💡 El notebook se lee, no se ejecuta: los comandos se escriben en la **terminal** (Git Bash, macOS o Linux). Solo hay una celda de código, en el apartado 7.

---



<div align="center">

# 🐍 Entornos Virtuales en Python

**Aísla, instala, reproduce — como un profesional**

*venv · pip · requirements.txt · uv · VS Code*

</div>

---

> 🎯 **Objetivo de la sesión (90 min):** al terminar sabrás **para qué sirve** un entorno virtual, **cómo crearlo** con `venv` y con `uv`, y **cómo trabajar con él** en el día a día: instalar paquetes, compartir el proyecto con Git y usar el entorno en un notebook de VS Code.

> ✅ **Antes de la sesión** tienes que haber hecho el pre-work (`prework.md`): Python 3.12 o 3.13, `uv`, Git configurado y VS Code con las extensiones *Python* y *Jupyter*.

## Índice

1. [¿Qué es un entorno virtual y por qué lo necesitas?](#1-qué-es-un-entorno-virtual-y-por-qué-lo-necesitas)
2. [Crear y activar un entorno con `venv`](#2-crear-y-activar-un-entorno-con-venv)
3. [Instalar paquetes en el entorno](#3-instalar-paquetes-en-el-entorno)
4. [Compartir dependencias con `requirements.txt`](#4-compartir-dependencias-con-requirementstxt)
5. [Entornos virtuales y Git](#5-entornos-virtuales-y-git)
6. [`uv`: lo mismo, más rápido y con menos pasos](#6-uv-lo-mismo-más-rápido-y-con-menos-pasos)
7. [Usar el entorno en un notebook de VS Code](#7-usar-el-entorno-en-un-notebook-de-vs-code)
8. [Chuleta](#8-chuleta)
9. [Ejercicio extra: proyecto en pareja](#9-ejercicio-extra-proyecto-en-pareja)
10. [Para saber más](#10-para-saber-más)

### Cómo leer los comandos

Todos los comandos están pensados para **Git Bash** (Windows), **Terminal** (macOS) o la terminal de **Linux**. Cuando cambian según el sistema, verás las dos versiones:

| Qué | Windows (Git Bash) | macOS / Linux |
|-----|--------------------|---------------|
| Llamar a Python **fuera** de un entorno | `python` | `python3` |
| Activar un entorno | `source .venv/Scripts/activate` | `source .venv/bin/activate` |

> 💡 **Dentro** de un entorno activado, `python` funciona igual en los tres sistemas. A partir de ahí usamos siempre `python`.

---
## 1. ¿Qué es un entorno virtual y por qué lo necesitas?

Sin entorno virtual, todo lo que instalas con `pip` va al **Python global** de tu ordenador, que es uno solo para todos tus proyectos. Si dos proyectos necesitan versiones distintas del mismo paquete, chocan:

```
Python global (uno para todo):
  pandas 2.3   ← el Proyecto A lo necesita así
  pandas 3.1   ← el Proyecto B lo necesita así
  Solo puede haber una. ¿Cuál gana? 💥
```

Un entorno virtual es una **carpeta dentro de tu proyecto** (normalmente `.venv/`) con su propio Python y sus propios paquetes:

```
proyecto-a/
  .venv/          ← pandas 2.3, numpy 2.2 ...
  main.py
proyecto-b/
  .venv/          ← pandas 3.1, scikit-learn 1.9 ...
  main.py
```

> 🧑‍🍳 **Analogía:** es como tener una despensa separada para cada receta. El sofrito de la paella no se mezcla con los ingredientes del tiramisú.

### Ventajas

- **Aislamiento:** instalar o actualizar algo en un proyecto no rompe otro.
- **Reproducibilidad:** cualquiera puede recrear tu entorno a partir de una lista de paquetes.
- **Limpieza:** el Python global se queda como estaba.
- **Es lo estándar:** cualquier equipo de desarrollo trabaja así.

> 🔑 **La idea que tienes que llevarte:** el entorno (`.venv/`) **no se comparte**. Lo que se comparte es la **lista de paquetes** (`requirements.txt` o `pyproject.toml` + `uv.lock`). Cada persona crea su propio entorno a partir de esa lista.

---
## 2. Crear y activar un entorno con `venv`

`venv` viene con Python: no hay que instalar nada.

### Crear el entorno

Desde la carpeta de tu proyecto:

```bash
# Windows (Git Bash)
python -m venv .venv

# macOS / Linux
python3 -m venv .venv
```

Esto crea la carpeta `.venv/` con una copia de Python y de `pip`. El entorno usa **la versión de Python con la que lo creas**: compruébala antes con `python --version` (macOS/Linux: `python3 --version`).

> 💡 **¿Te sale Python 3.14 o más nuevo?** En el curso recomendamos 3.12 o 3.13, porque algunas librerías tardan en estar disponibles para las versiones más nuevas. Si tienes varias instaladas, elige una al crear el entorno: `py -3.13 -m venv .venv` (Windows) o `python3.13 -m venv .venv` (macOS/Linux). Con `uv` es todavía más fácil (apartado 6).

> 💡 Por convención se llama `.venv` (el punto la oculta en el explorador). Podrías llamarla de otra forma, pero `.venv` es lo que esperan VS Code, `uv` y el `.gitignore` de este curso.

### Activar el entorno

Hay que activarlo **cada vez que abras una terminal nueva**.

| Terminal | Comando |
|----------|---------|
| Git Bash (Windows) | `source .venv/Scripts/activate` |
| macOS / Linux | `source .venv/bin/activate` |
| PowerShell (Windows) | `.venv\Scripts\Activate.ps1` |
| CMD (Windows) | `.venv\Scripts\activate.bat` |

Al activarlo, el prompt muestra el nombre del entorno delante:

```
(.venv) usuario@maquina:~/proyecto-demo$
```

### Comprobar que estás dentro

```bash
python -c "import sys; print(sys.prefix)"   # debe terminar en .../proyecto-demo/.venv
which python                                # Git Bash, macOS y Linux → .../.venv/...
```

> 💡 La primera línea es la prueba buena: funciona igual en todos los sistemas y no depende del prompt.

### Desactivar el entorno

```bash
deactivate
```

El `(.venv)` desaparece. A partir de aquí, lo que instales iría al Python global.

> ⚠️ **¿Usas PowerShell y te sale *«la ejecución de scripts está deshabilitada»*?** Ejecuta una vez `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`, o usa **Git Bash**, que es la terminal del curso.

### ✍️ Ejercicio 1 · Tu primer entorno virtual

1. Crea una carpeta `proyecto-demo` y entra en ella: `mkdir proyecto-demo && cd proyecto-demo`.
2. Crea un entorno virtual llamado `.venv`.
3. Actívalo y comprueba con `python -c "import sys; print(sys.prefix)"` que estás dentro.
4. Ejecuta `python -m pip list`. Debería salir **solo `pip`**:

```
Package Version
------- -------
pip     26.2.2
```

5. Desactívalo con `deactivate` y vuelve a ejecutar el `sys.prefix`. ¿Qué ha cambiado?

> 💬 *Tu versión de `pip` puede ser otra: no importa.*

---
## 3. Instalar paquetes en el entorno

Con el entorno **activado**:

```bash
python -m pip install requests              # un paquete
python -m pip install requests httpx        # varios a la vez
python -m pip install "httpx==0.28.1"       # una versión exacta
python -m pip install --upgrade requests    # actualizar
python -m pip uninstall requests            # desinstalar
```

Para ver qué tienes:

```bash
python -m pip list            # todos los paquetes del entorno
python -m pip show requests   # información de uno concreto
```

> 🔑 **¿Por qué `python -m pip` y no solo `pip`?** Porque así usas el `pip` del Python que estás ejecutando. Si se te olvida activar el entorno, `pip` a secas puede instalar en otro sitio sin avisarte.

> ⚠️ **Cuidado con copiar versiones antiguas de internet.** Una línea como `numpy==1.26.4` **no se puede instalar en Python 3.13**: no existe esa versión ya preparada para tu Python, así que `pip` intenta compilarla y se queda colgado o falla con `No matching distribution found`. Si no necesitas una versión concreta, instala **sin versión** y deja que `pip` elija la más reciente compatible.

---
## 4. Compartir dependencias con `requirements.txt`

Un `requirements.txt` es la **lista de paquetes** (con su versión) que necesita tu proyecto. Es lo que compartes con el equipo, en lugar de la carpeta `.venv/`.

### Generar el fichero

Con el entorno activado y los paquetes instalados:

```bash
python -m pip freeze > requirements.txt
cat requirements.txt
```

Si instalaste `requests` y `httpx`, verás algo así:

```
anyio==4.16.0
certifi==2026.10.23
charset-normalizer==3.5.2
h11==0.16.0
httpcore==1.0.9
httpx==0.28.1
idna==3.20
requests==2.34.2
typing_extensions==4.16.0
urllib3==2.8.0
```

> 🤔 **¿Por qué 10 líneas si instalé 2 paquetes?** Porque `requests` y `httpx` necesitan a su vez otros paquetes (sus *dependencias*), y `pip freeze` apunta **todo** lo que hay en el entorno. Así quien lo reproduzca tendrá exactamente lo mismo.

### Instalar desde el fichero

Quien recibe el proyecto crea su propio entorno y ejecuta:

```bash
python -m pip install -r requirements.txt
```

### Buenas prácticas

- **Versiones exactas (`==`)** en proyectos que se entregan o se despliegan: máxima reproducibilidad. Es lo que genera `pip freeze`.
- **Rangos (`>=`)** solo si escribes el fichero a mano y quieres flexibilidad, por ejemplo `pandas>=2.2`.
- **La versión de Python** no cabe en `requirements.txt`. Indícala en el `README` (*«Python 3.12 o 3.13»*). Con `uv` queda guardada automáticamente en `.python-version` (lo verás en el apartado 6).

### ✍️ Ejercicio 2 · Instalar y reproducir

**Parte A · en `proyecto-demo`**

1. Activa el entorno e instala `requests` y `httpx`.
2. Genera el `requirements.txt` y ábrelo. ¿Cuántas líneas tiene? ¿Por qué?
3. Desactiva el entorno.

**Parte B · simula a un compañero**

1. Sal a la carpeta de arriba y crea `proyecto-colega`: `cd .. && mkdir proyecto-colega && cd proyecto-colega`.
2. Crea y activa un entorno nuevo.
3. Instala con el fichero del ejercicio anterior: `python -m pip install -r ../proyecto-demo/requirements.txt`.
4. Comprueba que los dos entornos son idénticos:

```bash
python -m pip freeze | diff - ../proyecto-demo/requirements.txt && echo "✅ Idénticos"
```

---
## 5. Entornos virtuales y Git

La carpeta `.venv/` **nunca se sube al repositorio**: pesa cientos de MB, depende de tu sistema operativo y cualquiera puede recrearla en segundos.

| Se sube a Git ✅ | No se sube ❌ |
|------------------|---------------|
| `requirements.txt` (o `pyproject.toml` + `uv.lock` + `.python-version`) | `.venv/` |
| `.gitignore` | `.env` (tus claves de API) |
| `.env.example` (los nombres de las claves, sin valores) | `__pycache__/`, `.ipynb_checkpoints/` |

### El `.gitignore` del curso

Crea el `.gitignore` en la raíz del proyecto. Es el mismo que en el taller de Git:

```gitignore
# Claves y secretos
.env

# Entornos virtuales
.venv/
venv/

# Python y Jupyter
__pycache__/
.ipynb_checkpoints/
```

> ⚠️ **`.env` y `.env/` no son lo mismo.** `.env` (sin barra) ignora el **fichero** donde guardas las claves. `.env/` (con barra) solo ignora una **carpeta** con ese nombre, y tu fichero de claves se subiría a GitHub. Si una clave llega a subirse, hay que **anularla y crear otra**: borrar el commit no basta.

> 💡 **Dato:** desde Python 3.13, `venv` crea dentro de `.venv/` un pequeño `.gitignore` que la oculta a Git automáticamente (`uv` hace lo mismo). Aun así, deja `.venv/` en el `.gitignore` del proyecto: no todo el mundo tiene Python 3.13 ni usa estas herramientas.

### Flujo completo

> ✅ Necesitas Git configurado (nombre, email y rama `main`), como en el pre-work del taller de Git. Si no, `git commit` falla con *«Author identity unknown»*.

```bash
# 1. Proyecto con Git
mkdir mi-proyecto && cd mi-proyecto
git init

# 2. Entorno
python -m venv .venv                 # macOS/Linux: python3
source .venv/Scripts/activate        # macOS/Linux: source .venv/bin/activate

# 3. Dependencias
python -m pip install requests
python -m pip freeze > requirements.txt

# 4. .gitignore (copia el bloque de arriba) y commit
git add .gitignore requirements.txt
git commit -m "chore: add requirements and gitignore"

# 5. Subir a GitHub: como en el taller de Git (gh repo create ... o git remote add + git push)
```

Y quien clona el proyecto:

```bash
git clone <url> && cd mi-proyecto
python -m venv .venv                 # macOS/Linux: python3
source .venv/Scripts/activate        # macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
```

### ✍️ Ejercicio 3 · Entornos y Git

En `proyecto-demo`:

1. Inicializa un repositorio: `git init`.
2. Crea el `.gitignore` del curso (el bloque de arriba).
3. Crea un `.env` de mentira: `echo "OPENAI_API_KEY=sk-de-mentira" > .env`.
4. Ejecuta `git status`. Deben aparecer **solo** `.gitignore` y `requirements.txt`. Ni `.venv/` ni `.env`.
5. Haz un commit con esos dos ficheros.
6. Comprueba lo que Git está ignorando: `git status --ignored`.

> 🧪 **Prueba a romperlo:** cambia en el `.gitignore` la línea `.env` por `.env/` y vuelve a ejecutar `git status`. ¿Qué aparece? Déjalo como estaba antes de seguir.

---
## 6. `uv`: lo mismo, más rápido y con menos pasos

[`uv`](https://docs.astral.sh/uv/) es una herramienta moderna que hace en uno lo que antes eran varios pasos: crea el entorno, instala paquetes, apunta las dependencias **y además instala la versión de Python que pidas**. Por dentro sigue creando un `.venv/` normal: todo lo que has aprendido sigue valiendo.

Hay dos formas de usarlo. Las dos son válidas y en este curso verás ambas:

| | **Modo proyecto** (recomendado para proyectos nuevos) | **Modo compatible** (como `pip`, pero más rápido) |
|---|---|---|
| Cuándo | Empiezas un proyecto desde cero | El proyecto ya usa `requirements.txt` (por ejemplo, un Team Challenge) |
| Lista de paquetes | `pyproject.toml` + `uv.lock` | `requirements.txt` |
| Comandos | `uv init`, `uv add`, `uv run`, `uv sync` | `uv venv`, `uv pip install ...` |
| ¿Hay que activar? | No: `uv run` usa el `.venv` del proyecto | Sí, como con `venv` |

### 6.1 Modo proyecto

```bash
uv init --no-package --python 3.12 proyecto-uv   # crea la carpeta, pyproject.toml, .python-version, main.py y un repo Git
cd proyecto-uv
uv add requests                       # crea .venv, instala y apunta la dependencia
uv run main.py                        # ejecuta con el Python del proyecto, sin activar nada
```

Qué ha creado `uv`:

| Fichero | Para qué sirve | ¿A Git? |
|---------|----------------|---------|
| `pyproject.toml` | Lista de dependencias **que tú pediste** (`requests`) y versión mínima de Python | ✅ |
| `uv.lock` | **Todas** las versiones exactas, también las dependencias de tus dependencias (como `pip freeze`, pero automático) | ✅ |
| `.python-version` | La versión de Python del proyecto (`3.12`) | ✅ |
| `.venv/` | El entorno, igual que con `venv` | ❌ (ya viene en su `.gitignore`) |

Quien clona el proyecto solo necesita **un comando**:

```bash
git clone <url> && cd proyecto-uv
uv sync          # crea el .venv con la misma versión de Python y los mismos paquetes
```

Otros comandos útiles:

```bash
uv remove requests          # quitar una dependencia
uv add --dev ipykernel      # dependencia solo para desarrollo (la usarás en el apartado 7)
uv python install 3.13      # instalar otra versión de Python
uv python pin 3.13          # cambiar la versión del proyecto (escribe .python-version)
```

> 💡 **¿Por qué `--no-package`?** Desde uv 0.12 (julio de 2026), `uv init` sin opciones crea un proyecto preparado para publicarse como paquete: mete el código en `src/` y **no crea `main.py`**. Para scripts y notebooks del bootcamp es más sencillo el proyecto plano que crea `--no-package`. Si ves tutoriales donde `uv init` crea `main.py` directamente, son de versiones anteriores.

> ⚠️ `uv python pin` no puede elegir una versión menor que la que dice `requires-python` en el `pyproject.toml`. Por eso, al crear el proyecto, usa `--python 3.12`: así el proyecto acepta 3.12 o superior.

### 6.2 Modo compatible (`uv pip`)

Mismos pasos que con `venv` + `pip`, cambiando el comando:

```bash
uv venv --python 3.12                     # crea .venv (si no tienes 3.12, uv lo descarga)
source .venv/Scripts/activate             # macOS/Linux: source .venv/bin/activate
uv pip install -r requirements.txt        # mucho más rápido que pip
uv pip freeze > requirements.txt          # generar la lista
```

> 💡 **Del modo proyecto a `requirements.txt`:** si alguien te pide el fichero clásico, ejecuta `uv export --format requirements.txt --no-hashes > requirements.txt`.

### ✍️ Ejercicio 4 · Proyecto con `uv`

1. Vuelve a tu carpeta de trabajo (la que contiene `proyecto-demo`).
2. Crea el proyecto: `uv init --no-package --python 3.12 proyecto-uv` y entra en él.
3. Mira qué ha creado: `ls -a` y `cat pyproject.toml`.
4. Añade `requests` con `uv add requests`. Vuelve a mirar el `pyproject.toml`: ¿qué ha cambiado? ¿Qué es `uv.lock`?
5. Ejecuta el programa de ejemplo: `uv run main.py`.
6. Comprueba la versión de Python sin activar nada: `uv run python --version`.
7. `uv` ya creó un `.gitignore` con `.venv`, pero **no incluye `.env`**. Añade las líneas del curso: `printf '.env\n.ipynb_checkpoints/\n' >> .gitignore`.
8. Haz un commit: `git add . && git commit -m "chore: proyecto uv"`.
9. Simula a un compañero: `cd .. && git clone proyecto-uv proyecto-uv-colega && cd proyecto-uv-colega && uv sync`. ¿Ha hecho falta crear o activar el entorno a mano?

### ✍️ Ejercicio 5 · Modo compatible

1. Crea `proyecto-compat` junto a los anteriores y entra.
2. Crea el entorno con `uv venv --python 3.12` y actívalo.
3. Instala con `uv pip install -r ../proyecto-demo/requirements.txt`. Compara la velocidad con el ejercicio 2.
4. Desactívalo.

---
## 7. Usar el entorno en un notebook de VS Code

En un notebook, los paquetes no los busca la terminal, sino el **kernel**: el Python que ejecuta las celdas. Si el kernel no es el de tu `.venv`, verás `ModuleNotFoundError` aunque hayas instalado el paquete.

### Pasos

1. Instala `ipykernel` en el entorno (VS Code lo necesita para usarlo como kernel):

```bash
# Proyecto con uv
uv add --dev ipykernel

# Proyecto con venv (con el entorno activado)
python -m pip install ipykernel
```

2. Abre **la carpeta del proyecto** en VS Code: `code .` (o *File → Open Folder*).
3. Crea o abre un notebook (`.ipynb`).
4. Arriba a la derecha pulsa **Select Kernel** → **Python Environments** → elige el que apunta a **`.venv`**.
5. Comprueba en una celda qué Python estás usando (celda siguiente).

> 💡 Si `.venv` no aparece en la lista, abre la paleta (`Ctrl+Shift+P` / `Cmd+Shift+P`) y ejecuta **Developer: Reload Window**. Si VS Code te ofrece instalar `ipykernel`, acepta.

*Celda de código del notebook:*

```python
# Ejecuta esta celda: la ruta debe terminar en .venv/... de tu proyecto
import sys
print(sys.executable)
```

### ✍️ Ejercicio 6 · El kernel correcto

1. En `proyecto-uv`, añade `ipykernel` con `uv add --dev ipykernel` y abre la carpeta con `code .`.
2. Crea `prueba.ipynb`, elige el kernel de `.venv` y ejecuta `import sys; print(sys.executable)`.
3. En otra celda, ejecuta `import requests; print(requests.__version__)`. Debe funcionar.
4. **Provoca el error:** cambia el kernel al Python global y vuelve a ejecutar la celda de `requests`. ¿Qué error sale? Vuelve a poner el kernel de `.venv`.
5. *(Opcional)* Revisa tu proyecto con el script del taller: copia `check_entorrk.py` (está en la carpeta del taller) a tu carpeta de trabajo y, desde `proyecto-uv`, ejecuta `uv run python ../check_entorrk.py`.

---
## 8. Chuleta

| Quiero... | `venv` + `pip` | `uv` (modo proyecto) |
|-----------|----------------|----------------------|
| Crear el proyecto y el entorno | `python -m venv .venv` | `uv init --no-package --python 3.12 nombre` (el `.venv` se crea con el primer `uv add` o `uv sync`) |
| Activarlo | `source .venv/Scripts/activate` (Win) · `source .venv/bin/activate` (Mac/Linux) | No hace falta: `uv run ...` |
| Instalar un paquete | `python -m pip install requests` | `uv add requests` |
| Quitar un paquete | `python -m pip uninstall requests` | `uv remove requests` |
| Ejecutar un script | `python main.py` | `uv run main.py` |
| Guardar la lista | `python -m pip freeze > requirements.txt` | Automático (`pyproject.toml` + `uv.lock`) |
| Reproducir un proyecto | `python -m pip install -r requirements.txt` | `uv sync` |
| Elegir versión de Python | La que tengas instalada | `uv python install 3.12` · `uv python pin 3.12` |
| Salir | `deactivate` | — |

> 📦 **Regla de oro:** `.venv/` y `.env` en el `.gitignore`; la lista de paquetes (`requirements.txt` o `pyproject.toml` + `uv.lock`) en el repo.

---
## 9. Ejercicio extra: proyecto en pareja

> ⭐ **Opcional.** Necesita GitHub y lo visto en el taller de Git (cuenta, `gh auth login`, colaboradores).

**Persona A**

1. Crea el repo y clónalo: `gh repo create mi-api --public --clone` y `cd mi-api`.
2. Inicializa el proyecto en esa carpeta con `uv init --no-package --python 3.12` y añade `uv add fastapi uvicorn`.
3. Sustituye `main.py` por una API mínima:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hola():
    return {"mensaje": "hola"}
```

4. Pruébala: `uv run uvicorn main:app --reload` y abre http://127.0.0.1:8000. Para pararla, `Ctrl+C`.
5. Completa el `.gitignore` que creó `uv` con las líneas del curso (`.env`, `__pycache__/`, `.ipynb_checkpoints/`), haz commit y `git push`. Añade a B como colaborador (*Settings → Collaborators*).

**Persona B**

1. Clona el repo de A y entra en la carpeta.
2. Reproduce el entorno con `uv sync`.
3. Comprueba que funciona: `uv run python -c "import fastapi; print(fastapi.__version__)"` y arranca la API como hizo A.

> 🔁 **Variante sin uv:** A usa `venv` + `python -m pip install fastapi uvicorn` + `python -m pip freeze > requirements.txt`; B usa `python -m pip install -r requirements.txt`.

**Reflexión:** ¿qué habría pasado si A hubiera subido el `.venv/` al repo? ¿Y si hubiera subido un `.env` con una clave real?

---
## 10. Para saber más

*Nada de esta sección es necesario para la sesión.*

| Herramienta | Qué es | Cuándo te la puedes encontrar |
|-------------|--------|-------------------------------|
| **conda** | Gestor de entornos y paquetes que también instala librerías de C/C++ y otros lenguajes | Proyectos de ciencia de datos antiguos o con dependencias de sistema complicadas |
| **pyenv** / **pyenv-win** | Instala varias versiones de Python | Hoy `uv python install` hace lo mismo con un comando |
| **virtualenv** | La herramienta de entornos anterior a `venv`, que se sigue manteniendo | Herramientas que la usan por dentro |
| **Python install manager** | El instalador oficial de Python en Windows (comandos `py install 3.12`, `py list`) | Si instalas Python desde python.org en Windows |

### Conda en 1 minuto

```bash
conda create --name mi_entorno python=3.12
conda activate mi_entorno
conda install numpy pandas
conda env export --from-history > environment.yml   # solo lo que tú pediste: sirve en otros sistemas
conda env create -f environment.yml
```

> ⚖️ **Licencia:** `conda` es gratis, pero el canal de paquetes por defecto de Anaconda (`defaults`) exige licencia de pago a organizaciones de 200 personas o más. Si lo necesitas en una empresa, instala **Miniforge**, que usa el canal comunitario `conda-forge`.

### Enlaces

- [venv — documentación oficial de Python](https://docs.python.org/3/library/venv.html)
- [uv — documentación oficial](https://docs.astral.sh/uv/)
- [Usar Python en Windows (Python install manager)](https://docs.python.org/3/using/windows.html)
- [Kernels de Jupyter en VS Code](https://code.visualstudio.com/docs/datascience/jupyter-kernel-management)
- [Miniforge](https://github.com/conda-forge/miniforge)
