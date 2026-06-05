# PROPUESTA 1: Cambio Climático y Emisiones de CO2 Global

---

## 1. TÍTULO Y DESCRIPCIÓN DEL DATASET

**Título:** Global CO2 Emissions and Climate Indicators Dataset

**Descripción:** Dataset integrador que combina múltiples fuentes de datos sobre emisiones de CO2 por país y año, junto con indicadores de temperatura global, para analizar la relación entre la actividad humana y el cambio climático desde 1950 hasta la actualidad.

**Fuentes:**
- Our World in Data - CO2 and Greenhouse Gas Emissions: https://github.com/owid/co2-data
- NASA GISS Surface Temperature Analysis (GISTEMP v4): https://data.giss.nasa.gov/gistemp/
- IRENA Renewable Energy Statistics: https://pxweb.irena.org/pxweb/en/IRENASTAT/

---

## 2. JUSTIFICACIÓN DE LA SELECCIÓN

He elegido este tema por los siguientes motivos:

**Personales:**
- Tema que me interesa personalmente: el cambio climático es uno de los desafíos más importantes de mi generación
- Coherencia con mi formación en Ciencia de Datos: permite aplicar técnicas de visualización avanzadas

**Profesionales:**
- Alta demanda de profesionales con habilidades de visualización de datos ambientales
- Sector en crecimiento: consultoras ambientales, agencias gubernamentales, ONGs

**Curiosidad personal:**
- Viví directamente los efectos del cambio climático en mi región (sequías, olas de calor)
- Quisiera entender mejor los datos detrás de la crisis climática

---

## 3. RELEVANCIA DEL CONJUNTO DE DATOS

### 3.1 Actualización

| Fuente | Última actualización | Cobertura temporal |
|--------|---------------------|-------------------|
| OWID CO2 Data | 2025 | 1950-2024 |
| NASA GISTEMP | Febrero 2026 | 1880-2025 |
| IRENA Energy | 2025 | 2000-2024 |

✅ **Datos muy actuales**: El dataset más reciente (Climate TRACE) tiene datos hasta 2025.

### 3.2 Importancia para colectivos concretos

- **Países en desarrollo**: Pueden ver comparativamente sus emisiones vs países ricos (principio de "responsabilidad común pero diferenciada")
- **Activistas climáticos**: Datos para advocacy basados en evidencia
- **Políticos**: Indicadores para seguimiento de Objetivos de Desarrollo Sostenible (ODS 13)
- **Investigadores**: Base para estudios científicos sobre cambio climático

### 3.3 Perspectiva de género

El dataset NO incluye variables de género explícitas directamente. Sin embargo, se puede enriquecer cruzando con:
- Datos de representación femenina en ministerios de medio ambiente (UNFCCC)
- Estudios sobre impacto de cambio climático en mujeres rurales

### 3.4 Connotación social

- **Educación ambiental**: Herramienta para sensibilizara la población
- **Justicia climática**: Visualiza la Inequality entre países ricos y pobres
- **Responsabilidad corporativa**: Empresas pueden usar datos para comparar su huella

---

## 4. COMPLEJIDAD DEL DATASET

### 4.1 Número de registros

| Dataset | Registros aproximados |
|---------|----------------------|
| OWID CO2 | ~40,000+ (200 países × 200 años) |
| NASA Temperature | ~145 años (serie temporal) |
| IRENA Energy | ~3,750 (150 países × 25 años) |

**Total estimado**: >50,000 registros

### 4.2 Variables disponibles

**Variables categóricas:**
- `country` - Nombre del país
- `iso_code` - Código ISO 3166-1
- `continent` - Continente
- `year` - Año (variable temporal)
- `energy_source` - Fuente de energía (en datos IRENA)

**Variables cuantitativas:**
- `annual_co2_emissions` - Emisiones anuales de CO2 (toneladas)
- `co2_per_capita` - Emisiones per cápita
- `cumulative_co2` - Emisiones acumuladas desde 1950
- `temperature_anomaly` - Anomalía de temperatura (°C)
- `renewable_energy_capacity` - Capacidad renovable (MW)
- `gdp` - PIB (USD)
- `population` - Población

**Tipos de datos:**
- ✅ Valores discretos (país, año)
- ✅ Valores continuos (emisiones, temperatura)
- ✅ Fechas (serie temporal 1950-2025)
- ✅ Valores lógicos (flags de datos disponibles)

### 4.3 Riqueza de tipología

| Tipo | Cantidad | Ejemplo |
|------|----------|---------|
| Categóricas | 5+ | país, continente, código ISO |
| Cuantitativas continuas | 10+ | emisiones, GDP, población |
| Temporales | 3+ | año, fecha, serie temporal |
| Calculadas | 5+ | CO2 per capita, intensidad emissions |

---

## 5. ORIGINALIDAD

### 5.1 ¿Por qué es diferente?

1. **Combinación única**: No es común ver un dashboard que combine:
   - Emisiones de CO2 por país
   - Temperatura global
   - Energía renovable por tecnología

