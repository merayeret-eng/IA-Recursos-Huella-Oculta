# IA y Recursos: La Huella Oculta

Visualización interactiva que explora el costo ambiental de la inteligencia artificial
a través de tres dimensiones: **agua**, **energía** y **memoria**.

**Autor:** Aaron Mera — Máster Data Science UOC, Visualización de Datos
**URL:** [aaronmera.github.io/IA-Recursos-Huella-Oculta](https://aaronmera.github.io/IA-Recursos-Huella-Oculta)

---

## Preguntas de Investigación

1. **P1 - Agua:** ¿Cómo ha evolucionado el consumo de agua de Google, Microsoft y Meta?
   ¿Cuál es el costo hídrico de cada consulta de IA?

2. **P2 - Energía:** ¿Cuál es la tendencia de consumo eléctrico de los centros de datos?
   ¿Cómo se compara el costo energético entre distintos modelos de IA?

3. **P3 - Memoria:** ¿Por qué sube el precio de la memoria DRAM/HBM y cómo se relaciona
   con el costo de entrenar modelos de IA?

4. **P4 - Equivalencias:** ¿Cómo se relacionan estas tres dimensiones y qué significan
   en términos cotidianos?

---

## Dataset

Los datos se compilaron desde fuentes primarias y se organizan en 3 archivos CSV:

| Archivo | Filas | Variables | Fuentes |
|---------|-------|-----------|---------|
| `datos/agua.csv` | 29 | 14 | Google, Microsoft, Meta, Li et al. |
| `datos/energia.csv` | 31 | 13 | IEA, Amazon, Epoch AI |
| `datos/memoria.csv` | 25 | 12 | TrendForce, NVIDIA, OpenAI |

### Variables

- **10 categóricas:** empresa, tipo_recurso, dimensión, escenario, región, tipo_medición,
  tipo_memoria, tecnología, fabricante, aplicación
- **18 cuantitativas continuas:** consumo_energía_TWh, consumo_agua_total_BL,
  emisiones_CO2_Mt, precio_unitario_USD, mercado_B_USD, Wh_por_query, etc.
- **4 temporales:** año, trimestre, periodo_fiscal
- **2 lógicas:** es_proyección, verified_source

---

## Tecnología

- **Visualización:** D3.js v7 + TopoJSON — gráficos SVG interactivos con scroll storytelling y mapamundi coroplético
- **Procesamiento:** Python 3.11 + pandas para compilación de datos
- **Estilo:** CSS3 vintage con diseño responsivo, paleta sepia/parchment/rust/gold, tipografía Playfair Display + IBM Plex Mono
- **Sin dependencias externas** (excepto D3.js v7 y TopoJSON vía CDN)

---

## Estructura del Proyecto

```
proyecto_PET/
├── index.html              # Visualización principal (scroll storytelling, 12 charts, 6 secciones)
├── compilar_datos.py       # Script Python para generar CSVs
├── VALIDACION.md           # Documento de validación y checklist de rúbrica
├── README.md               # Este archivo
├── PROPUESTA_DEFINITIVA_IA_Recursos_Huella_Oculta.md
├── PROPUESTA_DEFINITIVA_IA_Recursos_Huella_Oculta.html
├── Propuesta_4_IA_Recursos_Huella_Oculta.md
├── datos/
│   ├── agua.csv            # Consumo de agua Google, Microsoft, Meta (2019-2026)
│   ├── energia.csv         # Consumo eléctrico IEA, emisiones CO2 (2009-2035)
│   └── memoria.csv         # Precios DDR5, HBM, costos entrenamiento (2020-2026)
└── LICENSE
```

---

## Fuentes

- IEA (2025) — *Energy and AI*. International Energy Agency.
- Google (2025) — *Environmental Report 2025*.
- Microsoft (2025) — *2025 Environmental Sustainability Report*.
- Microsoft (2025) — *AI Diffusion Index H2 2025*.
- Meta (2024-2025) — *Sustainability Data Index*.
- Li et al. (2023) — *Making AI Less "Thirsty"*. arXiv:2304.03271.
- Epoch AI (2025) — *Data on AI compute and energy trends*.
- TrendForce (2025-2026) — *DRAM/HBM Market Reports*.
- Similarweb / OpenAI (2025) — *Country-level ChatGPT traffic and signals data*.

---

## Licencia

MIT — Libre uso con atribución.
