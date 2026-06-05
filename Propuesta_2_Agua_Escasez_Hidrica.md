# PROPUESTA 2: Agua y Escasez Hídrica Global

---

## 1. TÍTULO Y DESCRIPCIÓN DEL DATASET

**Título:** Global Water Scarcity and Gender Indicators Dataset

**Descripción:** Dataset integrador que combina estadísticas de agua dulce por país con indicadores de género (recolección de agua, acceso a agua potable), permitiendo visualizar la Inequality hídrica global con perspectiva de género.

**Fuentes:**
- AQUASTAT (FAO): https://www.fao.org/land-water/databases-and-software/aquastat/en/
- LivWell: Women's Well-being Database (Zenodo): https://zenodo.org/records/7277104
- World Bank Water Development Indicators: https://data.worldbank.org/indicator/ER.H2O.INTR.PC

---

## 2. JUSTIFICACIÓN DE LA SELECCIÓN

He elegido este tema por los siguientes motivos:

**Personales:**
- Interés en temas de justicia social y desigualdad
- Vivencias personales en países con estrés hídrico durante viajes

**Profesionales:**
- Sector agua es estratégico: cambio climático = más escasez
- Permisos de trabajo ambiental en España (Required educativo)

**Curiosidad/perspectiva de género:**
- Descubrí que NO existen muchos datasets con perspectiva de género
- Es un GAP de datos conocido → oportunidad
- Las mujeres y niñas son las principales afectadas en países en desarrollo

**Diferenciación:**
- Dataset de microplásticos que propuse el compañero → tema alternativo
- Este tema tiene perspectiva de género explícita → más original

---

## 3. RELEVANCIA DEL CONJUNTO DE DATOS

### 3.1 Actualización

| Fuente | Última actualización | Cobertura temporal |
|--------|---------------------|-------------------|
| FAO AQUASTAT | 2024-2025 | 1960-2022 |
| LivWell | 2023 | 2000-2022 |
| World Bank WDI | 2024 | 1960-2023 |

✅ **Datos recientes**: Fuentes actualizadas 2023-2025.

### 3.2 Importancia para colectivos concretos

- **Mujeres rurales (países en desarrollo)**:她们 recogen agua = horas dedicadas
- **Niñas**: Novan a escuela por recogido agua
- **Refugiados climáticos**: Migración por escasez de agua
- **Cooperación al desarrollo**: ONGs y agencias de难民

### 3.3 Perspectiva de género ✅ EXPLÍCITA

| Variable de género | Disponible | Descripción |
|-------------------|------------|-------------|
| `HH_women_time_water_mean` | ✅ LivWell | Tiempo moyen de recogida de agua por mujeres |
| `HH_women_water_high_p` | ✅ LivWell | % hogares con acceso de calidad por mujeres |
| `women_management` | ✅ AQUASTAT (nuevo) | % tierras irrigation gestionadas por mujeres |

✅ **Esta es la UNICA propuesta con perspectiva de género directa**.

### 3.4 Connotación social

- **ODS 6**: Agua limpia y saneamiento (Objetivo 6 de la ONU)
- **Derecho humano al agua**: Según la ONU, es un derecho humano fundamental
- **Desigualdad estructural**: Las mujeres dedican 4+ horas/día a recogido agua en algunos países

---

## 4. COMPLEJIDAD DEL DATASET

### 4.1 Número de registros

| Dataset | Registros aproximados |
|---------|----------------------|
| FAO AQUASTAT | ~10,000 (200 países × 50 variables) |
| LivWell | ~2,800 (52 países × 50+ indicadores) |
| World Bank WDI | ~8,000 (200 países × 40 años) |

**Total estimado**: >20,000 registros

### 4.2 Variables disponibles

**Variables categóricas:**
- `country` - Nombre del país
- `region` - Región geográfica (África, Asia, etc.)
- `water_stress_category` - Categoría de estrés hídrico

**Variables cuantitativas:**
- `renewable_water_per_capita` - Agua renovable por persona (m³/año)
- `water_withdrawals` - Extracción de agua dulce (km³/año)
- `water_stress_index` - Índice de estrés hídrico (%)
- `agriculture_withdrawal_pct` - % agua para agricultura
- `industry_withdrawal_pct` - % agua para industria
- `domestic_withdrawal_pct` - % agua para uso doméstico
- `basic_water_access_pct` - % acceso a agua potable básica

**Variables de género:**
- `women_time_to_water` - Tiempo medio mujeres dedicado a recoger agua (horas)
- `women_water_quality_perception` - Percepción de calidad por mujeres
- `women_land_management_pct` - % gestión de tierras de irrigation por mujeres

**Otros tipos:**
- ✅ Valores lógicos (flags de acceso)
- ✅ Valores discretos (categorías de estrés)
- ✅ Fechas (serie temporal)

### 4.3 Riqueza de tipología

| Tipo | Cantidad | Ejemplo |
|------|----------|---------|
| Categóricas | 5+ | país, región, categoría estrés |
| Cuantitativas continuas | 15+ | m³, %, km³ |
| De género | 3+ | tiempo, gestión, percepción |
| Temporales | 2+ | año, serie temporal |

---

## 5. ORIGINALIDAD

### 5.1 ¿Por qué es diferente?

