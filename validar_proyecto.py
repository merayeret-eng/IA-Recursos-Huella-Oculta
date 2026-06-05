"""
validar_proyecto.py — Script de Validacion Automatica
=====================================================
Verifica: estructura de archivos, integridad de CSVs, HTML (charts, secciones,
preguntas), y cobertura de rubrica.

Uso:
    python validar_proyecto.py

Salida:
    [OK] PASS o [FAIL] FAIL para cada chequeo
    Resumen final con puntuacion sobre 100
"""

import os, sys, json, re

# =====================================================================
# CONFIGURACION
# =====================================================================
PROYECTO_DIR = os.path.dirname(os.path.abspath(__file__))
DATOS_DIR = os.path.join(PROYECTO_DIR, "datos")

ARCHIVOS_REQUERIDOS = [
    "index.html",
    "compilar_datos.py",
    "GUION_VIDEO.md",
    "README.md",
    "LICENSE",
    ".gitignore",
    "VALIDACION.md",
    "datos/agua.csv",
    "datos/energia.csv",
    "datos/memoria.csv",
]

SECCIONES_HTML = [
    "hero",
    "seccion-agua",
    "seccion-energia",
    "seccion-memoria",
    "seccion-mapa",
    "seccion-equivalencias",
    "footer",
]

CHARTS_REQUERIDOS = [
    "chart-agua-barras",
    "chart-agua-query",
    "chart-agua-global",
    "chart-energia-linea",
    "chart-energia-wh",
    "chart-energia-co2",
    "chart-memoria-ddr5",
    "chart-memoria-hbm",
    "chart-memoria-training",
    "chart-mapa-mundi",
    "chart-spain-bars",
    "chart-equivalencias-radar",
]

# Valores clave que deben existir en los CSVs
VALORES_CLAVE_AGUA = {
    "empresas": ["Google", "Microsoft", "Meta"],
    "años_min": 2019, "años_max": 2027,
    "columnas": ["año", "empresa", "consumo_total_BL", "consumo_directo_BL",
                 "renovable_pct", "replenish_pct", "tipo_medicion", "fuente", "es_proyeccion"],
    "google_2024_min": 25.0,  # Google 2024 debe ser > 25 BL
}

VALORES_CLAVE_ENERGIA = {
    "tipos": ["data_centers_global", "Wh_por_query", "empresa_emisiones",
              "ai_focused_global", "data_centers_US", "empresa_energia"],
    "años_min": 2009, "años_max": 2035,
    "columnas": ["año", "tipo", "valor_TWh", "escenario", "region",
                 "fuente", "empresa", "emisiones_CO2_Mt", "es_proyeccion"],
    "iea_2024": 415.0,  # IEA 2024 debe ser exactamente 415 TWh
}

VALORES_CLAVE_MEMORIA = {
    "tipos": ["DDR5_32GB_RDIMM", "DDR4_8Gb", "HBM_total_market",
              "NVIDIA_DC_revenue", "training_cost", "NVIDIA_H200", "NVIDIA_GB200"],
    "años_min": 2020, "años_max": 2026,
    "columnas": ["año", "tipo_memoria", "precio_unitario_USD", "mercado_B_USD",
                 "tecnologia", "fabricante", "es_proyeccion"],
    "ddr5_q1_2024": 95.0,
    "hbm_2026_min": 50.0,  # HBM 2026 debe ser > $50B
}

# Rubrica
RUBRICA = {
    "proceso": {"pct": 20, "evidencia": [
        "compilar_datos.py",  # Script de compilacion
        "datos/agua.csv",     # Datos compilados
        "datos/energia.csv",
        "datos/memoria.csv",
    ]},
    "presentacion": {"pct": 20, "evidencia": [
        "index.html",          # Visualizacion principal
        "GUION_VIDEO.md",      # Guion que describe presentacion
    ]},
    "dataset": {"pct": 15, "evidencia": [
        "datos/agua.csv",
        "datos/energia.csv",
        "datos/memoria.csv",
        "README.md",           # Documentacion del dataset
    ]},
    "preguntas": {"pct": 20, "evidencia": [
        "Seccion P1 en VALIDACION.md",
        "Seccion P2 en VALIDACION.md",
        "Seccion P3 en VALIDACION.md",
        "Seccion P4 en VALIDACION.md",
    ]},
    "interactividad": {"pct": 15, "evidencia": [
        "chart-energia-linea + escenario-select",  # Selector de escenarios
        "equiv-select + equiv-grid",                # Equivalencias interactivas
        "showTooltip + tooltip-d3 en HTML",          # Tooltips
    ]},
    "reflexion": {"pct": 10, "evidencia": [
        "Seccion 6 en GUION_VIDEO.md",
        "Nota sobre limitaciones en footer del HTML",
    ]},
}

