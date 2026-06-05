# Guion de Video — IA y Recursos: La Huella Oculta

**Duracion total:** 5:00 - 6:00 minutos
**Autor:** Aaron Mera
**Asignatura:** Visualizacion de Datos — Master Data Science UOC

---

## Estructura Rubrica

| Seccion | Duracion | % Rubrica | Contenido |
|---------|----------|-----------|-----------|
| 1. Proceso | ~1:00 | 20% | Como se compilaron los datos, fuentes, metodologia |
| 2. Dataset | ~0:45 | 15% | Estructura del dataset, 25+ variables, 3 dimensiones |
| 3. Preguntas P1-P4 | ~2:00 | 20% | 4 preguntas de investigacion respondidas |
| 4. Presentacion | ~1:00 | 20% | Recorrido por la visualizacion, 6 secciones, tema vintage |
| 5. Interactividad | ~0:45 | 15% | Funcionalidades interactivas (selectores, tooltips, mapa, equivalencias) |
| 6. Reflexion | ~0:30 | 10% | Aprendizajes, limitaciones, trabajos futuros |

---

## Script Detallado

### [0:00 - 0:10] Introduccion (10s)

**Visual:** Pantalla de inicio con titulo "IA y Recursos: La Huella Oculta"
**Audio:**
"Hola, soy Aaron Mera. En este video presento el proyecto 'IA y Recursos: La Huella Oculta',
una visualizacion interactiva que explora el costo ambiental de la inteligencia artificial:
el agua que consume, la energia que necesita y la memoria que demanda."

---

### [0:10 - 1:10] SECCION 1: Proceso (60s) — 20%

**Visual:** Secuencia rapida mostrando logos de IEA, Google, Microsoft, Meta, capturas de informes

**Audio:**
"El proceso de compilacion de datos fue una investigacion exhaustiva desde cero.
No parti de un dataset preexistente, sino que fui a las fuentes primarias:

Primero, el informe 'Energy and AI' de la Agencia Internacional de la Energia (IEA, 2025),
que proporciona las proyecciones mas autorizadas sobre consumo electrico de centros de datos.

Segundo, los informes de sostenibilidad de Google, Microsoft y Meta —sus reportes ambientales de 2025—
para obtener datos reales de consumo de agua y emisiones.

Tercero, el estudio academico de Li et al. (2023), 'Making AI Less Thirsty',
que cuantifica el agua necesaria para entrenar y ejecutar modelos de lenguaje.

Cuarto, datos de Epoch AI sobre eficiencia energetica por consulta de modelos como GPT-4o,
y reportes de mercado de TrendForce para los precios de memoria DRAM y HBM.

Quinto, el informe Microsoft AI Diffusion Index H2 2025 para datos de adopcion de IA
por pais, que permitio crear el mapamundi interactivo y la comparativa de España.

En total, consulte mas de 12 fuentes, compile 25+ variables, y estructure todo en tres CSVs."

---

### [1:10 - 1:55] SECCION 2: Dataset (45s) — 15%

**Visual:** Mostrar los 3 CSVs (agua.csv, energia.csv, memoria.csv) con sus columnas

**Audio:**
"El dataset resultante se organiza en tres archivos CSV, uno por dimension:

'agua.csv' contiene 29 registros con datos de Google, Microsoft y Meta entre 2019 y 2026,
incluyendo consumo total en billones de litros, porcentaje de energia renovable,
y la metrica de agua por consulta de los estudios de Li et al.

'energia.csv' tiene 31 registros con las proyecciones de la IEA hasta 2035,
datos de emisiones de CO2 de Amazon, Microsoft y Meta,
y la comparativa de eficiencia energetica entre distintos modelos de IA.

'memoria.csv' con 25 registros sobre la evolucion de precios de DDR5, DDR4,
el crecimiento explosivo del mercado HBM de $10,000 millones a $55,000 millones,
y el costo de entrenar modelos como GPT-3, GPT-4 y la proyeccion de GPT-5.

En total hablamos de 85 registros distribuidos en tres dimensiones interconectadas."

