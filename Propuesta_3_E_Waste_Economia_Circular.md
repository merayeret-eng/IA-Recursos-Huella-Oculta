# PROPUESTA 3: Residuos Electrónicos y Economía Circular

---

## 1. TÍTULO Y DESCRIPCIÓN DEL DATASET

**Título:** Global E-waste Generation and Circular Economy Metrics Dataset

**Descripción:** Dataset integrador que combina estadísticas de generación de residuos electrónicos (e-waste) por país con indicadores de economía circular, permitiendo visualizar el flujo global de-e waste y los progressos hacia una economía circular.

**Fuentes:**
- Global E-waste Statistics Partnership (GESP): https://globalewaste.org/map/
- Kaggle E-waste Statistics by Country 2015-2024: https://www.kaggle.com/datasets/maazshaikh05/e-waste-statistics-by-country-from-2015-to-2024
- Our World in Data - Electronic Waste Recycling Rate: https://ourworldindata.org/grapher/electronic-waste-recycling-rate
- Circularity Gap Report: https://www.circularity-gap.world/countries
- OECD Global Plastics Outlook: https://stats.oecd.org/Index.aspx?DataSetCode=PLASTIC_WASTE_5

---

## 2. JUSTIFICACIÓN DE LA SELECCIÓN

He elegido este tema por los siguientes motivos:

**Personales:**
- Tema de máxima actualidad: todosbotamos móviles, portátiles, tablets constantemente
- Relación directa con el tema de microplásticos del ejemplo (ambiente, contaminación)
- Quiero entender el "otro lado" del móvils después debotarlo

**Profesionales:**
- Sector en crecimiento: las empresas deben cumplir normativas de RAEE (Residuos de Aparatos Eléctricos y Electrónicos)
- Demanda de perfiles en gestión de residuos y economía circular
- Conexión con sostenibilidad corporativa

**Curiosidad personal:**
- Me sorprendió saber que solo se reciclaje ~17% del e-waste global
- España está muy por debajo de la media europea
- Hay tráfico ilegal de e-waste a países africanos (impacto social)

**Diferenciación del ejemplo de microplásticos:**
- Tema complementario pero diferente
- Mismos conceptos de "flujo" y "ciclo" pero aplicado a electrónicos
- También permite análisis geográfico y temporal

---

## 3. RELEVANCIA DEL CONJUNTO DE DATOS

### 3.1 Actualización

| Fuente | Última actualización | Cobertura temporal |
|--------|---------------------|-------------------|
| GESP / ITU | 2024 | 2010-2024 |
| Kaggle E-waste | 2025 | 2015-2024 |
| OWID Recycling Rate | 2024 | 2000-2023 |
| Circularity Gap Report | 2025 | 2020-2025 |

✅ **Datos muy actuales**: Kaggle tiene datos hasta 2024.

### 3.2 Importancia para colectivos concretos

- **Países en desarrollo**: Reciben e-waste ilegal de países ricos (Agbogbloshie, Ghana)
- **Trabajadores informales**: Reciclan e-waste en condiciones precarias
- **Industria tecnológica**: Deben cumplir normativas de reciclaje (Apple, Samsung, etc.)
- **Medio ambiente**: E-waste = plomo, mercurio, cadmio = contaminación

### 3.3 Perspectiva de género

El dataset NO incluye variables de género directamente. Sin embargo:
- Se puede cruzar con estudios cualitativos de UNEP sobre género en gestión de residuos
- Es un GAP de datos conocido (mismo problema que e-waste)
- Se podría mencionar como limitación y propuesta de mejora

### 3.4 Connotación social

- **ODS 12**: Producción y consumo responsables (Objetivo 12 de la ONU)
- **Economía circular**: Modelo económico alternativo al "usar y botar"
- **Justicia ambiental**: Tráfico ilegal de e-waste a países pobres
- **Derechos laborales**: Trabajadoresinformales en países en desarrollo

---

## 4. COMPLEJIDAD DEL DATASET

### 4.1 Número de registros