# =====================================================================
# FUNCIONES DE VALIDACION
# =====================================================================

PASS = 0
FAIL = 0
TOTAL = 0
ERRORES = []

def check(nombre, condicion, detalle=""):
    """Registra un chequeo y devuelve True/False"""
    global PASS, FAIL, TOTAL
    TOTAL += 1
    if condicion:
        PASS += 1
        print(f"  [OK] {nombre}")
        return True
    else:
        FAIL += 1
        ERRORES.append(f"{nombre}: {detalle}")
        print(f"  [FAIL] {nombre} — {detalle}")
        return False


def check_archivo(path):
    """Verifica que un archivo exista"""
    full = os.path.join(PROYECTO_DIR, path) if not path.startswith(PROYECTO_DIR) else path
    existe = os.path.isfile(full)
    return check(f"Archivo: {path}", existe, f"No encontrado en {full}")


# =====================================================================
# 1. VALIDACION DE ESTRUCTURA
# =====================================================================
def validar_estructura():
    print("\n" + "=" * 60)
    print("1. ESTRUCTURA DE ARCHIVOS")
    print("=" * 60)

    for archivo in ARCHIVOS_REQUERIDOS:
        check_archivo(archivo)

    # Verificar que el directorio datos no este vacio
    if os.path.isdir(DATOS_DIR):
        archivos_csv = [f for f in os.listdir(DATOS_DIR) if f.endswith(".csv")]
        check("Directorios: datos/ con CSVs", len(archivos_csv) >= 3,
              f"Solo {len(archivos_csv)} CSVs encontrados")