---

### [1:55 - 3:55] SECCION 3: Preguntas de Investigacion (120s) — 20%

#### [1:55 - 2:25] P1: Agua (30s)

**Visual:** Seccion de agua en la visualizacion — grafico de barras apiladas

**Audio:**
"Primera pregunta: ¿Como ha evolucionado el consumo de agua de los gigantes tecnologicos?

Google es, con diferencia, el mayor consumidor: 30.7 billones de litros en 2024,
frente a los 5.8 de Microsoft y los 3 de Meta. Pero lo mas preocupante no es el volumen absoluto,
sino la tendencia: el consumo de Google crecio un 60% entre 2020 y 2024, y se proyecta
que alcance los 40 billones de litros en 2026.

Ademas, segun Li et al., una conversacion tipica de ChatGPT de entre 5 y 50 preguntas
consume aproximadamente 500 mililitros de agua. Si bien GPT-4o redujo significativamente
el consumo respecto a GPT-3, el volumen masivo de consultas —500 millones diarias—
hace que el impacto siga siendo enorme."

#### [2:25 - 3:00] P2: Energia (35s)

**Visual:** Grafico de linea con proyecciones IEA + barras de Wh por consulta

**Audio:**
"Segunda pregunta: ¿Cual es la tendencia de consumo electrico?

En 2024, los centros de datos consumieron 415 TWh, el 1.5% de la electricidad global.
Para 2030, la IEA proyecta entre 945 TWh en el escenario base y hasta 1,400 TWh
en el escenario 'lift-off' de adopcion acelerada de IA.

La buena noticia es que la eficiencia mejora radicalmente: GPT-4o consume solo 0.3 Wh
por consulta tipica, exactamente lo mismo que una busqueda de Google en 2009,
y 10 veces menos que los 3 Wh de GPT-3.5.

Pero el volumen de uso crece mas rapido que la eficiencia, lo que significa
que el consumo absoluto sigue aumentando."

#### [3:00 - 3:30] P3: Memoria (30s)

**Visual:** Graficos de DDR5, HBM y costos de entrenamiento

**Audio:**
"Tercera pregunta: ¿Por que sube el precio de la memoria?

El precio de la DDR5 paso de $95 en el primer trimestre de 2024 a $189 en 2026,
y se proyecta que alcance los $310 a finales de 2026. Pero el caso mas dramatico
es el mercado HBM —la memoria de alto ancho de banda que usan las GPUs de NVIDIA—
que crecio de $10,000 millones en 2023 a $55,000 millones proyectados para 2026.
Y entrenar GPT-5 podria costar $1,000 millones, 100 veces mas que GPT-4."

#### [3:30 - 3:55] P4: Equivalencias (25s)

**Visual:** Seccion de equivalencias interactivas + grafico comparativo

**Audio:**
"Cuarta pregunta: ¿Como se relacionan estas dimensiones?

He creado equivalencias interactivas que traducen los numeros a conceptos cotidianos:
Una consulta de GPT-4o consume 0.3 Wh y unos 50 mililitros de agua. Puede parecer poco,
pero las 500 millones de consultas diarias de ChatGPT requieren 150 MWh de electricidad
y 25 millones de litros de agua cada dia.

Estas tres dimensiones —agua, energia, memoria— estan profundamente conectadas:
mas potencia de calculo requiere mas memoria, mas memoria genera mas calor,
mas calor necesita mas agua para refrigeracion, y todo consume mas energia."

---

### [3:55 - 4:55] SECCION 4: Presentacion del Dashboard (60s) — 20%

**Visual:** Recorrido lento por toda la pagina, seccion por seccion

**Audio:**
"La visualizacion esta construida como una pagina web de scroll storytelling,
con 6 secciones narrativas y un diseno vintage que evoca los mapas y diagramas
cientificos del siglo XIX. Use la tipografia 'Playfair Display' para los titulos,
'IBM Plex Mono' para los datos numericos, y una paleta de colores sepia, parchment
y rust que recuerda a los atlas antiguos.

La pagina se estructura asi:

