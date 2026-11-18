"""Revisa en un segundo si un proyecto Python está bien montado.

Uso, desde la carpeta del proyecto:
    con venv (entorno activado):  python ruta/a/check_entorno.py
    con uv:                       uv run python ruta/a/check_entorno.py

No necesita instalar nada. Comprueba:
  1. que Python se está ejecutando dentro de un entorno virtual;
  2. que la versión de Python es 3.12 o 3.13 (la recomendada en el curso);
  3. que hay una lista de dependencias (requirements.txt o pyproject.toml + uv.lock);
  4. que el .gitignore ignora .venv/ y el fichero .env;
  5. que .env no está ya guardado en Git.
"""

import subprocess
import sys
from pathlib import Path

OK, AVISO, MAL = "✅", "⚠️ ", "❌"
resultados = []


def informe(estado, texto, consejo=""):
    resultados.append(estado)
    print(f"{estado} {texto}")
    if consejo and estado != OK:
        print(f"     → {consejo}")


def git(*args):
    try:
        r = subprocess.run(["git", *args], capture_output=True, text=True)
        return r.returncode, r.stdout.strip()
    except FileNotFoundError:
        return 127, ""


def main():
    carpeta = Path.cwd()
    print(f"Revisando: {carpeta}\n")

    # 1. ¿Dentro de un entorno virtual?
    if sys.prefix != sys.base_prefix:
        informe(OK, f"Estás dentro de un entorno virtual ({sys.prefix})")
    else:
        informe(MAL, "Estás usando el Python global, no un entorno virtual",
                "activa el entorno (source .venv/Scripts/activate en Git Bash, "
                "source .venv/bin/activate en macOS/Linux) o usa 'uv run python ...'")

    # 2. Versión de Python
    v = sys.version_info
    if (v.major, v.minor) in [(3, 12), (3, 13)]:
        informe(OK, f"Python {v.major}.{v.minor}.{v.micro}")
    else:
        informe(AVISO, f"Python {v.major}.{v.minor}: el curso recomienda 3.12 o 3.13",
                "con uv: 'uv python pin 3.12' y 'uv sync'; con venv: crea el .venv con un Python 3.12/3.13")

    # 3. Lista de dependencias
    req = (carpeta / "requirements.txt").exists()
    pyproj = (carpeta / "pyproject.toml").exists()
    lock = (carpeta / "uv.lock").exists()
    if req or (pyproj and lock):
        cuales = ", ".join(n for n, e in [("requirements.txt", req), ("pyproject.toml", pyproj), ("uv.lock", lock)] if e)
        informe(OK, f"Lista de dependencias: {cuales}")
    elif pyproj:
        informe(AVISO, "Hay pyproject.toml pero falta uv.lock", "ejecuta 'uv lock' o añade un paquete con 'uv add'")
    else:
        informe(MAL, "No hay requirements.txt ni pyproject.toml",
                "venv: 'python -m pip freeze > requirements.txt' · uv: 'uv init' + 'uv add ...'")

    # 4 y 5. Git
    codigo, _ = git("rev-parse", "--is-inside-work-tree")
    if codigo != 0:
        informe(AVISO, "Esta carpeta no es un repositorio Git", "si vas a compartir el proyecto: 'git init'")
    else:
        if not (carpeta / ".gitignore").exists():
            informe(MAL, "No hay .gitignore en la raíz del proyecto", "crea el .gitignore del curso (apartado 5)")
        # git check-ignore dice si Git ignoraría esas rutas, aunque no existan
        for ruta, nombre in [(".venv/", "la carpeta .venv/"), (".env", "el fichero .env")]:
            c, _ = git("check-ignore", "-q", "--no-index", ruta)
            if c == 0:
                informe(OK, f"Git ignora {nombre}")
            else:
                informe(MAL, f"Git NO ignora {nombre}",
                        f"añade la línea '{ruta}' al .gitignore" +
                        (" (ojo: '.env/' con barra no sirve para el fichero)" if ruta == ".env" else ""))
        c, salida = git("ls-files", "--error-unmatch", ".env")
        if c == 0:
            informe(MAL, ".env ya está guardado en Git: tus claves están en el historial",
                    "'git rm --cached .env', commit, y ANULA las claves en la web del proveedor")
        else:
            informe(OK, ".env no está en Git")

    print()
    if MAL in resultados:
        print("Hay cosas que arreglar (❌). Pregunta en el chat si te atascas.")
        sys.exit(1)
    print("Todo listo 🎉")


if __name__ == "__main__":
    main()