2. **Datos muy recientes**: Climate TRACE tiene datos de 2025, más actual que la mayoría de visualizaciones existentes

3. **Cobertura global**: 200+ países con series temporales largas

### 5.2 Visualizaciones existentes

Las visualizaciones típicas de este tema son:
- Gráfico de líneas de emisiones por país (muy básico)
- Mapas coropléticos de emisiones (comunes en medios)
- Gráfico de espiral de temperatura (The Warming Stripe)

### 5.3 Mi propuesta de valor

**Propuesta original:**
- Combinar EMISIONES + TEMPERATURA + ENERGÍAS en un mismo dashboard
- Mostrar la CORRELACIÓN entre三者 (emisiones ↑ mientras temperatura ↑ mientras renovables ↑)
- Comparativa INTERACTIVA por país/región/tiempo
- Análisis de "brecha de emisiones" (qué país cumple vs qué debería cumplir)

### 5.4 Enriquecimiento propuesto

Crear nuevas métricas/indicadores:
- **Índice de Compromiso Climático (ICC)**: Emisiones acumuladas / PIB per cápita
- **Tasa de Decarbonización (TDD)**: % reducción de emisiones por década
- **Brecha de Temperatur (BT)**: Temperatura real vs modelo de optimistic/scenarios

---

## 6. PREGUNTAS DE INVESTIGACIÓN

He planteillado las siguientes preguntas que la visualización debe responder:

### Pregunta 1: Distribución Geográfica
**¿Cómo se distribuyen las emisiones de CO2 por país y región en 2024, y qué países/regiones son los principales emisores?**

- Mapa coroplético interactivo por país
- Ranking de top 20 países emisores
- Desglose por continente

### Pregunta 2: Evolución Temporal
**¿Cómo han evolucionado las emisiones de CO2 y la temperatura global desde 1950, y existe correlación entre ambas?**

- Serie temporal dual (emisiones + temperatura)
- Análisis de puntos de inflexión
- Tendencias por década

### Pregunta 3: Factores Explicativos
** ¿Qué factores (GDP, población, tipo de energía) están más correlacionados con las emisiones por país?**

- Scatter plot: emisiones vs GDP
- Heatmap de correlaciones
- Análisis por cluster de países

### Pregunta 4: Transición Energética
**¿Qué países han avanzado más en transición energética y cómo se compara su trayectoria?**

- Gráfico de barras apiladas: mix energético por país
- Evolución temporal de renovables
- Ranking de países "verdes"

---

## 7. DICCIONARIO DE VARIABLES

| Variable | Significado | Tipo | Hecho o Dimensión |
|----------|--------------|------|-------------------|
| `country` | Nombre oficial del país | Categórico | Hecho: país observado |
| `iso_code` | Código ISO 3166-1 de 3 letras | Categórico | Hecho: identificación |
| `year` | Año de observación | Temporal | Hecho: momento temporal |
| `annual_co2_emissions` | Emisiones de CO2 en ese año (toneladas) | Cuantitativo | Hecho: emisiones anuales |
| `co2_per_capita` | Emisiones por persona (toneladas/persona) | Cuantitativo | Dimensión: intensidad/emisiones por individuo |
| `cumulative_co2_emissions` | Emisiones acumuladas desde 1950 (toneladas) | Cuantitativo | Dimensión: histórico total |
| `temperature_anomaly` | Anomalía de temperatura vs período base (°C) | Cuantitativo | Hecho: temperatura medida |
| `gdp` | Producto Interno Bruto (USD) | Cuantitativo | Dimensión: actividad económica |
| `population` | Número de habitantes | Cuantitativo | Dimensión: tamaño demográfico |
| `energy_source` | Tipo de fuente energética | Categórico | Hecho: fuente de energía |
| `renewable_capacity_mw` | Capacidad renovable instalada (MW) | Cuantitativo | Hecho: capacidad instalada |

---

## 8. COHERENCIA GENERAL

| Criterio | Cumple | Explicación |
|----------|--------|-------------|
| Justificación clara | ✅ | Tema personal + profesional coherente con formación |
| Relevancia social | ✅ | Crisis climática, ODS 13, justicia climática |
| Perspectiva de género | ⚠️ | No directa, pero se puede enriquecer |
| Complejidad adecuada | ✅ | >50,000 registros, 10+ variables |
| Originalidad | ✅ | Combinación única de fuentes |
| Preguntas coherentes | ✅ | 4 preguntas conectadas con variables |

---

## 9. RESULTADOS ESPERADOS

Se espera obtener un dashboard interactivo con:

1. **Mapa global** de emisiones por país (2024)
2. **Serie temporal** de emisiones + temperatura superpuesta
3. **Gráfico de dispersión** de emisiones vs GDP por país
4. **Evolución de energías renovables** por país/región
5. **Filtros interactivos** por año, país, rango de emisiones

---

**Propuesta elaborada para:**-master UOC - Visualización de Datos
**Fecha:** 17 de abril de 2026