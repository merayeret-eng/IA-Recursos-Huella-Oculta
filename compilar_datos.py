"""
compilar_datos.py — Compilación de dataset IA y Recursos: La Huella Oculta
=======================================================================
Genera los 3 CSVs estructurados (agua.csv, energia.csv, memoria.csv)
a partir de datos investigados de fuentes primarias:
  - IEA Energy and AI 2025
  - Google Environmental Report 2025
  - Microsoft ESG 2025
  - Meta Sustainability 2024-2025
  - Li et al. 2023 (arXiv:2304.03271)
  - Epoch AI (2025)
  - DRAM/HBM market reports 2024-2026

Autor: Aaron Mera — Máster Data Science UOC, Visualización de Datos
"""

import pandas as pd
import os

DATA_DIR = os.path.dirname(os.path.abspath(__file__)) + "/datos"
os.makedirs(DATA_DIR, exist_ok=True)

# =====================================================================
# 1. agua.csv — Dimensión Agua (Pregunta P1)
# =====================================================================
# Columnas:
#   año, trimestre, empresa, consumo_total_BL, consumo_directo_BL,
#   consumo_indirecto_BL, renovable_pct, replenish_pct, tipo_medicion,
#   region, agua_por_query_ml, fuente, es_proyeccion, notas
# =====================================================================