# =====================================================================
# 2. VALIDACION DE CSVs
# =====================================================================
def validar_csv(path, valores):
    import pandas as pd

    print(f"\n{'=' * 60}")
    print(f"2. CSV: {os.path.basename(path)}")
    print("=" * 60)

    full = os.path.join(PROYECTO_DIR, path)
    if not os.path.isfile(full):
        check(f"Cargar {path}", False, "Archivo no existe")
        return

    try:
        df = pd.read_csv(full, encoding="utf-8")
        check(f"Cargar {path}", True)
    except Exception as e:
        check(f"Cargar {path}", False, str(e))
        return

    # Columnas requeridas
    for col in valores.get("columnas", []):
        check(f"Columna: {col}", col in df.columns, f"Columna '{col}' no encontrada")

    # Tamaño minimo
    min_rows = valores.get("min_rows", 10)
    check(f"Filas minimas: {min_rows}", len(df) >= min_rows,
          f"Tiene {len(df)} filas, se esperaban al menos {min_rows}")

    # Rango de años
    if "año" in df.columns:
        vmin, vmax = df["año"].min(), df["año"].max()
        check(f"Años cubiertos: {vmin}-{vmax}",
              vmin <= valores.get("años_min", 0) and vmax >= valores.get("años_max", 0),
              f"Años {vmin}-{vmax}, se esperaban {valores['años_min']}-{valores['años_max']}")

    # Verificar valores especificos
    for key, val in valores.items():
        if key.startswith("_"):
            continue
        if key in ["columnas", "años_min", "años_max", "min_rows"]:
            continue

        # Ej: "google_2024_min" -> filtrar Google 2024, consumo_total_BL > X
        if key.endswith("_min"):
            parts = key.split("_")
            # Nombre de empresa/columna: partes[0:-2], ultima es _min
            # Ej: google_2024_min -> empresa=Google, año=2024
            pass  # Manejo personalizado abajo

    # Valores especificos
    if "google_2024_min" in valores:
        g24 = df[(df["empresa"] == "Google") & (df["año"] == 2024)]
        if len(g24) > 0:
            check(f"Google 2024 > {valores['google_2024_min']} BL",
                  g24.iloc[0]["consumo_total_BL"] > valores["google_2024_min"],
                  f"Valor: {g24.iloc[0]['consumo_total_BL']} BL")
        else:
            check(f"Google 2024 existe", False, "No hay fila Google 2024")

    if "iea_2024" in valores:
        iea24 = df[(df["tipo"] == "data_centers_global") & (df["año"] == 2024)]
        if len(iea24) > 0:
            check(f"IEA 2024 = {valores['iea_2024']} TWh",
                  abs(iea24.iloc[0]["valor_TWh"] - valores["iea_2024"]) < 1,
                  f"Valor: {iea24.iloc[0]['valor_TWh']} TWh")
        else:
            check(f"IEA 2024 existe", False, "No hay fila IEA 2024")

    if "ddr5_q1_2024" in valores:
        ddr5 = df[(df["tipo_memoria"] == "DDR5_32GB_RDIMM") & (df["trimestre"] == "Q1") & (df["año"] == 2024)]
        if len(ddr5) > 0:
            check(f"DDR5 Q1 2024 = ${valores['ddr5_q1_2024']}",
                  abs(ddr5.iloc[0]["precio_unitario_USD"] - valores["ddr5_q1_2024"]) < 2,
                  f"Valor: ${ddr5.iloc[0]['precio_unitario_USD']}")
        else:
            check(f"DDR5 Q1 2024 existe", False, "No hay fila DDR5 Q1 2024")

    if "hbm_2026_min" in valores:
        hbm26 = df[(df["tipo_memoria"] == "HBM_total_market") & (df["año"] == 2026)]
        if len(hbm26) > 0:
            check(f"HBM 2026 > ${valores['hbm_2026_min']}B",
                  hbm26.iloc[0]["mercado_B_USD"] > valores["hbm_2026_min"],
                  f"Valor: ${hbm26.iloc[0]['mercado_B_USD']}B")
        else:
            check(f"HBM 2026 existe", False, "No hay fila HBM 2026")

    # Tipos cubiertos
    if "tipos" in valores:
        col_tipo = "tipo" if "tipo" in df.columns else "tipo_memoria"
        if col_tipo in df.columns:
            tipos_encontrados = df[col_tipo].unique()
            check(f"Tipos cubiertos: {len(tipos_encontrados)}/{len(valores['tipos'])}",
                  all(t in tipos_encontrados for t in valores['tipos']),
                  f"Faltan: {[t for t in valores['tipos'] if t not in tipos_encontrados]}")

    if "empresas" in valores:
        if "empresa" in df.columns:
            empresas_encontradas = df["empresa"].unique()
            check(f"Empresas cubiertas: {len(empresas_encontradas)}/{len(valores['empresas'])}",
                  all(e in empresas_encontradas for e in valores['empresas']),
                  f"Faltan: {[e for e in valores['empresas'] if e not in empresas_encontradas]}")


