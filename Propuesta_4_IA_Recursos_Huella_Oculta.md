# PROPUESTA 4: IA y Recursos - La Huella Oculta de la Revolución de la Inteligencia Artificial

---

## 1. TÍTULO Y DESCRIPCIÓN DEL DATASET

**Título:** AI Resources Footprint Dataset: Water, Energy, and Memory Consumption

**Descripción:** Dataset integrador que combina por primera vez tres dimensiones del impacto de la IA en recursos naturales y hardware: (1) consumo de agua de data centers, (2) consumo energético de modelos de IA, y (3) escasez de memoria RAM/HBM. El dataset permite visualizar cómo la revolución de la IA está afectando a recursos hídricos, energéticos y de hardware a nivel global.

**Fuentes principales:**
- IEA Energy and AI Report (2025): https://www.iea.org/reports/energy-and-ai
- Microsoft/Google/Meta Environmental Reports (2024-2025)
- TrendForce Memory Market Reports: https://www.trendforce.com
- estudios académicos: Díaz-Marín et al. (2024), Shehabi et al. (2024)
- Global E-waste Statistics Partnership (para contexto de hardware)

---

## 2. JUSTIFICACIÓN DE LA SELECCIÓN

### 2.1 Motivos Personales

- **Interés personal en IA**: Como estudiante de ciencia de datos, uso herramientas de IA a diario (ChatGPT, Claude, Copilot)
- **Paradoja identificada**: Uso IA para "ser más eficiente" pero la IA consume recursos masivos
- **Curiosidad**: Quería entender si los titulares de prensa son ciertos ("IA secará los data centers", "RAM 400% más cara")
- **Experiencia propia**: He notado el aumento de precios de componentes GPU/RAM en 2024-2025

### 2.2 Motivos Profesionales

- **Sector en crecimiento**: La IA y sus impactos ambientales es un área de consultoría emergente
- **Demanda de perfiles**: Las empresas buscan profesionales que entiendan la sostenibilidad de la IA
- **Conexión con el mercado laboral**: Conocimiento aplicable a roles de Data Science + Sustainability

### 2.3 Diferenciación

Esta propuesta es radicalmente diferente a las anteriores porque:
- **No existe un dataset similar**: Es la PRIMERA vez que se combinan estas tres dimensiones
- **Tema de máxima actualidad**: Los datos más recientes son de 2025-2026
- **Alta relevancia mediática**: Temas candentes en prensa y redes sociales

---

## 3. RELEVANCIA DEL CONJUNTO DE DATOS

### 3.1 Actualización de los Datos

| Fuente | Última actualización | Cobertura temporal |
|--------|---------------------|-------------------|
| IEA Energy and AI | Abril 2025 | 2024-2030 (proyecciones) |
| Microsoft ESG Report | Mayo 2025 | 2022-2024 |
| Google Environmental | Junio 2025 | 2022-2024 |
| TrendForce Memory | Marzo 2026 | 2023-2026 |
| Estudios académicos | 2024-2025 | varies |

✅ **Datos MUY actuales**: Los informes de memoria son de marzo 2026, IEA abril 2025.

### 3.2 Importancia para Colectivos Concretos

| Colectivo | Por qué le importa |
|-----------|-------------------|
| **Entidades gubernamentales** | Planificación energética, políticas de data centers |
| **Empresas de IA (OpenAI, Anthropic, Google)** | Presión para ser sostenibles, reporting ESG |
| **ONGs ambientales** | Advocacy, lobby por regulación |
| **Inversores** | Evaluación de riesgos ASG en empresas de IA |
| **Usuarios individuales** | Conciencia sobre uso responsable de IA |
| **Industria de semiconductores** | Planificación de capacidad, precios |

### 3.3 Perspectiva de Género

El dataset NO incluye variables de género directamente. Sin embargo:
- Se puede discutir el impacto diferenciado en países del Sur Global
- La mano de obra en mines de tierras raras (fundamental para chips) tiene perspectiva de género
- Es una limitación reconocida que podría enriquecer estudios futuros

### 3.4 Connotación Social

| Aspecto | Relevancia Social |
|---------|------------------|
| **Agua** | Data centers en regiones con estrés hídrico = conflicto con comunidades locales |
| **Energía** | Aumento de demanda eléctrica = más centrales = emisiones |
| **Hardware** | Escasez de chips = aumento de precios = tecnología menos accesible |
| **Desigualdad** | Países ricos tienen data centers, países pobres sufren consecuencias |

---

## 4. COMPLEJIDAD DEL DATASET

### 4.1 Número de Registros

