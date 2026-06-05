# Validación del Proyecto — IA y Recursos: La Huella Oculta

## Objetivo

Este documento describe qué se ha construido, qué debe contener cada pregunta de investigación,
y proporciona un script de verificación automática para validar que todo esté correcto
antes de la entrega final.

---

## 1. Resumen del Proyecto

**Visualización interactiva** que responde a la pregunta principal:
> ¿Cuál es el costo ambiental invisible de la inteligencia artificial?

A través de **3 dimensiones** (agua, energía, memoria) y **4 preguntas de investigación**,
se exploran los recursos que consume la IA: desde el agua para enfriar servidores
hasta la energía para entrenar modelos y la memoria que encarece los componentes.

### Dataset
- **3 archivos CSV**: `agua.csv`, `energia.csv`, `memoria.csv`
- **25+ variables** (10 categóricas, 18 cuantitativas, 4 temporales, 2 lógicas)
- **85+ registros** compilados de fuentes primarias (IEA, Google, Microsoft, Meta, Li et al., Epoch AI, TrendForce)

### Visualización
- **HTML autocontenido** con D3.js v7 (sin servidor, funciona desde GitHub Pages)
- **6 secciones** narrativas con scroll storytelling (incluye mapamundi IA)
- **12 gráficos interactivos** con tooltips, selectores y equivalencias dinámicas

---

## 2. Checklist por Pregunta de Investigación

### P1 — Agua: ¿Cómo ha evolucionado el consumo de agua?

| Requisito | Implementación | Archivo/Sección |
|-----------|---------------|-----------------|
| Datos Google, Microsoft, Meta 2020-2024 | Barras apiladas por empresa | `#chart-agua-barras` |
| Agua por consulta de IA (ml) | Barras GPT-3 → GPT-4 → GPT-4o | `#chart-agua-query` |
| Proyección global Li et al. | Barra de rango 2023 vs 2027 | `#chart-agua-global` |
| Tendencia creciente visible | Sí — todas las empresas suben | agua.csv |
| Tooltips con valores exactos | Sí — al hover en cada gráfico | JS: showTooltip() |
| Dato clave destacado | Highlight box azul | Sección P1 |

### P2 — Energía: ¿Cuál es la tendencia de consumo eléctrico?

| Requisito | Implementación | Archivo/Sección |
|-----------|---------------|-----------------|
| Serie histórica IEA 2015-2035 | Línea con área de proyección | `#chart-energia-linea` |
| Escenarios base vs lift-off | Selector interactivo | `#escenario-select` |
| Wh por modelo comparativo | Barras horizontales | `#chart-energia-wh` |
| Emisiones CO2 por empresa | Líneas múltiples Amazon/MS/Meta | `#chart-energia-co2` |
| Proyecciones claramente marcadas | Línea punteada + área sombreada | SVG: stroke-dasharray |
| Tooltips con valores exactos | Sí | JS: showTooltip() |
| Dato clave destacado | Highlight box naranja | Sección P2 |

### P3 — Memoria: ¿Por qué sube el precio de la memoria?

| Requisito | Implementación | Archivo/Sección |
|-----------|---------------|-----------------|
| Evolución precio DDR5 | Línea Q1 2024 → Q4 2026 | `#chart-memoria-ddr5` |
| Mercado HBM ($B) | Barras 2023-2026 | `#chart-memoria-hbm` |
| Costo entrenamiento modelos | Barras escala logarítmica | `#chart-memoria-training` |
| Proyecciones vs reales | Línea punteada en DDR5 | SVG: stroke-dasharray |
| Tooltips con valores exactos | Sí | JS: showTooltip() |
| Dato clave destacado | Highlight box azul | Sección P3 |

### P4 — Equivalencias: ¿Cómo se relacionan las dimensiones?

| Requisito | Implementación | Archivo/Sección |
|-----------|---------------|-----------------|
| Equivalencias interactivas | Selector 3 niveles + tarjetas | `#equiv-select` + `#equiv-grid` |
| Agua ↔ Energía ↔ Memoria | 3 tarjetas por nivel | `#equiv-grid` |
| Nivel 1: 1 consulta | 50-100ml, 0.3Wh, ~$0.0001 | equiv-grid |
| Nivel 2: 1 día ChatGPT | 25M L, 150MWh, 15 casas | equiv-grid |
| Nivel 3: 1 entrenamiento | 700KL, 1,300MWh, $12M→$1B | equiv-grid |
| Vista comparativa 3 dimensiones | Círculos concéntricos | `#chart-equivalencias-radar` |

### Requisitos Generales

| Requisito | Implementación |
|-----------|---------------|
| Scroll storytelling | 6 secciones con `min-height: 100vh` |
| Navegación por secciones | 7 dots laterales + barra progreso |
| Diseño responsivo | Media queries, viewBox SVG |
| Paleta colores consistente (vintage) | Sepia/Parchment (#f5f0e8) + Ink (#2c1810) + Rust (#c04000) + Gold (#b8963e) |
| Tipografía vintage | Playfair Display (títulos) + IBM Plex Mono (datos) + Source Sans 3 (cuerpo) |
| Mapamundi coroplético interactivo | 177 países con adopción IA, España destacada en oro |
| Tooltips en todos los gráficos | Position:fixed + transition |
| Animaciones al scroll | IntersectionObserver + CSS fadeInUp |
| Loading screen | Spinner mientras carga D3.js + TopoJSON |
| Fuentes citadas | Sección footer con 10+ fuentes |
| Limitaciones declaradas | Nota sobre datos estimados en footer |

---

## 3. Cobertura de Rúbrica (Parte II)

| Criterio | % | Cubierto en |
|----------|---|-------------|
| **Proceso** | 20% | `GUION_VIDEO.md` sección 1 (0:10-1:10) + `compilar_datos.py` |
| **Presentación** | 20% | `GUION_VIDEO.md` sección 4 (3:55-4:55) + index.html completo |
| **Dataset** | 15% | `GUION_VIDEO.md` sección 2 (1:10-1:55) + `datos/*.csv` |
| **Preguntas** | 20% | `GUION_VIDEO.md` sección 3 (1:55-3:55) + 4 secciones HTML |
| **Interactividad** | 15% | `GUION_VIDEO.md` sección 5 (4:55-5:40) + selectores + tooltips |
| **Reflexión** | 10% | `GUION_VIDEO.md` sección 6 (5:40-6:10) |

---

## 4. Script de Validación Automática

El script `validar_proyecto.py` verifica:

1. **Estructura de archivos** — que existan todos los archivos necesarios
2. **Integridad de CSVs** — columnas, tipos, valores clave
3. **HTML** — que existan todos los charts y secciones
4. **Preguntas** — que cada P1-P4 tenga sus elementos
5. **Rubric** — que el guión cubra los porcentajes

### Cómo ejecutarlo

```bash
cd "C:\Users\Victus\documentacion_master\Visualizacion de datos\proyecto_PET"
python validar_proyecto.py
```

Salida esperada: todos los checks en VERDE ✅

Si hay algún check en ROJO ❌, el script indica exactamente qué falta.
