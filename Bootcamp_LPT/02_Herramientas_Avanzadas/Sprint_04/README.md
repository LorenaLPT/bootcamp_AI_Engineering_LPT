![Cabecera](./assets/cabecera_thebridge.png)

# 📘 Sprint 04 — Herramientas Avanzadas: APIs e IA Generativa

## Bienvenido al Sprint 04

En este sprint final de Herramientas Avanzadas aprenderás a integrar tu código Python con el mundo exterior a través de APIs HTTP y a trabajar con modelos de IA generativa. Estas habilidades son fundamentales para construir aplicaciones modernas que interactúen con servicios en la nube y aprovechen el poder de la IA.

Este sprint se divide en **bloques temáticos**, cada uno con su teoría y su workout.

---

## 🎯 Contenidos del Sprint

### 📖 Bloque 01 — HTTP: Llamadas a APIs

📖 [`01_Teoria/01_HTTP_llamadas_APIs/`](./01_Teoria/01_HTTP_llamadas_APIs/) · 🎯 [`02_Workout/01_HTTP_llamadas_APIs/`](./02_Workout/01_HTTP_llamadas_APIs/) · 📝 [`03_Material_de_Practica/01_HTTP_llamadas_APIs/`](./03_Material_de_Practica/01_HTTP_llamadas_APIs/) · 🧪 [`Practica_live_review/01_HTTP_llamadas_APIs/`](./Practica_live_review/01_HTTP_llamadas_APIs/)

**Tema Central**: Integración con APIs REST y manejo de datos en la nube

En este bloque aprenderás a comunicarte con servidores web a través de HTTP, a consumir APIs públicas y a manejar respuestas en JSON. Estas habilidades te permitirán integrar datos externos en tus aplicaciones Python.

**¿Qué aprenderás?**

- Protocolo HTTP: métodos GET, POST, PUT, DELETE
- Biblioteca `requests` en Python
- Consumo de APIs REST públicas
- Autenticación y manejo de tokens
- Parsing de respuestas JSON
- Manejo de errores y excepciones HTTP
- Rate limiting (error 429) y buenas prácticas de consumo de APIs
- Construcción de clientes API básicos

---

### 🤖 Bloque 02 — IA Generativa con Python: Gemini API

📖 [`01_Teoria/02_IA_generativa_python/`](./01_Teoria/02_IA_generativa_python/) · 🎯 [`02_Workout/02_IA_generativa_python/`](./02_Workout/02_IA_generativa_python/) · 📝 [`03_Material_de_Practica/02_IA_generativa_python/`](./03_Material_de_Practica/02_IA_generativa_python/) · 🧪 [`Practica_live_review/02_IA_generativa_python/`](./Practica_live_review/02_IA_generativa_python/)

**Tema Central**: Integración de Gemini en aplicaciones Python a través de Google AI Studio

En este bloque trabajarás con **Gemini**, el modelo de IA generativa de Google, aprendiendo a construir prompts efectivos e integrar esta poderosa herramienta en tus aplicaciones Python. Utilizarás Google AI Studio para experimentar y la Gemini API para integrar IA generativa en tu código.

**¿Qué aprenderás?**

- Gemini API y Google AI Studio: acceso y configuración
- Prompting efectivo con Gemini
- Modelos de lenguaje: características y limitaciones
- Construcción de aplicaciones con Gemini en Python
- Streams y respuestas en tiempo real
- Tokens y límites de uso (error 429)
- Casos de uso: clasificación, generación, análisis
- Consideraciones éticas en IA generativa

#### Qué modelo de Gemini usar

Usa uno de estos modelos en la variable `MODEL`. Son de la **capa gratuita** de la API de Gemini (comprobados en noviembre de 2026).

| Modelo (`MODEL = …`) | ¿Cuándo usarlo? |
|---|---|
| `gemini-3.6-flash` | **Recomendado** para todo el sprint (texto, JSON, `system_instruction`, streaming y chat) |
| `gemini-3.5-flash-lite` | Alternativa más ligera si el anterior da `429` o `503` |
| `gemini-3.8-flash` | El más nuevo; en horas punta puede dar `503 UNAVAILABLE` (saturado) |

**No uses** `gemini-3-flash-preview` (ya no existe: `404 NOT_FOUND`) ni `gemini-2.5-flash` (solo disponible para cuentas que ya lo usaban y, con `google-genai` 3.x, sin modo JSON ni `system_instruction`).

**Si te sale un error:**
- `503 UNAVAILABLE` → modelo saturado: espera unos segundos y reintenta, o cambia de modelo.
- `429 RESOURCE_EXHAUSTED` → has gastado tu cuota gratuita (por minuto o por día): espera y no repitas celdas sin necesidad.
- `404 NOT_FOUND … is not found` → el nombre del modelo no existe: revisa cómo lo has escrito.
- `400 … API key not valid` → la clave de tu `.env` no es correcta.

**Lista actualizada:** modelos gratuitos y precios en <https://ai.google.dev/pricing> (columna «Free tier»). Los modelos que tu clave puede usar:

```python
from google import genai
client = genai.Client()
print([m.name for m in client.models.list() if "flash" in m.name])
```

---

## 📚 Estructura de Carpetas

```
Sprint_04/
├── README.md              ← Este documento
├── 01_Teoria/             ← Material teórico, un subdirectorio por bloque
├── 02_Workout/            ← Workouts, un subdirectorio por bloque
├── 03_Material_de_Practica/ ← Ejercicios y práctica extra que no son del workout, un subdirectorio por bloque
└── Practica_live_review/  ← Material de la Live Review (si el sprint lo incluye)
```

Dentro de cada carpeta encontrarás un subdirectorio por bloque temático. Los ejercicios con solución para repasar están en `03_Material_de_Practica`, en el bloque correspondiente.

---

## 🆘 Ayuda y Recursos

Si algo no funciona o tienes dudas:

1. **Revisa el README del bloque** — Contiene detalles específicos (`readme.md` dentro de `01_Teoria/<bloque>/`)
2. **Consulta la Teoría** — Lee los notebooks/documentos con atención
3. **Pregunta en las Sesiones** — Los profesores y compañeros están para ayudarte
4. **Usa los Foros o Mensajería** — Si no puedes asistir, contacta al equipo