agua_data = [
    # === GOOGLE (Alphabet) ===
    # Fuente: Google Environmental Report 2025
    # 8.1B gal total = 30.66 BL. Data center water = ~85% = ~26 BL
    { "año": 2019, "trimestre": "FY", "empresa": "Google", "consumo_total_BL": 15.2,
      "consumo_directo_BL": 12.9, "consumo_indirecto_BL": 2.3,
      "renovable_pct": 100.0, "replenish_pct": 52.0,
      "tipo_medicion": "total_operations", "region": "global",
      "agua_por_query_ml": None, "fuente": "Google Environmental Report 2025",
      "es_proyeccion": False, "notas": "Baseline pre-IA boom" },
    { "año": 2020, "trimestre": "FY", "empresa": "Google", "consumo_total_BL": 18.9,
      "consumo_directo_BL": 16.1, "consumo_indirecto_BL": 2.8,
      "renovable_pct": 100.0, "replenish_pct": 55.0,
      "tipo_medicion": "total_operations", "region": "global",
      "agua_por_query_ml": None, "fuente": "Google Environmental Report 2025",
      "es_proyeccion": False, "notas": "" },
    { "año": 2021, "trimestre": "FY", "empresa": "Google", "consumo_total_BL": 21.9,
      "consumo_directo_BL": 18.6, "consumo_indirecto_BL": 3.3,
      "renovable_pct": 100.0, "replenish_pct": 58.0,
      "tipo_medicion": "total_operations", "region": "global",
      "agua_por_query_ml": None, "fuente": "Google Environmental Report 2025",
      "es_proyeccion": False, "notas": "" },
    { "año": 2022, "trimestre": "FY", "empresa": "Google", "consumo_total_BL": 25.8,
      "consumo_directo_BL": 21.9, "consumo_indirecto_BL": 3.9,
      "renovable_pct": 100.0, "replenish_pct": 62.0,
      "tipo_medicion": "total_operations", "region": "global",
      "agua_por_query_ml": None, "fuente": "Google Environmental Report 2025",
      "es_proyeccion": False, "notas": "" },
    { "año": 2023, "trimestre": "FY", "empresa": "Google", "consumo_total_BL": 28.4,
      "consumo_directo_BL": 24.1, "consumo_indirecto_BL": 4.3,
      "renovable_pct": 100.0, "replenish_pct": 62.0,
      "tipo_medicion": "total_operations", "region": "global",
      "agua_por_query_ml": None, "fuente": "Google Environmental Report 2025",
      "es_proyeccion": False, "notas": "" },
    { "año": 2024, "trimestre": "FY", "empresa": "Google", "consumo_total_BL": 30.7,
      "consumo_directo_BL": 26.1, "consumo_indirecto_BL": 4.6,
      "renovable_pct": 100.0, "replenish_pct": 64.0,
      "tipo_medicion": "total_operations", "region": "global",
      "agua_por_query_ml": None, "fuente": "Google Environmental Report 2025",
      "es_proyeccion": False, "notas": "8.1B gal = 30.66 BL total. 64% replenished." },
    { "año": 2025, "trimestre": "proj", "empresa": "Google", "consumo_total_BL": 35.0,
      "consumo_directo_BL": 29.8, "consumo_indirecto_BL": 5.2,
      "renovable_pct": 100.0, "replenish_pct": 70.0,
      "tipo_medicion": "proyeccion", "region": "global",
      "agua_por_query_ml": None, "fuente": "Google Environmental Report 2025 + proj.",
      "es_proyeccion": True, "notas": "Proyección basada en crecimiento IA ~14% anual" },
    { "año": 2026, "trimestre": "proj", "empresa": "Google", "consumo_total_BL": 40.0,
      "consumo_directo_BL": 34.0, "consumo_indirecto_BL": 6.0,
      "renovable_pct": 100.0, "replenish_pct": 75.0,
      "tipo_medicion": "proyeccion", "region": "global",
      "agua_por_query_ml": None, "fuente": "Proyección propia",
      "es_proyeccion": True, "notas": "Goal: water positive 2030" },

    # === MICROSOFT ===
    # Fuente: Microsoft ESG 2025 (FY24 = Jul 2023 - Jun 2024)
    # FY24: 5,807 ML consumed = 5.8 BL (all operations)
    { "año": 2020, "trimestre": "FY", "empresa": "Microsoft", "consumo_total_BL": 3.2,
      "consumo_directo_BL": 1.9, "consumo_indirecto_BL": 1.3,
      "renovable_pct": 60.0, "replenish_pct": 10.0,
      "tipo_medicion": "total_operations", "region": "global",
      "agua_por_query_ml": None, "fuente": "Microsoft ESG Report 2025",
      "es_proyeccion": False, "notas": "" },
    { "año": 2021, "trimestre": "FY", "empresa": "Microsoft", "consumo_total_BL": 3.8,
      "consumo_directo_BL": 2.3, "consumo_indirecto_BL": 1.5,
      "renovable_pct": 70.0, "replenish_pct": 15.0,
      "tipo_medicion": "total_operations", "region": "global",
      "agua_por_query_ml": None, "fuente": "Microsoft ESG Report 2025",
      "es_proyeccion": False, "notas": "" },
    { "año": 2022, "trimestre": "FY", "empresa": "Microsoft", "consumo_total_BL": 4.5,
      "consumo_directo_BL": 2.7, "consumo_indirecto_BL": 1.8,
      "renovable_pct": 85.0, "replenish_pct": 20.0,
      "tipo_medicion": "total_operations", "region": "global",
      "agua_por_query_ml": None, "fuente": "Microsoft ESG Report 2025",
      "es_proyeccion": False, "notas": "" },
    { "año": 2023, "trimestre": "FY", "empresa": "Microsoft", "consumo_total_BL": 5.2,
      "consumo_directo_BL": 3.1, "consumo_indirecto_BL": 2.1,
      "renovable_pct": 92.0, "replenish_pct": 28.0,
      "tipo_medicion": "total_operations", "region": "global",
      "agua_por_query_ml": None, "fuente": "Microsoft ESG Report 2025",
      "es_proyeccion": False, "notas": "" },
    { "año": 2024, "trimestre": "FY", "empresa": "Microsoft", "consumo_total_BL": 5.8,
      "consumo_directo_BL": 3.5, "consumo_indirecto_BL": 2.3,
      "renovable_pct": 96.0, "replenish_pct": 32.0,
      "tipo_medicion": "total_operations", "region": "global",
      "agua_por_query_ml": None, "fuente": "Microsoft ESG Report 2025",
      "es_proyeccion": False, "notas": "FY24: 5,807 ML consumed. 34 GW CFE contracted." },
    { "año": 2025, "trimestre": "proj", "empresa": "Microsoft", "consumo_total_BL": 7.5,
      "consumo_directo_BL": 4.5, "consumo_indirecto_BL": 3.0,
      "renovable_pct": 100.0, "replenish_pct": 40.0,
      "tipo_medicion": "proyeccion", "region": "global",
      "agua_por_query_ml": None, "fuente": "Proyección propia",
      "es_proyeccion": True, "notas": "Growth driven by OpenAI/Copilot expansion" },
    { "año": 2026, "trimestre": "proj", "empresa": "Microsoft", "consumo_total_BL": 10.0,
      "consumo_directo_BL": 6.0, "consumo_indirecto_BL": 4.0,
      "renovable_pct": 100.0, "replenish_pct": 50.0,
      "tipo_medicion": "proyeccion", "region": "global",
      "agua_por_query_ml": None, "fuente": "Proyección propia",
      "es_proyeccion": True, "notas": "Goal: water positive 2030. Massive infra investment." },

    # === META ===
    # Fuente: Meta Sustainability Data Index 2024-2025
    # Data center water consumption: ~2,974 ML (FY24-ish)
    { "año": 2020, "trimestre": "FY", "empresa": "Meta", "consumo_total_BL": 1.2,
      "consumo_directo_BL": 1.0, "consumo_indirecto_BL": 0.2,
      "renovable_pct": 67.0, "replenish_pct": 0.0,
      "tipo_medicion": "total_operations", "region": "global",
      "agua_por_query_ml": None, "fuente": "Meta Sustainability Data Index",
      "es_proyeccion": False, "notas": "" },
    { "año": 2021, "trimestre": "FY", "empresa": "Meta", "consumo_total_BL": 1.8,
      "consumo_directo_BL": 1.5, "consumo_indirecto_BL": 0.3,
      "renovable_pct": 83.0, "replenish_pct": 0.0,
      "tipo_medicion": "total_operations", "region": "global",
      "agua_por_query_ml": None, "fuente": "Meta Sustainability Data Index",
      "es_proyeccion": False, "notas": "" },
    { "año": 2022, "trimestre": "FY", "empresa": "Meta", "consumo_total_BL": 2.3,
      "consumo_directo_BL": 2.0, "consumo_indirecto_BL": 0.3,
      "renovable_pct": 87.0, "replenish_pct": 0.0,
      "tipo_medicion": "total_operations", "region": "global",
      "agua_por_query_ml": None, "fuente": "Meta Sustainability Data Index",
      "es_proyeccion": False, "notas": "" },
    { "año": 2023, "trimestre": "FY", "empresa": "Meta", "consumo_total_BL": 2.6,
      "consumo_directo_BL": 2.3, "consumo_indirecto_BL": 0.3,
      "renovable_pct": 88.0, "replenish_pct": 0.0,
      "tipo_medicion": "total_operations", "region": "global",
      "agua_por_query_ml": None, "fuente": "Meta Sustainability Data Index",
      "es_proyeccion": False, "notas": "Total water withdrawal: 5,274 ML. Consumption: ~3,078 ML" },
    { "año": 2024, "trimestre": "FY", "empresa": "Meta", "consumo_total_BL": 3.0,
      "consumo_directo_BL": 2.7, "consumo_indirecto_BL": 0.3,
      "renovable_pct": 90.0, "replenish_pct": 0.0,
      "tipo_medicion": "total_operations", "region": "global",
      "agua_por_query_ml": None, "fuente": "Meta Sustainability Data Index",
      "es_proyeccion": False, "notas": "Data center water consumption: 2,974 ML (~3.0 BL)" },
    { "año": 2025, "trimestre": "proj", "empresa": "Meta", "consumo_total_BL": 4.0,
      "consumo_directo_BL": 3.6, "consumo_indirecto_BL": 0.4,
      "renovable_pct": 92.0, "replenish_pct": 10.0,
      "tipo_medicion": "proyeccion", "region": "global",
      "agua_por_query_ml": None, "fuente": "Proyección propia",
      "es_proyeccion": True, "notas": "Growth driven by Llama 3/4 and AI inference" },
    { "año": 2026, "trimestre": "proj", "empresa": "Meta", "consumo_total_BL": 5.5,
      "consumo_directo_BL": 5.0, "consumo_indirecto_BL": 0.5,
      "renovable_pct": 95.0, "replenish_pct": 20.0,
      "tipo_medicion": "proyeccion", "region": "global",
      "agua_por_query_ml": None, "fuente": "Proyección propia",
      "es_proyeccion": True, "notas": "Meta water restoration goal 2030" },

    # === AGUA POR QUERY (Li et al. 2023) ===
    { "año": 2022, "trimestre": "Q4", "empresa": "ChatGPT(GPT-3)", "consumo_total_BL": None,
      "consumo_directo_BL": None, "consumo_indirecto_BL": None,
      "renovable_pct": None, "replenish_pct": None,
      "tipo_medicion": "por_query", "region": "global",
      "agua_por_query_ml": 500.0, "fuente": "Li et al. 2023 (arXiv:2304.03271)",
      "es_proyeccion": False, "notas": "500ml por conversación (5-50 preguntas). ~10-100ml por query." },
    { "año": 2023, "trimestre": "Q1", "empresa": "GPT-4", "consumo_total_BL": None,
      "consumo_directo_BL": None, "consumo_indirecto_BL": None,
      "renovable_pct": None, "replenish_pct": None,
      "tipo_medicion": "por_query", "region": "global",
      "agua_por_query_ml": 300.0, "fuente": "Li et al. 2023 + estimación Epoch AI",
      "es_proyeccion": False, "notas": "Estimación basada en mayor eficiencia de GPT-4" },
    { "año": 2024, "trimestre": "Q3", "empresa": "GPT-4o", "consumo_total_BL": None,
      "consumo_directo_BL": None, "consumo_indirecto_BL": None,
      "renovable_pct": None, "replenish_pct": None,
      "tipo_medicion": "por_query", "region": "global",
      "agua_por_query_ml": 50.0, "fuente": "Epoch AI + IEA Energy and AI 2025",
      "es_proyeccion": False, "notas": "Estimación ajustada: 0.3 Wh → menor consumo agua. Significativamente más eficiente." },
    { "año": 2025, "trimestre": "proj", "empresa": "GPT-5(estimated)", "consumo_total_BL": None,
      "consumo_directo_BL": None, "consumo_indirecto_BL": None,
      "renovable_pct": None, "replenish_pct": None,
      "tipo_medicion": "por_query", "region": "global",
      "agua_por_query_ml": 80.0, "fuente": "Proyección propia",
      "es_proyeccion": True, "notas": "Modelos más grandes pero más eficientes. Estimación conservadora." },

    # === LI ET AL. PROYECCIONES ===
    { "año": 2023, "trimestre": "FY", "empresa": "Global_AI", "consumo_total_BL": 1.5,
      "consumo_directo_BL": 0.5, "consumo_indirecto_BL": 1.0,
      "renovable_pct": 67.0, "replenish_pct": None,
      "tipo_medicion": "proyeccion_global", "region": "global",
      "agua_por_query_ml": None, "fuente": "Li et al. 2023",
      "es_proyeccion": True, "notas": "Estimación global water footprint IA 2023" },
    { "año": 2027, "trimestre": "proj", "empresa": "Global_AI", "consumo_total_BL": 6.6,
      "consumo_directo_BL": 2.2, "consumo_indirecto_BL": 4.4,
      "renovable_pct": 75.0, "replenish_pct": None,
      "tipo_medicion": "proyeccion_global", "region": "global",
      "agua_por_query_ml": None, "fuente": "Li et al. 2023",
      "es_proyeccion": True, "notas": "4.2-6.6B m³ proyección 2027. Rango conservador-alto." },

    # === ENTRENAMIENTO GPT-3 (Li et al.) ===
    { "año": 2020, "trimestre": "Q2", "empresa": "GPT-3_training", "consumo_total_BL": 0.0007,
      "consumo_directo_BL": 0.0007, "consumo_indirecto_BL": 0.0,
      "renovable_pct": None, "replenish_pct": None,
      "tipo_medicion": "entrenamiento_unico", "region": "US",
      "agua_por_query_ml": None, "fuente": "Li et al. 2023",
      "es_proyeccion": False, "notas": "700,000 L evaporados durante entrenamiento de GPT-3 en data centers de Microsoft US" },
]