Primero, el hero con los 4 indicadores clave de impacto ambiental.

Segundo, la seccion de agua con sus graficos de barras apiladas, el consumo
por consulta, y la proyeccion global.

Tercero, la seccion de energia con el selector de escenarios de la IEA,
la comparativa de Wh por consulta, y las emisiones de CO2.

Cuarto, la seccion de memoria con la evolucion de precios DDR5,
el mercado HBM y el costo de entrenar modelos.

Quinto, una nueva seccion con un **mapamundi coropletico interactivo**
que muestra la adopcion de IA generativa en 177 paises, con datos del
Microsoft AI Diffusion Index. España aparece destacada con un borde dorado,
mostrando su posicion como uno de los lideres europeos con un 24% de adopcion.
Acompanando al mapa, un grafico de barras compara a España con los 18 paises
con mayor adopcion.

Sexto, la seccion de equivalencias interactivas que traduce los numeros
a conceptos cotidianos con tres niveles de profundidad.

Cada grafico tiene tooltips que muestran los valores exactos al pasar el raton,
y la navegacion se facilita con puntos en la parte derecha y una barra
de progreso en la parte superior."

---

### [4:55 - 5:40] SECCION 5: Interactividad (45s) — 15%

**Visual:** Demostrar cada elemento interactivo en accion

**Audio:**
"Los elementos interactivos son cuatro:

Primero, el selector de escenarios en la seccion de energia permite alternar
entre el escenario base de la IEA y el escenario 'lift-off' de adopcion acelerada,
actualizando el grafico en tiempo real.

Segundo, el **mapamundi interactivo**: al pasar el raton sobre cualquier pais,
un tooltip muestra el nombre y el porcentaje de adopcion. España tiene un
resalte especial con borde dorado. Ademas, la leyenda de 8 rangos permite
interpretar rapidamente la distribucion global.

Tercero, las equivalencias interactivas: un menu desplegable permite cambiar entre
tres niveles —una consulta individual, un dia de uso global de ChatGPT,
o el entrenamiento de un modelo completo— mostrando tarjetas con equivalencias
en agua, energia y costo.

Cuarto, los tooltips en cada grafico: al pasar el raton sobre cualquier barra,
linea o punto, se muestra el valor exacto con contexto adicional.

Toda la visualizacion es responsiva y funciona correctamente en movil y escritorio."

---

### [5:40 - 6:10] SECCION 6: Reflexion (30s) — 10%

**Visual:** Seccion final con fuentes y creditos

**Audio:**
"Para cerrar, tres reflexiones:

Primera: La IA no es intangible. Cada consulta tiene un costo fisico medible
en agua, energia y recursos. Como futuros cientificos de datos, debemos
incorporar estas metricas en nuestras decisiones.

Segunda: La eficiencia mejora — GPT-4o consume 10 veces menos que GPT-3 —
pero el efecto rebote es real: consumimos mas porque es mas accesible.

Tercera: Las proyecciones de la IEA muestran que para 2030 la IA podria
consumir el 3% de la electricidad global. No es una crisis inminente,
pero es una senal que no podemos ignorar.

Las fuentes completas estan en la seccion final de la pagina. El codigo
y los datos estan disponibles en GitHub.

Gracias por ver esta presentacion."

---

## Guia de Presentacion — Checklist y Recomendaciones

### Preparacion Pre-Grabacion

- [ ] Abrir `index.html` en Chrome/Edge (NO Explorer)
- [ ] Verificar que todos los graficos cargan (esperar 3-4s por el mapa TopoJSON)
- [ ] Desactivar notificaciones del sistema operativo
- [ ] Cerrar pestañas del navegador no relacionadas
- [ ] Resolucion de pantalla: 1920x1080 (o superior)
- [ ] Ventana del navegador en pantalla completa (F11)

### Durante la Grabacion