| Dataset | Registros aproximados |
|---------|----------------------|
| GESP | ~2,000 (190 países × 10+ años) |
| Kaggle E-waste | ~2,000 (200 países × 10 años) |
| OWID Recycling Rate | ~4,000 (200 países × 20 años) |
| Circularity Gap Report | ~50 países × 5 años |

**Total estimado**: >8,000 registros

### 4.2 Variables disponibles

**Variables categóricas:**
- `country` - Nombre del país
- `region` - Región geográfica
- `income_group` - Grupo de ingreso (Banco Mundial)
- `legislation` - Tipo de legislación de e-waste (sí/no)

**Variables cuantitativas:**
- `e_waste_generated_kg` - E-waste generado (kg per cápita)
- `e_waste_total_tonnes` - E-waste total generado (toneladas)
- `e_waste_collected` - E-waste recolectado formalmente (toneladas)
- `recycling_rate` - Tasa de reciclaje (%)
- `circularity_metric` - Índice de circularidad (%)
- `gdp_per_capita` - PIB per cápita (USD)
- `population` - Población

**Variables derivadas:**
- `treatment_gap` - Brecha entre generado y reciclado
- `informal_sector_estimate` - Estimación sector informal

**Otros tipos:**
- ✅ Valores continuos (toneladas, %)
- ✅ Valores discretos (país, año)
- ✅ Valores lógicos (legislación sí/no)
- ✅ Serie temporal

### 4.3 Riqueza de tipología

| Tipo | Cantidad | Ejemplo |
|------|----------|---------|
| Categóricas | 5+ | país, región, grupo ingreso |
| Cuantitativas continuas | 8+ | toneladas, kg/cápita, % |
| De tiempo | 1+ | año |
| Calculadas | 3+ | brecha tratamiento, gap |

---

## 5. ORIGINALIDAD

### 5.1 ¿Por qué es diferente?

1. **Tema emergente**: La economía circular es tendencia 2024-2025 post-pandemia
2. **Poca visualización**: Menos común que cambio climático o COVID
3. **Contexto español/europeo**: España tiene normativa específica RAEE
4. **Datos nuevos**: Dataset Kaggle 2015-2024 muy reciente

### 5.2 Visualizaciones existentes

Las visualizaciones típicas de e-waste son:
- Mapas de generación por país (Global E-waste Monitor)
- Gráficos circulares de destino final (reciclado vsbotado vs incinerado)
- Ranking de países por tasa de reciclaje

### 5.3 Mi propuesta de valor

**Propuesta original:**
- **Combinar** e-waste + circularidad en un mismo dashboard
- **Análisis de la "brecha"**: cuánto se genera vs cuánto se recicla
- **Comparativa España vs Europa**: situar a España en el contexto europeo
- **Análisis de predictores**: qué factores influyen en la tasa de reciclaje (GDP, legislación, educación)
- **Flujo Sankey**: visualizar el flujo de e-waste desde generación hasta destino final

### 5.4 Enriquecimiento propuesto

Crear nuevas métricas/indicadores:
- **Índice de E-waste Responsibility (IER)**: Generación per cápita × PIB per cápita
- **Brecha de Tratamiento (BT)**: Generado - Recolectado - Reciclado
- **Score de Circularidad Compuesto (SCC)**: Media de recycling rate + circularity metric

---

## 6. PREGUNTAS DE INVESTIGACIÓN

### Pregunta 1: Distribución Geográfica
**¿Cómo se distribuye la generación de e-waste por país y región, y cuáles son los principales países generadores?**

- Mapa coroplético interactivo de e-waste per cápita
- Ranking top 20 países generadores
- Desglose por continente y grupo de ingreso

### Pregunta 2: Brecha de Reciclaje
**¿Cuál es la diferencia entre el e-waste generado y el efectivamente reciclado, y cómo varía por región?**

- Gráfico de barras: generado vs reciclado por país
- Mapa de "treatment gap" (brecha de tratamiento)
- Evolución temporal de la brecha

