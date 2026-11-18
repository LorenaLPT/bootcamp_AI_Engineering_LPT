# config.py — reglas del juego (sin lógica de negocio)

VALID_TIPOS = ["summary", "translate", "qa"]

PRIORIDAD_MIN = 1
PRIORIDAD_MAX = 5

import re

PATRON_CODIGO = re.compile(r"^TKT-\d{4}$")

# Placeholder para el bloque de Prompt Engineering (sin llamar a la API en este bloque)
MODEL = "gemini-proximamente"
