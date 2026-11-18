# Catálogo de películas · Team Challenge

> Renombrad este fichero a `README.md` y completad las partes entre `<...>`.

**Equipo:** <nombre 1>, <nombre 2>, <nombre 3>, <nombre 4>

Catálogo de películas enriquecido a partir del dataset MovieLens: análisis con Pandas, sinopsis y web oficial desde la API de TMDB, y sinopsis en español generadas con Gemini.

## Reparto de funciones

| Persona | Rol | Notebook / tarea |
|---|---|---|
| <nombre> | <rol> | <notebook> |

## Instalación

```bash
git clone <URL del repo>
cd <carpeta>
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env            # y rellenad las claves
```

## Claves necesarias

| Variable | Dónde se obtiene |
|---|---|
| `TMDB_READ_ACCESS_TOKEN` o `TMDB_API_KEY` | themoviedb.org → Settings → API |
| `GEMINI_API_KEY` | aistudio.google.com |

## Ejecución

Ejecutad los notebooks **en este orden** (cada uno genera un CSV en `data/processed/` que usa el siguiente):

1. `01_ingesta_limpieza.ipynb` → `movies_clean.csv`
2. `02_analisis.ipynb`
3. `03_tmdb.ipynb` → `movies10.csv`
4. `04_gemini.ipynb` → `movies10_es.csv`

## Resultados principales

<3–5 frases con lo más interesante que habéis encontrado>