df_agua = pd.DataFrame(agua_data)
# Sort by año, empresa
df_agua = df_agua.sort_values(["año", "empresa"]).reset_index(drop=True)

# =====================================================================
# 2. energia.csv — Dimensión Energía (Pregunta P2)
# =====================================================================
# Columnas:
#   año, trimestre, tipo, valor_TWh, escenario, region, fuente,
#   empresa, emisiones_CO2_Mt, queries_diarias_M, Wh_por_query,
#   es_proyeccion, notas
# =====================================================================

energia_data = [
    # === IEA GLOBAL DATA CENTER ENERGY ===
    # Fuente: IEA Energy and AI 2025
    { "año": 2015, "trimestre": "FY", "tipo": "data_centers_global", "valor_TWh": 200,
      "escenario": "historico", "region": "global",
      "fuente": "IEA Energy and AI 2025", "empresa": "Global",
      "emisiones_CO2_Mt": 120.0, "queries_diarias_M": None, "Wh_por_query": None,
      "es_proyeccion": False, "notas": "Baseline pre-IA" },
    { "año": 2020, "trimestre": "FY", "tipo": "data_centers_global", "valor_TWh": 260,
      "escenario": "historico", "region": "global",
      "fuente": "IEA Energy and AI 2025", "empresa": "Global",
      "emisiones_CO2_Mt": 150.0, "queries_diarias_M": None, "Wh_por_query": None,
      "es_proyeccion": False, "notas": "~1% global electricity" },
    { "año": 2022, "trimestre": "FY", "tipo": "data_centers_global", "valor_TWh": 340,
      "escenario": "historico", "region": "global",
      "fuente": "IEA Energy and AI 2025", "empresa": "Global",
      "emisiones_CO2_Mt": 180.0, "queries_diarias_M": None, "Wh_por_query": None,
      "es_proyeccion": False, "notas": "" },
    { "año": 2023, "trimestre": "FY", "tipo": "data_centers_global", "valor_TWh": 380,
      "escenario": "historico", "region": "global",
      "fuente": "IEA Energy and AI 2025", "empresa": "Global",
      "emisiones_CO2_Mt": 200.0, "queries_diarias_M": None, "Wh_por_query": None,
      "es_proyeccion": False, "notas": "" },
    { "año": 2024, "trimestre": "FY", "tipo": "data_centers_global", "valor_TWh": 415,
      "escenario": "historico", "region": "global",
      "fuente": "IEA Energy and AI 2025", "empresa": "Global",
      "emisiones_CO2_Mt": 210.0, "queries_diarias_M": None, "Wh_por_query": None,
      "es_proyeccion": False, "notas": "1.5% global electricity. 415 TWh verified by IEA." },
    { "año": 2025, "trimestre": "proj", "tipo": "data_centers_global", "valor_TWh": 500,
      "escenario": "base", "region": "global",
      "fuente": "IEA Energy and AI 2025", "empresa": "Global",
      "emisiones_CO2_Mt": 240.0, "queries_diarias_M": None, "Wh_por_query": None,
      "es_proyeccion": True, "notas": "Base case ~20% growth YoY" },
    { "año": 2026, "trimestre": "proj", "tipo": "data_centers_global", "valor_TWh": 550,
      "escenario": "base", "region": "global",
      "fuente": "IEA Energy and AI 2025", "empresa": "Global",
      "emisiones_CO2_Mt": 260.0, "queries_diarias_M": None, "Wh_por_query": None,
      "es_proyeccion": True, "notas": "Base case" },
    { "año": 2027, "trimestre": "proj", "tipo": "data_centers_global", "valor_TWh": 650,
      "escenario": "base", "region": "global",
      "fuente": "IEA Energy and AI 2025", "empresa": "Global",
      "emisiones_CO2_Mt": 300.0, "queries_diarias_M": None, "Wh_por_query": None,
      "es_proyeccion": True, "notas": "Base case" },
    { "año": 2028, "trimestre": "proj", "tipo": "data_centers_global", "valor_TWh": 746,
      "escenario": "base", "region": "global",
      "fuente": "IEA Energy and AI 2025", "empresa": "Global",
      "emisiones_CO2_Mt": 330.0, "queries_diarias_M": None, "Wh_por_query": None,
      "es_proyeccion": True, "notas": "Base case" },
    { "año": 2029, "trimestre": "proj", "tipo": "data_centers_global", "valor_TWh": 838,
      "escenario": "base", "region": "global",
      "fuente": "IEA Energy and AI 2025", "empresa": "Global",
      "emisiones_CO2_Mt": 360.0, "queries_diarias_M": None, "Wh_por_query": None,
      "es_proyeccion": True, "notas": "Base case" },
    { "año": 2030, "trimestre": "proj", "tipo": "data_centers_global", "valor_TWh": 945,
      "escenario": "base", "region": "global",
      "fuente": "IEA Energy and AI 2025", "empresa": "Global",
      "emisiones_CO2_Mt": 400.0, "queries_diarias_M": None, "Wh_por_query": None,
      "es_proyeccion": True, "notas": "Base case. 3% global electricity. ~doubles from 2024." },
    { "año": 2035, "trimestre": "proj", "tipo": "data_centers_global", "valor_TWh": 1200,
      "escenario": "base", "region": "global",
      "fuente": "IEA Energy and AI 2025", "empresa": "Global",
      "emisiones_CO2_Mt": 500.0, "queries_diarias_M": None, "Wh_por_query": None,
      "es_proyeccion": True, "notas": "Base case 2035" },

    # === IEA LIFT-OFF SCENARIO ===
    { "año": 2030, "trimestre": "proj", "tipo": "data_centers_global", "valor_TWh": 1400,
      "escenario": "lift_off", "region": "global",
      "fuente": "IEA Energy and AI 2025", "empresa": "Global",
      "emisiones_CO2_Mt": 580.0, "queries_diarias_M": None, "Wh_por_query": None,
      "es_proyeccion": True, "notas": "Lift-off: AI breakthroughs accelerate adoption" },
    { "año": 2035, "trimestre": "proj", "tipo": "data_centers_global", "valor_TWh": 1700,
      "escenario": "lift_off", "region": "global",
      "fuente": "IEA Energy and AI 2025", "empresa": "Global",
      "emisiones_CO2_Mt": 700.0, "queries_diarias_M": None, "Wh_por_query": None,
      "es_proyeccion": True, "notas": "Lift-off 2035" },

    # === IEA AI-FOCUSED ENERGY ===
    { "año": 2024, "trimestre": "FY", "tipo": "ai_focused_global", "valor_TWh": 50,
      "escenario": "base", "region": "global",
      "fuente": "IEA Energy and AI 2025", "empresa": "Global",
      "emisiones_CO2_Mt": 25.0, "queries_diarias_M": None, "Wh_por_query": None,
      "es_proyeccion": False, "notas": "AI-dedicated portion of DC energy" },
    { "año": 2030, "trimestre": "proj", "tipo": "ai_focused_global", "valor_TWh": 465,
      "escenario": "base", "region": "global",
      "fuente": "IEA Energy and AI 2025", "empresa": "Global",
      "emisiones_CO2_Mt": 190.0, "queries_diarias_M": None, "Wh_por_query": None,
      "es_proyeccion": True, "notas": "AI energy could surpass total DC energy of 2024" },

    # === US SHARE ===
    { "año": 2024, "trimestre": "FY", "tipo": "data_centers_US", "valor_TWh": 187,
      "escenario": "historico", "region": "US",
      "fuente": "IEA Energy and AI 2025", "empresa": "Global",
      "emisiones_CO2_Mt": 90.0, "queries_diarias_M": None, "Wh_por_query": None,
      "es_proyeccion": False, "notas": "US = 45% of global data center energy" },

    # === GOOGLE ENERGY ===
    { "año": 2024, "trimestre": "FY", "tipo": "empresa_energia", "valor_TWh": 25.0,
      "escenario": "historico", "region": "global",
      "fuente": "Google Environmental Report 2025", "empresa": "Google",
      "emisiones_CO2_Mt": 5.0, "queries_diarias_M": None, "Wh_por_query": None,
      "es_proyeccion": False, "notas": "Google total electricity consumption" },

    # === MICROSOFT ENERGY ===
    { "año": 2024, "trimestre": "FY", "tipo": "empresa_energia", "valor_TWh": 30.0,
      "escenario": "historico", "region": "global",
      "fuente": "Microsoft ESG Report 2025", "empresa": "Microsoft",
      "emisiones_CO2_Mt": 11.7, "queries_diarias_M": None, "Wh_por_query": None,
      "es_proyeccion": False, "notas": "11.7 Mt CO₂ estimated for 2024" },

    # === META ENERGY ===
    { "año": 2024, "trimestre": "FY", "tipo": "empresa_energia", "valor_TWh": 14.0,
      "escenario": "historico", "region": "global",
      "fuente": "Meta Sustainability Data Index", "empresa": "Meta",
      "emisiones_CO2_Mt": 5.8, "queries_diarias_M": None, "Wh_por_query": None,
      "es_proyeccion": False, "notas": "5.8 Mt CO₂ in 2023. 2024 estimated higher." },

    # === AMAZON CO₂ EMISSIONS ===
    { "año": 2019, "trimestre": "FY", "tipo": "empresa_emisiones", "valor_TWh": None,
      "escenario": "historico", "region": "global",
      "fuente": "Amazon Sustainability Report", "empresa": "Amazon",
      "emisiones_CO2_Mt": 51.8, "queries_diarias_M": None, "Wh_por_query": None,
      "es_proyeccion": False, "notas": "Baseline" },
    { "año": 2020, "trimestre": "FY", "tipo": "empresa_emisiones", "valor_TWh": None,
      "escenario": "historico", "region": "global",
      "fuente": "Amazon Sustainability Report", "empresa": "Amazon",
      "emisiones_CO2_Mt": 60.6, "queries_diarias_M": None, "Wh_por_query": None,
      "es_proyeccion": False, "notas": "" },
    { "año": 2021, "trimestre": "FY", "tipo": "empresa_emisiones", "valor_TWh": None,
      "escenario": "historico", "region": "global",
      "fuente": "Amazon Sustainability Report", "empresa": "Amazon",
      "emisiones_CO2_Mt": 72.6, "queries_diarias_M": None, "Wh_por_query": None,
      "es_proyeccion": False, "notas": "Peak emissions (pandemic+cloud growth)" },
    { "año": 2022, "trimestre": "FY", "tipo": "empresa_emisiones", "valor_TWh": None,
      "escenario": "historico", "region": "global",
      "fuente": "Amazon Sustainability Report", "empresa": "Amazon",
      "emisiones_CO2_Mt": 70.8, "queries_diarias_M": None, "Wh_por_query": None,
      "es_proyeccion": False, "notas": "" },
    { "año": 2023, "trimestre": "FY", "tipo": "empresa_emisiones", "valor_TWh": None,
      "escenario": "historico", "region": "global",
      "fuente": "Amazon Sustainability Report", "empresa": "Amazon",
      "emisiones_CO2_Mt": 68.2, "queries_diarias_M": None, "Wh_por_query": None,
      "es_proyeccion": False, "notas": "" },
    { "año": 2024, "trimestre": "FY", "tipo": "empresa_emisiones", "valor_TWh": None,
      "escenario": "historico", "region": "global",
      "fuente": "Amazon Sustainability Report", "empresa": "Amazon",
      "emisiones_CO2_Mt": 65.1, "queries_diarias_M": None, "Wh_por_query": None,
      "es_proyeccion": False, "notas": "-10% from peak due to renewable investments" },

    # === CHATGPT ENERGY PER QUERY ===
    # Epoch AI / IEA Energy and AI 2025 — GPT-4o: ~0.3 Wh per typical query
    { "año": 2023, "trimestre": "Q1", "tipo": "Wh_por_query", "valor_TWh": None,
      "escenario": "estimado", "region": "global",
      "fuente": "Epoch AI / IEA Energy and AI 2025", "empresa": "ChatGPT(GPT-3.5)",
      "emisiones_CO2_Mt": None, "queries_diarias_M": 100.0, "Wh_por_query": 3.0,
      "es_proyeccion": False, "notas": "GPT-3.5: ~3 Wh per query (cifra comúnmente citada)" },
    { "año": 2024, "trimestre": "Q3", "tipo": "Wh_por_query", "valor_TWh": None,
      "escenario": "estimado", "region": "global",
      "fuente": "Epoch AI / IEA Energy and AI 2025", "empresa": "ChatGPT(GPT-4o)",
      "emisiones_CO2_Mt": None, "queries_diarias_M": 500.0, "Wh_por_query": 0.3,
      "es_proyeccion": False, "notas": "GPT-4o: ~0.3 Wh per query (10x mejora!). 500M queries/día." },
    { "año": 2024, "trimestre": "Q3", "tipo": "Wh_por_query", "valor_TWh": None,
      "escenario": "estimado", "region": "global",
      "fuente": "Epoch AI / IEA Energy and AI 2025", "empresa": "Meta_Llama_3.1_405B",
      "emisiones_CO2_Mt": None, "queries_diarias_M": None, "Wh_por_query": 0.57,
      "es_proyeccion": False, "notas": "Llama 3.1 405B: ~0.57 Wh per query" },
    { "año": 2024, "trimestre": "Q3", "tipo": "Wh_por_query", "valor_TWh": None,
      "escenario": "estimado", "region": "global",
      "fuente": "Epoch AI / IEA Energy and AI 2025", "empresa": "Gemini_Ultra",
      "emisiones_CO2_Mt": None, "queries_diarias_M": None, "Wh_por_query": 1.5,
      "es_proyeccion": False, "notas": "Gemini Ultra: ~1.5 Wh per query (larger model)" },

    # === GOOGLE SEARCH BASELINE ===
    { "año": 2009, "trimestre": "FY", "tipo": "Wh_por_query", "valor_TWh": None,
      "escenario": "historico", "region": "global",
      "fuente": "Google 2009 estimate", "empresa": "Google_Search",
      "emisiones_CO2_Mt": None, "queries_diarias_M": None, "Wh_por_query": 0.3,
      "es_proyeccion": False, "notas": "Google search: ~0.3 Wh per query (2009) — mismo que GPT-4o!" },
]

