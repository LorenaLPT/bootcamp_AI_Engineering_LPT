# Pre-work · Taller T02 Entornos virtuales (venv + uv)

**Hazlo antes de la sesión (unos 30 minutos).** En la sesión no hay tiempo para instalar: al empezar solo comprobaremos que todo funciona.

Terminal del curso: **Git Bash** en Windows, **Terminal** en macOS y la terminal de **Linux**.

---

## 1. Git y Git Bash (si ya hiciste el pre-work del taller de Git, salta al paso 2)

- **Windows:** instala [Git for Windows](https://git-scm.com/downloads/win), que trae **Git Bash**.
- **macOS:** ejecuta `git --version` en Terminal; si no lo tienes, el sistema te ofrecerá instalarlo.
- **Linux (Ubuntu/Debian):** `sudo apt install git`.

Configura tu identidad y la rama `main` (cambia nombre y email):

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
git config --global init.defaultBranch main
```

## 2. Python 3.12 o 3.13

Recomendamos **3.12 o 3.13**: algunas librerías de IA tardan en publicarse para las versiones más nuevas.

**Windows**, elige una opción:

- **A (recomendada) · Python install manager.** Instálalo desde la [Microsoft Store](https://apps.microsoft.com/detail/9NQ7512CXL7T) o desde [python.org/downloads](https://www.python.org/downloads/). Después, en Git Bash:

  ```bash
  py install 3.13
  py list          # muestra las versiones instaladas
  ```

- **B · Instalador clásico.** Descarga el instalador de **Python 3.13** en [python.org/downloads/windows](https://www.python.org/downloads/windows/) y marca **«Add python.exe to PATH»** al instalar.

**macOS:** instalador de **Python 3.13** desde [python.org/downloads/macos](https://www.python.org/downloads/macos/) (o `brew install python@3.13` si usas Homebrew).

**Linux (Ubuntu/Debian):** `sudo apt install python3 python3-venv` (el paquete `python3-venv` hace falta para crear entornos).

## 3. uv

Abre la terminal indicada, pega el comando y **cierra y vuelve a abrir la terminal** al terminar.

- **Windows** (en **PowerShell**, solo esta vez):

  ```powershell
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```

  o, si usas WinGet: `winget install --id=astral-sh.uv -e`

- **macOS / Linux:**

  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

  o, en macOS con Homebrew: `brew install uv`

Deja descargado el Python que usaremos con uv (así no esperas en la sesión):

```bash
uv python install 3.12
```

## 4. VS Code

Instala [VS Code](https://code.visualstudio.com/) y, dentro, las extensiones **Python** y **Jupyter** (las dos de Microsoft). Comprueba que el comando `code` funciona en la terminal: `code --version`. Si no funciona en macOS, en VS Code abre la paleta (`Cmd+Shift+P`) y ejecuta **Shell Command: Install 'code' command in PATH**.

## 5. Comprobación final

Copia y pega este bloque en Git Bash, Terminal o la terminal de Linux:

```bash
python --version 2>/dev/null || python3 --version
uv --version
uv python find 3.12
git config --global user.name
git config --global init.defaultBranch
code --version | head -1
```

Debes ver, en este orden:

- tu versión de Python;
- la versión de uv;
- una ruta a Python 3.12;
- tu nombre;
- `main`;
- la versión de VS Code.

**Al empezar la sesión te pediremos que pegues esta salida en el chat.**

> ❓ ¿Algo falla? Escribe en el canal del curso **antes** de la sesión, con el error copiado tal cual.