### Pregunta 3: Factores de Influencia
**¿Qué factores (legislación, GDP, educación) están más relacionados con mejores tasas de reciclaje?**

- Scatter plot: GDP per cápita vs tasa reciclaje
- Comparativa países con/sin legislación RAEE
- Heatmap de correlaciones

### Pregunta 4: Progreso hacia Economía Circular
**¿Qué países avanzan más hacia una economía circular según el Circularity Gap Report?**

- Ranking de países por índice de circularidad
- Evolución temporal del índice 2020-2025
- Comparativa por región y grupo de ingreso

---

## 7. DICCIONARIO DE VARIABLES

| Variable | Significado | Tipo | Hecho o Dimensión |
|----------|--------------|------|-------------------|
| `country` | Nombre del país | Categórico | Hecho: país observado |
| `year` | Año de observación | Temporal | Hecho: momento temporal |
| `e_waste_generated_kg_capita` | E-waste generado por persona (kg/persona/año) | Cuantitativo | Hecho: generación per cápita |
| `e_waste_total_tonnes` | E-waste total generado (toneladas) | Cuantitativo | Hecho: generación total |
| `e_waste_collected_formally` | E-waste recolectado formalmente (toneladas) | Cuantitativo | Hecho: recolección formal |
| `e_waste_recycled_tonnes` | E-waste reciclado (toneladas) | Cuantitativo | Hecho: reciclaje realizado |
| `recycling_rate_pct` | Porcentaje de e-waste reciclado (%) | Cuantitativo | Dimensión: eficiencia reciclaje |
| `circularity_metric_pct` | Índice de circularidad del país (%) | Cuantitativo | Dimensión: economía circular |
| `has_legislation` | Sí/No tiene legislación RAEE | Lógico | Dimensión: marco legal |
| `gdp_per_capita` | PIB per cápita (USD) | Cuantitativo | Dimensión: nivel desarrollo |
| `population` | Población total | Cuantitativo | Dimensión: tamaño demográfico |
| `treatment_gap` | Brecha entre generado y reciclado (toneladas) | Calculado | Dimensión: problema/no resuelto |
| `income_group` | Grupo de ingreso (World Bank) | Categórico | Dimensión: clasificación económica |

---

## 8. COHERENCIA GENERAL

| Criterio | Cumple | Explicación |
|----------|--------|-------------|
| Justificación clara | ✅ | Tema personal relevante + coherencia profesional |
| Relevancia social | ✅ | ODS 12, economía circular, justicia ambiental |
| Perspectiva de género | ⚠️ | No directa, pero se menciona como limitación |
| Complejidad adecuada | ✅ | >8,000 registros, 13+ variables |
| Originalidad | ✅ | Tema emergente, pocos usado en visualizaciones |
| Preguntas coherentes | ✅ | 4 preguntas conectadas con variables |

---

## 9. RESULTADOS ESPERADOS

Se espera obtener un dashboard interactivo con:

1. **Mapa global** de generación de e-waste per cápita
2. **Gráfico de barras** de brecha tratamiento (generado vs reciclado)
3. **Scatter plot** de GDP vs tasa reciclaje con regresión
4. **Ranking de países** por índice de circularidad
5. **Serie temporal** de evolución e-waste y recycling rate
6. **Filtros interactivos** por año, país, región, legislación

---

## 10. NOTA SOBRE LIMITACIONES

- **Perspectiva de género**: Esta es una limitación del dataset. Se podría enriquecer cruzando con estudios de UNEP/ILO sobre género en gestión de residuos.
- **Datos de informalidad**: El sector informal es difícil de cuantificar. Se incluiría como estimación.

---

**Esta propuesta destaca por:**
- ✅ Tema emergente y relevante (economía circular tendencia 2025)
- ✅ Conexión con ejemplo de microplásticos (contaminación)
- ✅ Posibilidad de análisis geográfico y temporal rico
- ✅ Datos muy actuales (2015-2024)

---

**Propuesta elaborada para:**
- Master UOC - Visualización de Datos
**Fecha:** 17 de abril de 2026