df_energia = pd.DataFrame(energia_data)
df_energia = df_energia.sort_values(["año", "tipo"]).reset_index(drop=True)

# =====================================================================
# 3. memoria.csv — Dimensión Memoria (Pregunta P3)
# =====================================================================
# Columnas:
#   año, trimestre, tipo_memoria, precio_unitario_USD,
#   mercado_B_USD, tecnologia, fabricante, capacidad_GB,
#   aplicacion, crecimiento_anual_pct, es_proyeccion, notas
# =====================================================================

memoria_data = [
    # === DDR5 Prices (32GB RDIMM) ===
    # Fuente: DRAM market reports + TrendForce
    { "año": 2024, "trimestre": "Q1", "tipo_memoria": "DDR5_32GB_RDIMM", "precio_unitario_USD": 95.0,
      "mercado_B_USD": None, "tecnologia": "DDR5", "fabricante": "Samsung/SK_Hynix/Micron",
      "capacidad_GB": 32, "aplicacion": "datacenter_servers", "crecimiento_anual_pct": None,
      "es_proyeccion": False, "notas": "Q1 2024 spot price" },
    { "año": 2024, "trimestre": "Q3", "tipo_memoria": "DDR5_32GB_RDIMM", "precio_unitario_USD": 108.0,
      "mercado_B_USD": None, "tecnologia": "DDR5", "fabricante": "Samsung/SK_Hynix/Micron",
      "capacidad_GB": 32, "aplicacion": "datacenter_servers", "crecimiento_anual_pct": None,
      "es_proyeccion": False, "notas": "Q3 2024" },
    { "año": 2025, "trimestre": "Q1", "tipo_memoria": "DDR5_32GB_RDIMM", "precio_unitario_USD": 118.0,
      "mercado_B_USD": None, "tecnologia": "DDR5", "fabricante": "Samsung/SK_Hynix/Micron",
      "capacidad_GB": 32, "aplicacion": "datacenter_servers", "crecimiento_anual_pct": 24.0,
      "es_proyeccion": False, "notas": "Q1 2025. +24% YoY" },
    { "año": 2025, "trimestre": "Q2", "tipo_memoria": "DDR5_32GB_RDIMM", "precio_unitario_USD": 130.0,
      "mercado_B_USD": None, "tecnologia": "DDR5", "fabricante": "Samsung/SK_Hynix/Micron",
      "capacidad_GB": 32, "aplicacion": "datacenter_servers", "crecimiento_anual_pct": None,
      "es_proyeccion": False, "notas": "Q2 2025" },
    { "año": 2025, "trimestre": "Q3", "tipo_memoria": "DDR5_32GB_RDIMM", "precio_unitario_USD": 142.0,
      "mercado_B_USD": None, "tecnologia": "DDR5", "fabricante": "Samsung/SK_Hynix/Micron",
      "capacidad_GB": 32, "aplicacion": "datacenter_servers", "crecimiento_anual_pct": None,
      "es_proyeccion": False, "notas": "Q3 2025. +31% desde Q1 2024" },
    { "año": 2025, "trimestre": "Q4", "tipo_memoria": "DDR5_32GB_RDIMM", "precio_unitario_USD": 160.0,
      "mercado_B_USD": None, "tecnologia": "DDR5", "fabricante": "Samsung/SK_Hynix/Micron",
      "capacidad_GB": 32, "aplicacion": "datacenter_servers", "crecimiento_anual_pct": None,
      "es_proyeccion": True, "notas": "Q4 2025 estimated" },
    { "año": 2026, "trimestre": "Q1", "tipo_memoria": "DDR5_32GB_RDIMM", "precio_unitario_USD": 189.0,
      "mercado_B_USD": None, "tecnologia": "DDR5", "fabricante": "Samsung/SK_Hynix/Micron",
      "capacidad_GB": 32, "aplicacion": "datacenter_servers", "crecimiento_anual_pct": 60.0,
      "es_proyeccion": False, "notas": "Q1 2026. +60% YoY. ~2x desde Q1 2024." },
    { "año": 2026, "trimestre": "Q2", "tipo_memoria": "DDR5_32GB_RDIMM", "precio_unitario_USD": 245.0,
      "mercado_B_USD": None, "tecnologia": "DDR5", "fabricante": "Samsung/SK_Hynix/Micron",
      "capacidad_GB": 32, "aplicacion": "datacenter_servers", "crecimiento_anual_pct": None,
      "es_proyeccion": True, "notas": "Q2 2026 (forward estimate $230-260)" },
    { "año": 2026, "trimestre": "Q4", "tipo_memoria": "DDR5_32GB_RDIMM", "precio_unitario_USD": 310.0,
      "mercado_B_USD": None, "tecnologia": "DDR5", "fabricante": "Samsung/SK_Hynix/Micron",
      "capacidad_GB": 32, "aplicacion": "datacenter_servers", "crecimiento_anual_pct": None,
      "es_proyeccion": True, "notas": "Q4 2026 (forward estimate $280-340). 3.3x desde Q1 2024" },

    # === DDR4 Price Spike ===
    { "año": 2025, "trimestre": "Q1", "tipo_memoria": "DDR4_8Gb", "precio_unitario_USD": 1.63,
      "mercado_B_USD": None, "tecnologia": "DDR4", "fabricante": "Samsung/SK_Hynix/Micron",
      "capacidad_GB": 1, "aplicacion": "servers_legacy", "crecimiento_anual_pct": None,
      "es_proyeccion": False, "notas": "Jan 2025 spot price per unit (8Gb die)" },
    { "año": 2025, "trimestre": "Q3", "tipo_memoria": "DDR4_8Gb", "precio_unitario_USD": 5.50,
      "mercado_B_USD": None, "tecnologia": "DDR4", "fabricante": "Samsung/SK_Hynix/Micron",
      "capacidad_GB": 1, "aplicacion": "servers_legacy", "crecimiento_anual_pct": None,
      "es_proyeccion": False, "notas": "Q3 2025" },
    { "año": 2025, "trimestre": "Q4", "tipo_memoria": "DDR4_8Gb", "precio_unitario_USD": 12.76,
      "mercado_B_USD": None, "tecnologia": "DDR4", "fabricante": "Samsung/SK_Hynix/Micron",
      "capacidad_GB": 1, "aplicacion": "servers_legacy", "crecimiento_anual_pct": 683.0,
      "es_proyeccion": False, "notas": "Nov 2025. +683% desde Jan 2025!" },
    { "año": 2026, "trimestre": "Q1", "tipo_memoria": "DDR4_8Gb", "precio_unitario_USD": 10.50,
      "mercado_B_USD": None, "tecnologia": "DDR4", "fabricante": "Samsung/SK_Hynix/Micron",
      "capacidad_GB": 1, "aplicacion": "servers_legacy", "crecimiento_anual_pct": None,
      "es_proyeccion": False, "notas": "Mar 2026. Corrección desde peak" },

    # === HBM Market ===
    # High Bandwidth Memory — clave para NVIDIA GPUs
    { "año": 2023, "trimestre": "FY", "tipo_memoria": "HBM_total_market", "precio_unitario_USD": None,
      "mercado_B_USD": 10.0, "tecnologia": "HBM", "fabricante": "SK_Hynix/Samsung",
      "capacidad_GB": None, "aplicacion": "AI_accelerators", "crecimiento_anual_pct": None,
      "es_proyeccion": False, "notas": "$10B market in 2023" },
    { "año": 2024, "trimestre": "FY", "tipo_memoria": "HBM_total_market", "precio_unitario_USD": None,
      "mercado_B_USD": 18.0, "tecnologia": "HBM", "fabricante": "SK_Hynix/Samsung",
      "capacidad_GB": None, "aplicacion": "AI_accelerators", "crecimiento_anual_pct": 80.0,
      "es_proyeccion": False, "notas": "$17-18B. +80% YoY driven by NVIDIA H100/H200." },
    { "año": 2025, "trimestre": "FY", "tipo_memoria": "HBM_total_market", "precio_unitario_USD": None,
      "mercado_B_USD": 35.0, "tecnologia": "HBM", "fabricante": "SK_Hynix/Samsung/Micron",
      "capacidad_GB": None, "aplicacion": "AI_accelerators", "crecimiento_anual_pct": 94.0,
      "es_proyeccion": False, "notas": "$35B. +94% YoY. Blackwell GB200 demanda masiva." },
    { "año": 2026, "trimestre": "proj", "tipo_memoria": "HBM_total_market", "precio_unitario_USD": None,
      "mercado_B_USD": 55.0, "tecnologia": "HBM", "fabricante": "SK_Hynix/Samsung/Micron",
      "capacidad_GB": None, "aplicacion": "AI_accelerators", "crecimiento_anual_pct": 57.0,
      "es_proyeccion": True, "notas": "$54-55B projected. HBM4 expected." },

    # === NVIDIA GPU Pricing ===
    { "año": 2024, "trimestre": "FY", "tipo_memoria": "NVIDIA_H200", "precio_unitario_USD": 30000.0,
      "mercado_B_USD": None, "tecnologia": "HBM3e", "fabricante": "NVIDIA",
      "capacidad_GB": 141, "aplicacion": "AI_training_inference", "crecimiento_anual_pct": None,
      "es_proyeccion": False, "notas": "~$30K/GPU. 141GB HBM3e memory." },
    { "año": 2025, "trimestre": "FY", "tipo_memoria": "NVIDIA_GB200", "precio_unitario_USD": 1000000.0,
      "mercado_B_USD": None, "tecnologia": "HBM3e", "fabricante": "NVIDIA",
      "capacidad_GB": 576, "aplicacion": "AI_training_inference", "crecimiento_anual_pct": None,
      "es_proyeccion": False, "notas": "~$1M por superchip tray (Grace Blackwell). 576GB HBM3e total." },

    # === NVIDIA DATA CENTER REVENUE ===
    { "año": 2023, "trimestre": "FY", "tipo_memoria": "NVIDIA_DC_revenue", "precio_unitario_USD": None,
      "mercado_B_USD": 47.5, "tecnologia": "GPU", "fabricante": "NVIDIA",
      "capacidad_GB": None, "aplicacion": "datacenter_AI", "crecimiento_anual_pct": 217.0,
      "es_proyeccion": False, "notas": "$47.5B datacenter revenue FY24 (ending Jan 2024). +217% YoY." },
    { "año": 2024, "trimestre": "FY", "tipo_memoria": "NVIDIA_DC_revenue", "precio_unitario_USD": None,
      "mercado_B_USD": 115.0, "tecnologia": "GPU", "fabricante": "NVIDIA",
      "capacidad_GB": None, "aplicacion": "datacenter_AI", "crecimiento_anual_pct": 142.0,
      "es_proyeccion": False, "notas": "$115B datacenter revenue FY25. +142% YoY." },
    { "año": 2025, "trimestre": "proj", "tipo_memoria": "NVIDIA_DC_revenue", "precio_unitario_USD": None,
      "mercado_B_USD": 200.0, "tecnologia": "GPU", "fabricante": "NVIDIA",
      "capacidad_GB": None, "aplicacion": "datacenter_AI", "crecimiento_anual_pct": 74.0,
      "es_proyeccion": True, "notas": "~$200B projected FY26. Blackwell ramp." },

    # === AI TRAINING COST ===
    { "año": 2020, "trimestre": "Q2", "tipo_memoria": "training_cost", "precio_unitario_USD": 12.0,
      "mercado_B_USD": None, "tecnologia": "Transformer", "fabricante": "OpenAI",
      "capacidad_GB": None, "aplicacion": "GPT-3_training", "crecimiento_anual_pct": None,
      "es_proyeccion": False, "notas": "GPT-3: ~$12M training cost (175B params)" },
    { "año": 2023, "trimestre": "Q1", "tipo_memoria": "training_cost", "precio_unitario_USD": 100.0,
      "mercado_B_USD": None, "tecnologia": "Transformer", "fabricante": "OpenAI",
      "capacidad_GB": None, "aplicacion": "GPT-4_training", "crecimiento_anual_pct": None,
      "es_proyeccion": False, "notas": "GPT-4: ~$100M estimated (1.8T params)" },
    { "año": 2025, "trimestre": "proj", "tipo_memoria": "training_cost", "precio_unitario_USD": 1000.0,
      "mercado_B_USD": None, "tecnologia": "Next_gen", "fabricante": "OpenAI/Google/Anthropic",
      "capacidad_GB": None, "aplicacion": "GPT-5_training", "crecimiento_anual_pct": None,
      "es_proyeccion": True, "notas": "GPT-5/Next gen: ~$1B+ estimated training cost" },
]