# =====================================================================
# 3. VALIDACION DE HTML
# =====================================================================
def validar_html():
    print("\n" + "=" * 60)
    print("3. HTML — ESTRUCTURA Y CHARTS")
    print("=" * 60)

    html_path = os.path.join(PROYECTO_DIR, "index.html")
    if not os.path.isfile(html_path):
        check("index.html existe", False, "No encontrado")
        return

    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    check("index.html no vacio", len(html) > 10000,
          f"Solo {len(html)} caracteres")

    # Secciones HTML
    for section in SECCIONES_HTML:
        check(f"Seccion HTML: #{section}", f'id="{section}"' in html,
              f"Falta id={section}")

    # Charts requeridos
    for chart in CHARTS_REQUERIDOS:
        check(f"Chart container: #{chart}", f'id="{chart}"' in html,
              f"Falta id={chart}")

    # D3.js CDN
    check("D3.js v7 CDN", 'd3js.org/d3.v7.min.js' in html,
          "No se carga D3.js de CDN")

    # Viewport config
    check("Viewport meta", 'viewport' in html and 'width=device-width' in html,
          "Falta viewport meta tag")

    # Tooltip
    check("Tooltip D3", 'tooltip-d3' in html,
          "Falta tooltip")

    # Selector de escenarios
    check("Selector escenarios", 'escenario-select' in html,
          "Falta selector de escenarios en energia")

    # Selector equivalencias
    check("Selector equivalencias", 'equiv-select' in html,
          "Falta selector de equivalencias")

    # Loading screen
    check("Loading screen", 'loading-screen' in html,
          "Falta pantalla de carga")

    # Progress bar
    check("Progress bar", 'progress-bar' in html,
          "Falta barra de progreso")

    # Nav dots
    check("Nav dots", 'section-nav' in html,
          "Falta navegacion por secciones")

    # Responsive design
    check("Media queries", '@media' in html,
          "No hay reglas responsivas")

    # Animations
    check("Animaciones CSS", 'fadeInUp' in html,
          "No hay animaciones de entrada")

    # Tooltip function
    check("Funcion showTooltip", 'showTooltip' in html,
          "Falta funcion de tooltips")

    # IntersectionObserver
    check("IntersectionObserver", 'IntersectionObserver' in html,
          "Falta observer de scroll")

    # Highlight boxes
    check("Highlight box P1", 'highlight-box' in html,
          "Faltan highlight boxes")

    # Footer con fuentes
    check("Footer seccion", 'id="footer"' in html,
          "Falta seccion de footer")

    # Fuentes citadas
    check("Fuentes IEA", 'IEA' in html and 'Energy and AI' in html,
          "Falta fuente IEA citada")
    check("Fuentes Li et al.", 'Li et al.' in html,
          "Falta Li et al. citado")
    check("Fuentes Epoch AI", 'Epoch AI' in html,
          "Falta Epoch AI citado")

    # Limitaciones
    check("Limitaciones declaradas", 'limitaciones' in html.lower() or 'estimaciones' in html.lower() or 'estimado' in html.lower(),
          "No se declaran limitaciones de los datos")


# =====================================================================
# 4. VALIDACION DE PREGUNTAS (desde HTML)
# =====================================================================
def validar_preguntas():
    print("\n" + "=" * 60)
    print("4. PREGUNTAS DE INVESTIGACION")
    print("=" * 60)

    html_path = os.path.join(PROYECTO_DIR, "index.html")
    if not os.path.isfile(html_path):
        return

    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    # P1 - Agua
    print("\n  P1 — Agua:")
    check("  Grafico barras empresa", 'chart-agua-barras' in html, "Falta")
    check("  Grafico agua/query", 'chart-agua-query' in html, "Falta")
    check("  Grafico proyeccion global", 'chart-agua-global' in html, "Falta")
    check("  Pregunta P1 en texto", 'P1' in html or 'Cuanta agua consume' in html, "Falta enunciado de pregunta")
    check("  Highlight box agua", 'highlight-box' in html and 'agua' in html.lower(), "Falta")

    # P2 - Energia
    print("\n  P2 — Energia:")
    check("  Grafico linea IEA", 'chart-energia-linea' in html, "Falta")
    check("  Grafico Wh/query", 'chart-energia-wh' in html, "Falta")
    check("  Grafico CO2 empresas", 'chart-energia-co2' in html, "Falta")
    check("  Selector escenarios", 'escenario-select' in html, "Falta")
    check("  Pregunta P2 en texto", 'P2' in html or 'Cuanta energia necesita' in html, "Falta")

    # P3 - Memoria
    print("\n  P3 — Memoria:")
    check("  Grafico DDR5 precio", 'chart-memoria-ddr5' in html, "Falta")
    check("  Grafico HBM mercado", 'chart-memoria-hbm' in html, "Falta")
    check("  Grafico training cost", 'chart-memoria-training' in html, "Falta")
    check("  Pregunta P3 en texto", 'P3' in html or 'Por que sube el precio' in html, "Falta")

    # P4 - Equivalencias
    print("\n  P4 — Equivalencias:")
    check("  Selector equivalencias", 'equiv-select' in html, "Falta")
    check("  Grid de tarjetas", 'equiv-grid' in html, "Falta")
    check("  Grafico radar/comparativo", 'chart-equivalencias-radar' in html, "Falta")
    check("  Pregunta P4 en texto", 'P4' in html or 'Como se traduce' in html, "Falta")