| Momento | Accion | Que mostrar |
|---------|--------|-------------|
| 0:00-0:10 | Intro | Pantalla de inicio, titulo |
| 0:10-1:10 | Proceso | Scroll rapido por la pagina, señalar logos/fuentes |
| 1:10-1:55 | Dataset | Mostrar los CSVs (abrir archivos o mostrar estructura) |
| 1:55-2:25 | P1 Agua | SCROLL a seccion agua, pasar raton sobre barras (tooltips) |
| 2:25-3:00 | P2 Energia | SCROLL a energia, CAMBIAR selector escenarios, mostrar tooltips |
| 3:00-3:30 | P3 Memoria | SCROLL a memoria, mostrar linea DDR5 + tooltips |
| 3:30-3:55 | P4 Equivalencias | SCROLL a equivalencias, CAMBIAR selector 3 veces (query/dia/entreno) |
| 3:55-4:55 | Presentacion | SCROLL LENTO desde hero hasta footer (pausar en mapa) |
| 4:55-5:40 | Interactividad | Volver a mapa (hover paises + España), luego equivalencias, tooltips |
| 5:40-6:10 | Reflexion | SCROLL a footer, señalar fuentes |

### Puntos Clave a Demostrar

1. **Mapamundi:** Pasar el raton sobre España, Francia, Alemania, EEUU, Singapur para mostrar tooltips
2. **Selector escenarios:** Cambiar de "Base" a "Lift-Off" y señalar el cambio en la grafica
3. **Selector equivalencias:** Cambiar entre los 3 niveles y leer las tarjetas
4. **Tooltips:** Mostrar en grafico de DDR5, en barras de HBM, en lineas de CO2
5. **Nav dots:** Hacer scroll rapido y señalar que el punto activo cambia

### Consejos Tecnicos

- **Grabacion:** OBS Studio (gratuito, open source)
- **Resolucion:** 1920x1080, 30fps
- **Audio:** Microfono externo, grabar en sala silenciosa
- **Cursor:** Usar cursor del mouse, NO el dedo en trackpad (se ve tembloroso)
- **Zoom:** Si es necesario, Zoom al 100-125% del navegador para que se vean bien los graficos
- **Musica:** Opcional, muy baja (-25dB), sin letra
- **Subtitulos:** Recomendado pero no obligatorio

### Post-Produccion

- [ ] Cortar silencios prolongados
- [ ] Normalizar audio (-3dB a -6dB pico)
- [ ] Subir volumen si es necesario
- [ ] Añadir subtitulos (opcional)
- [ ] Exportar como MP4, H.264
- [ ] Nombre de archivo: `Mera_Aaron_Video.mkv`

### Errores Comunes a Evitar

- ❌ No leer textualmente el guion — usar palabras propias
- ❌ No cubrirse la cara con la ventana de graficos
- ❌ No mostrar el escritorio con archivos personales
- ❌ No exceder los 6 minutos
- ❌ No olvidar mencionar fuentes ni limitaciones
- ✅ Mantener ritmo constante, no apresurarse
- ✅ Hacer pausas entre secciones

---

## Notas Tecnicas para la Grabacion

### Herramientas sugeridas
- **Grabacion:** OBS Studio o similar
- **Resolucion:** 1920x1080
- **Audio:** Microfono externo, silencio absoluto

### Estilo de presentacion
- Voz clara, ritmo constante
- Mostrar la pagina web en pantalla completa
- Destacar con el cursor los elementos interactivos
- Alternar entre la pagina y una camara (opcional)

### Post-produccion
- Incluir subtitulos (opcional pero recomendado)
- Musica de fondo suave (opcional)
- Transiciones simples entre secciones

---

## Checklist Pre-Entrega

- [ ] Video grabado (min 4:00, max 6:00)
- [ ] Audio claro, sin ruido de fondo
- [ ] Todos los elementos interactivos demostrados
- [ ] Mapamundi con hover sobre paises y España destacada
- [ ] Selector de escenarios y selector de equivalencias
- [ ] Tooltips en todos los graficos
- [ ] Fuentes citadas
- [ ] Reflexion personal incluida
- [ ] Formato: MP4, H.264
- [ ] Nombre archivo: Apellido_Nombre_Video.mkv (o similar)