| Dataset | Registros aproximados |
|---------|----------------------|
| IEA Energy Data | ~500 (países × escenarios × años) |
| Memory Prices (TrendForce) | ~300 (tipos × meses) |
| Data Center Water (empresas) | ~50 (empresas × años) |
| Model Energy (estudios) | ~30 (modelos × estimaciones) |
| Hyperscaler Consumption | ~20 (empresas × años) |

**Total estimado**: >900 registros (compacto pero rico en variables)

### 4.2 Variables Disponibles

**Variables Categóricas:**
- `company` - Empresa (Microsoft, Google, Amazon, Meta, NVIDIA, etc.)
- `region` - Región geográfica
- `model_name` - Nombre del modelo de IA
- `memory_type` - Tipo de memoria (DDR5, HBM3, HBM3E, HBM4)
- `scenario` - Escenario de proyección (Base, Lift-Off, High Efficiency)

**Variables Cuantitativas - AGUA:**
- `water_withdrawn_billions_L` - Agua total extraída (miles de millones de litros)
- `water_consumed_billions_L` - Agua consumida (evaporada)
- `WUE` - Water Usage Effectiveness (L/kWh)
- `water_per_training_millions_L` - Litros para entrenar modelo

**Variables Cuantitativas - ENERGÍA:**
- `energy_consumption_TWh` - Consumo energético (TWh/año)
- `energy_per_query_Wh` - Energía por consulta (Wh)
- `CO2_emissions_Mt` - Emisiones de CO2 (megatoneladas)
- `electricity_demand_PCT` - Porcentaje de electricidad global

**Variables Cuantitativas - MEMORIA:**
- `DRAM_price_USD` - Precio DRAM ($/módulo)
- `price_change_pct` - Cambio porcentual de precio
- `HBM_market_size_B` - Tamaño mercado HBM (miles de millones $)
- `supply_demand_gap_pct` - Brecha oferta-demanda (%)

**Variables Temporales:**
- `year` - Año (2015-2030)
- `quarter` - Trimestre (para precios)
- `month` - Mes (para precios)

### 4.3 Riqueza de Tipología

| Tipo | Cantidad | Ejemplo |
|------|----------|---------|
| Categóricas | 10+ | empresa, modelo, región, tipo memoria |
| Cuantitativas continuas | 15+ | TWh, $, %, Litros |
| Temporales | 3+ | año, trimestre, mes |
| Calculadas | 5+ | brechas, índices compuestos |

---

## 5. ORIGINALIDAD

### 5.1 ¿Por qué es radicalmente diferente?

1. **NUNCA se ha visualizado así**: No existe un dashboard que combine agua + energía + memoria de IA
2. **Datos de 2025-2026**: Más reciente que cualquier dataset público
3. **Tres historias en una**: Muestra la "triada" del impacto de la IA
4. **Relevancia mediática extrema**: Todo el mundo habla de esto

### 5.2 Visualizaciones Existentes

Las visualizaciones típicas de estos temas son:
- **单独**: Gráficos de consumo energético de data centers (IEA)
- **单独**: Mapas de estrés hídrico de data centers (Díaz-Marín)
- **单独**: Gráficos de precios de memoria (TrendForce - privados)
- **NO existe**: Combinación de los tres

### 5.3 Mi Propuesta de Valor

**Propuesta única:**
- **Dashboard tridimensional**: Agua + Energía + Memoria en una misma visualización
- **Comparativa de impacto**: Cuál recurso es más afectado por la IA
- **Línea temporal**: Evolución 2020-2030 de los tres recursos
- **Análisis de correlación**: ¿Suben los precios de memoria cuando aumenta el consumo energético?
- **Equivalencias visuales**: 1 entrenamiento = X piscinas = X hogares = Y kg CO2

### 5.4 Enriquecimiento Propuesto

Crear nuevos indicadores/índices:
- **Índice de Huella IA (IHIA)**: Normalización combinada de agua + energía + memoria
- **Costo por Query Compuesto**: Energía + agua amortizada por consulta
- **Brecha de Sostenibilidad (BS)**: Diferencia entre crecimiento IA y mejoras en eficiencia

---

## 6. PREGUNTAS DE INVESTIGACIÓN

### Pregunta 1: Distribución Geográfica del Impacto
**¿Dónde están ubicados los principales data centers de IA y cómo varía su impacto hídrico y energético por región?**

- Mapa interactivo: Ubicación de data centers con consumo de agua/energía
- Comparativa por país/región
- Identificación de regiones con estrés hídrico + data centers

### Pregunta 2: Evolución Temporal del Impacto
**¿Cómo ha evolucionado el consumo de agua, energía y los precios de memoria desde 2020, y cuáles son las proyecciones para 2030?**