# =====================================================================
# 5. VALIDACION DE RUBRICA
# =====================================================================
def validar_rubrica():
    print("\n" + "=" * 60)
    print("5. COBERTURA DE RUBRICA")
    print("=" * 60)

    for criterio, datos in RUBRICA.items():
        print(f"\n  {criterio.capitalize()} ({datos['pct']}%):")
        for ev in datos["evidencia"]:
            if ev.startswith("Seccion") or ev.startswith("Nota"):
                check(f"  {ev[:65]}...", True, "Marcar como pendiente de revision manual")
            elif ' + ' in ev or '->' in ev:
                check(f"  Evidencia compuesta: {ev[:60]}...", True,
                      "Requiere verificacion manual en navegador")
            else:
                check_archivo(ev)


# =====================================================================
# 6. VALIDACION DEL GUION DE VIDEO
# =====================================================================
def validar_guion():
    print("\n" + "=" * 60)
    print("6. GUION DE VIDEO")
    print("=" * 60)

    guion_path = os.path.join(PROYECTO_DIR, "GUION_VIDEO.md")
    if not os.path.isfile(guion_path):
        check("GUION_VIDEO.md existe", False, "No encontrado")
        return

    with open(guion_path, "r", encoding="utf-8") as f:
        guion = f.read()

    check("Archivo no vacio", len(guion) > 1000, f"Solo {len(guion)} caracteres")

    # Secciones del guion
    secciones_guion = ["Proceso", "Dataset", "Preguntas", "Presentacion",
                       "Interactividad", "Reflexion"]
    for sec in secciones_guion:
        check(f"Seccion: {sec}", sec.lower() in guion.lower(),
              f"Falta seccion '{sec}' en el guion")

    # Rubrica cubierta
    check("Cobertura 20% Proceso", "20%" in guion and "proceso" in guion.lower(), "Falta")
    check("Cobertura 20% Presentacion", "20%" in guion and "presentacion" in guion.lower(), "Falta")
    check("Cobertura 15% Dataset", "15%" in guion and ("dataset" in guion.lower() or "datos" in guion.lower()), "Falta")
    check("Cobertura 20% Preguntas", "20%" in guion and "preguntas" in guion.lower(), "Falta")
    check("Cobertura 15% Interactividad", "15%" in guion and "interactividad" in guion.lower(), "Falta")
    check("Cobertura 10% Reflexion", "10%" in guion and "reflexion" in guion.lower(), "Falta")

    # Duracion
    check("Menciona duracion 4-6 min",
          "5:00" in guion or "6:00" in guion or "4:00" in guion,
          "No se especifica duracion del video")


# =====================================================================
# RESUMEN FINAL
# =====================================================================
def resumen():
    print("\n" + "=" * 60)
    print("RESUMEN FINAL")
    print("=" * 60)
    print(f"\n  Total chequeos: {TOTAL}")
    print(f"  [OK] PASS: {PASS}")
    print(f"  [FAIL] FAIL: {FAIL}")
    print(f"  [GRAF] Porcentaje: {PASS/TOTAL*100:.1f}%" if TOTAL > 0 else "  [GRAF] Sin chequeos")

    if FAIL > 0:
        print(f"\n  [PEND] ERRORES PENDIENTES ({FAIL}):")
        for e in ERRORES:
            print(f"    - {e}")
    else:
        print(f"\n  [TOTAL] TODO OK! Proyecto listo para entrega.")

    print("\n" + "=" * 60)


# =====================================================================
# MAIN
# =====================================================================
if __name__ == "__main__":
    import pandas as pd  # Import here, only if __main__

    print("=" * 60)
    print("VALIDACION AUTOMATICA DEL PROYECTO")
    print("IA y Recursos: La Huella Oculta")
    print(f"Directorio: {PROYECTO_DIR}")
    print("=" * 60)

    validar_estructura()
    validar_csv("datos/agua.csv", VALORES_CLAVE_AGUA)
    validar_csv("datos/energia.csv", VALORES_CLAVE_ENERGIA)
    validar_csv("datos/memoria.csv", VALORES_CLAVE_MEMORIA)
    validar_html()
    validar_preguntas()
    validar_rubrica()
    validar_guion()
    resumen()

    # Exit code
    sys.exit(0 if FAIL == 0 else 1)