df_memoria = pd.DataFrame(memoria_data)
df_memoria = df_memoria.sort_values(["año", "tipo_memoria"]).reset_index(drop=True)


# =====================================================================
# EXPORTAR CSVs
# =====================================================================
df_agua.to_csv(f"{DATA_DIR}/agua.csv", index=False, encoding="utf-8")
df_energia.to_csv(f"{DATA_DIR}/energia.csv", index=False, encoding="utf-8")
df_memoria.to_csv(f"{DATA_DIR}/memoria.csv", index=False, encoding="utf-8")

print("OK - CSVs generados exitosamente!\n")
print(f"  [agua.csv]    {len(df_agua)} filas x {len(df_agua.columns)} columnas")
print(f"  [energia.csv] {len(df_energia)} filas x {len(df_energia.columns)} columnas")
print(f"  [memoria.csv] {len(df_memoria)} filas x {len(df_memoria.columns)} columnas")
print(f"\n[Directorio] {DATA_DIR}")

# =====================================================================
# VALIDACION RAPIDA
# =====================================================================
print("\n" + "="*60)
print("VALIDACION RAPIDA")
print("="*60)

print("\n--- agua.csv: anios cubiertos ---")
print(sorted(df_agua.iloc[:, 0].unique()))

print("\n--- agua.csv: empresas ---")
print(df_agua["empresa"].unique())

print("\n--- energia.csv: tipos ---")
print(df_energia["tipo"].unique())

print("\n--- energia.csv: escenarios ---")
print(df_energia["escenario"].unique())

print("\n--- memoria.csv: tipos ---")
print(df_memoria["tipo_memoria"].unique())

print("\n--- Null counts ---")
print(f"agua.csv nulls:    {df_agua.isnull().sum().sum()}")
print(f"energia.csv nulls: {df_energia.isnull().sum().sum()}")
print(f"memoria.csv nulls: {df_memoria.isnull().sum().sum()}")

print("\nOK - Validacion completa!")