- Serie temporal múltiple: Agua, Energía, Memoria 2020-2030
- Escenarios IEA (Base, Lift-Off, High Efficiency)
- Identificación de puntos de inflexión (lanzamiento ChatGPT, etc.)

### Pregunta 3: Relación entre Crecimiento de IA y Escasez de Recursos
**¿Existe correlación entre el crecimiento del uso de IA (usuarios, queries) y la escasez de recursos (agua, memoria, energía)?**

- Scatter plots: Crecimiento IA vs incremento de precios memoria
- Análisis de correlación: Variables que más influyen en precios
- Comparativa: Entrenamiento vs inferencia

### Pregunta 4: Equivalencias y Contexto
**¿Cuánta agua, energía y dinero consume realmente la IA comparada con actividades cotidianas?**

- Visualizaciones de equivalencias:
  - 1 entrenamiento GPT-4 = ~3 piscinas olímpicas = 460 hogares/año
  - 1 consulta ChatGPT = ~500ml agua = 4g CO2
  - Precio DDR5 2024-2026 = +400% (de $80 a $400)
- Comparativas visuales impactantes

---

## 7. DICCIONARIO DE VARIABLES

| Variable | Significado | Tipo | Hecho o Dimensión |
|----------|-------------|------|-------------------|
| `company` | Nombre de la empresa de IA/cloud | Categórico | Hecho: actor principal |
| `region` | Ubicación geográfica del data center | Categórico | Hecho: ubicación |
| `year` | Año de observación | Temporal | Hecho: momento temporal |
| `water_withdrawn_billions_L` | Agua total extraída (miles de millones litros) | Cuantitativo | Hecho: consumo hídrico |
| `water_consumed_billions_L` | Agua consumida/evaporada (miles de millones litros) | Cuantitativo | Hecho: consumo real |
| `WUE_L_per_kWh` | Water Usage Effectiveness (L/kWh) | Cuantitativo | Dimensión: eficiencia hídrica |
| `energy_consumption_TWh` | Consumo energético (Teravatios-hora/año) | Cuantitativo | Hecho: demanda eléctrica |
| `energy_per_query_Wh` | Energía por consulta de IA (Vatios-hora) | Cuantitativo | Dimensión: eficiencia por uso |
| `CO2_emissions_Mt` | Emisiones de CO2 (Megatoneladas) | Cuantitativo | Dimensión: impacto climático |
| `electricity_demand_pct_global` | % electricidad global consumida por data centers | Cuantitativo | Dimensión: escala relativa |
| `model_name` | Nombre del modelo de IA | Categórico | Hecho: modelo específico |
| `training_water_millions_L` | Agua para entrenar modelo (millones litros) | Cuantitativo | Hecho: entrenamiento específico |
| `DRAM_price_USD` | Precio módulo DRAM server ($) | Cuantitativo | Hecho: costo hardware |
| `HBM_price_change_pct` | Cambio porcentual precio HBM | Cuantitativo | Dimensión: variación mercado |
| `HBM_market_size_B` | Tamaño mercado HBM (miles millones $) | Cuantitativo | Hecho: tamaño mercado |
| `memory_supply_gap_pct` | Brecha oferta-demanda memoria (%) | Cuantitativo | Dimensión: escasez |
| `GPU_demand_units` | Demanda de GPUs para IA (unidades) | Cuantitativo | Hecho: demanda hardware |
| `scenario` | Escenario de proyección IEA | Categórico | Dimensión: proyección |
| `PUE` | Power Usage Effectiveness | Cuantitativo | Dimensión: eficiencia energética |

---

## 8. HALLAZGOS CLAVE (DATOS PARA VISUALIZACIÓN)

### 8.1 Agua: El Recurso Invisible

| Métrica | Valor | Fuente |
|---------|-------|--------|
| Agua para entrenar GPT-3 | ~700,000 litros | Díaz-Marín 2024 |
| Agua para entrenar GPT-4 | 5-10 millones litros | Estimación |
| Agua数据中心 Microsoft/año | 20.9 mil millones litros | Microsoft ESG 2024 |
| Agua数据中心 Google/año | 25.4 mil millones litros | Google Env 2024 |
| Proyección 2027 global | 4.2-6.6 mil millones m³ | Shehabi 2024 |

### 8.2 Energía: La Demanda Exponencial

| Métrica | Valor | Fuente |
|---------|-------|--------|
| Consumo global data centers 2024 | 415 TWh | IEA 2025 |
| Proyección 2030 (escenario base) | 945 TWh | IEA 2025 |
| % electricidad global 2030 | 3-4.4% | IEA 2025 |
| Energía por consulta ChatGPT | 0.34 Wh | OpenAI 2025 |
| Equivalente entrenamiento GPT-3 | 120 hogares/año | UC Riverside |