1. **Perspectiva de género explícita**: La mayoría de visualizaciones de agua NO incluyen género
2. **Combinación única**: Agua + Género + Datos espaciales
3. **Dataset poco usado**: LivWell y datos de género water son muy poco conocidos

### 5.2 Visualizaciones existentes

Las visualizaciones típicas de agua son:
- Mapas coropléticos de estrés hídrico (WRI, World Bank)
- Gráficos de barras depaíses con escasez (varios medios)
- Dashboard SDG 6 de la ONU

### 5.3 Mi propuesta de valor

**Propuesta original:**
- **Primera visualización** que combina agua + género + cambio climático
- **Histoires invisibilisées**: las mujeres que recogen agua
- **Comparativa regional** confilter de género
- **Análisis de brechas**: países con mayor desigualdad de género en acceso al agua

### 5.4 Enriquecimiento propuesto

Crear nuevas métricas/indicadores:
- **Índice de Desigualdad Hídrica de Género (IDHG)**: Tiempo mujeres / Tiempo hombres
- **Brecha de Acceso (BA)**: Acceso agua urbana - Acceso agua rural
- **Índice de Vulnerabilidad Hídrica (IVH)**: Combinación de estrés + población + género

---

## 6. PREGUNTAS DE INVESTIGACIÓN

### Pregunta 1: Distribución Geográfica
**¿Cómo se distribuye el estrés hídrico por región y país, y cuáles son las zonas más vulnerables?**

- Mapa coroplético interactivo de estrés hídrico por país
- Ranking de top 20 países con mayor escasez
- Comparativa por continente

### Pregunta 2: Desigualdad de Género
**¿Quién recoge el agua en los países con estrés hídrico, y cuántas horas dedican las mujeres y niñas?**

- Barras horizontales: tiempo de recogida por género y país
- Mapa de países donde mujeres recoctionan agua
- Comparativa: mujeres urbanas vs rurales

### Pregunta 3: Relación con Desarrollo
**¿Existe correlación entre el nivel de desarrollo económico (GDP per cápita) y el acceso al agua?**

- Scatter plot: GDP per cápita vs acceso agua básica
- Análisis por clusters de países (desarrollados/en desarrollo)
- Tendencias por década

### Pregunta 4: Tendencias Temporales
**¿Ha mejorado el acceso al agua potable desde 2000, y qué países han avanzado más?**

- Serie temporal de acceso a agua por región
- Evolución del estrés hídrico 2000-2023
- Ranking de países con mayor progreso

---

## 7. DICCIONARIO DE VARIABLES

| Variable | Significado | Tipo | Hecho o Dimensión |
|----------|--------------|------|-------------------|
| `country` | Nombre del país | Categórico | Hecho: país observado |
| `year` | Año de observación | Temporal | Hecho: momento temporal |
| `renewable_water_per_capita` | Agua renovable por persona (m³/año) | Cuantitativo | Hecho: recursos hídricos |
| `water_withdrawal_total` | Extracción total de agua (km³/año) | Cuantitativo | Hecho: agua usada |
| `water_stress_index` | % recursos renovables consumidos | Cuantitativo | Dimensión: presión sobre recursos |
| `agriculture_withdrawal_pct` | % agua para agricultura | Cuantitativo | Dimensión: sector uso |
| `industry_withdrawal_pct` | % agua para industria | Cuantitativo | Dimensión: sector uso |
| `domestic_withdrawal_pct` | % agua uso doméstico | Cuantitativo | Dimensión: sector uso |
| `basic_water_access_pct` | % población con agua potable básica | Cuantitativo | Hecho: acceso servicios |
| `women_time_to_water` | Tiempo moyen mujeres recoger agua (horas/día) | Cuantitativo | Hecho: carga de género |
| `women_water_access_pct` | % hogares encabezados por mujeres con agua calidad | Cuantitativo | Dimensión: igualdadAccess |
| `rural_access_pct` | % acceso agua zona rural | Cuantitativo | Dimensión: brecha urbano-rural |
| `population_total` | Población total | Cuantitativo | Dimensión: tamaño demográfico |

---

## 8. COHERENCIA GENERAL

| Criterio | Cumple | Explicación |
|----------|--------|-------------|
| Justificación clara | ✅ | Tema personal de justicia social + perspectiva de género |
| Relevancia social | ✅ | ODS 6, derecho humano al agua, desigualdad de género |
| Perspectiva de género | ✅ | Variables explícitas de género en dataset LivWell |
| Complejidad adecuada | ✅ | >20,000 registros, 13+ variables |
| Originalidad | ✅ | Dataset género+agua = muy poco usado |
| Preguntas coherentes | ✅ | 4 preguntas conectadas con variables |

---

## 9. RESULTADOS ESPERADOS

Se espera obtener un dashboard interactivo con:

1. **Mapa global** de estrés hídrico con filtros por género
2. **Gráfico de barras** de tiempo de recogida de agua por género
3. **Serie temporal** de acceso a agua potable por región
4. **Scatter plot** de GDP vs acceso a agua con análisis de género
5. **Comparativas** rural vs urbano, hombre vs mujer

---

**Esta propuesta destaca por:**
- ✅ SER EL ÚNICO tema con perspectiva de género
- ✅ Relevancia social maxima (ODS 6)
- ✅ Originalidad (dataset casi inexplorado en visualizaciones)

---

**Propuesta elaborada para:**
- Master UOC - Visualización de Datos
**Fecha:** 17 de abril de 2026