### 8.3 Memoria: La Escasez Estructural

| Métrica | Valor | Fuente |
|---------|-------|--------|
| Incremento precios DDR5 2024-2026 | +200-400% | TrendForce 2026 |
| Tamaño mercado HBM 2024 | $17-18 mil millones | TrendForce |
| Tamaño mercado HBM 2026 | $54-55 mil millones | BofA |
| Brecha oferta-demanda HBM 2025 | -36% | Estimación |
| Duración estimada escasez | 4-5 años | SK Hynix Chairman |

---

## 9. COHERENCIA GENERAL

| Criterio | Cumple | Explicación |
|----------|--------|-------------|
| Justificación clara | ✅ | Tema personal + profesional muy bien fundamentado |
| Relevancia social | ✅ | ODS 7 (energía limpia), ODS 12 (consumo responsable), impacto económico |
| Perspectiva de género | ⚠️ | No directa, pero se puede discutir impacto en países en desarrollo |
| Complejidad adecuada | ✅ | ~900 registros, 20+ variables de múltiples tipos |
| Originalidad | ✅ | NO existe dataset similar que combine los tres recursos |
| Preguntas coherentes | ✅ | 4 preguntas conectadas con todas las variables |
| Datos muy actuales | ✅ | Marzo 2026 para memoria, Abril 2025 para energía |

---

## 10. RESULTADOS ESPERADOS

Se espera obtener un dashboard interactivo con:

1. **Mapa global** de data centers con consumo de agua y energía
2. **Serie temporal** de agua + energía + precios memoria 2020-2030
3. **Gráfico de equivalencias** impactante (piscinas, hogares, CO2)
4. **Análisis de correlación** entre crecimiento IA y escasez recursos
5. **Panel de control** con KPIs de las tres dimensiones
6. **Filtros interactivos** por empresa, año, región, escenario

---

## 11. VENTAJAS COMPETITIVAS FRENTE A OTRAS PROPUESTAS

| Aspecto | Propuesta 1 (Clima) | Propuesta 2 (Agua) | Propuesta 3 (E-waste) | **Propuesta 4 (IA+Recursos)** |
|---------|---------------------|---------------------|----------------------|------------------------------|
| Actualidad datos | 2024 | 2024 | 2024 | **2025-2026** |
| Originalidad | Media | Alta | Media | **MUY ALTA** |
| Cobertura temática | Tradicional | Género | Emergente | **TRIPLE + Candente** |
| Interés mediático | Alto | Medio | Medio | **EXTRIMO** |
| Complejidad | Alta | Alta | Media | **ALTA** |

---

## 12. LIMITACIONES RECONOCIDAS

1. **Datos de memoria son de pago**: TrendForce requiere suscripción ($15K-25K/año)
2. **Estimaciones vs datos reales**: Muchas cifras son estimaciones (agua por modelo)
3. **Perspectiva de género**: No incluida directamente
4. **Sesgo de fuentes**: Empresas tienden a reportar solo energía limpia contratada

---

**Esta propuesta destaca por:**
- ✅ Tema RADICALMENTE actual (datos de marzo 2026)
- ✅ NUNCA antes visualizado así (tres recursos combinados)
- ✅ Interés mediático EXTREMO (todo el mundo habla de esto)
- ✅ Datos verificables de fuentes reconocidas (IEA, empresas, TrendForce)
- ✅ Potencial para visualización muy impactante

---

**Propuesta elaborada para:**
- Master UOC - Visualización de Datos
**Fecha:** 17 de abril de 2026

---

## ANEXO: Fuentes Principales con Enlaces

### Agua + Data Centers
- IEA Energy and AI (2025): https://www.iea.org/reports/energy-and-ai
- Microsoft ESG Report (2025): https://www.microsoft.com/esg
- Google Environmental Report (2025): https://blog.google/outreach-initiatives/sustainability/environmental-report-2025
- Díaz-Marín et al. (2024): Estudio académico sobre agua y data centers

### Energía + IA
- IEA Global Energy Review 2025: https://www.iea.org/reports/global-energy-review-2025
- McKinsey - AI Power Demand: https://www.mckinsey.com/featured-insights/week-in-charts/ais-power-binge
- Epoch AI - ChatGPT Energy: https://epochai.org/gradient-updates/how-much-energy-does-chatgpt-use

### Memoria + Semiconductores
- TrendForce (informes de mercado): https://www.trendforce.com
- Gartner - Semiconductor Forecast: https://www.gartner.com
- Yahoo Finance / Reuters - Entrevistas CEOs (SK Hynix, Micron)