# Perfil Profesional de Danna Paola Pedrín Cabrales

> 📄 **Enlace a mi Resume (Google Docs):** [Pega aquí el enlace público de tu Google Doc](https://docs.google.com/document/d/TU_ID_AQUI/edit?usp=sharing)

---

## 📌 Instrucciones para Danna Paola
A continuación encontrarás tu experiencia y proyectos redactados en lenguaje narrativo y con datos desordenados. Tu trabajo es leer cada bloque, extraer los logros cuantificables y convertirlos en viñetas (*bullet points*) con la fórmula: **Verbo de acción + Métrica ($Y$) + Tarea/Herramienta ($Z$)** en tu documento de Google Docs de 1 sola página.

---

## 💼 Experiencia Laboral

### 1. Data Science Intern — MedPulse Analytics (HealthTech)
*Julio 2025 – Diciembre 2025 | Remoto*

Estuve colaborando con el equipo de ciencia de datos en una startup de analítica hospitalaria preventiva orientada a optimizar la atención de pacientes de urgencias. Mi labor principal consistió en construir tuberías de limpieza, ingeniería de características y validación de datos para un repositorio de más de 800,000 registros clínicos anonimizados utilizando Python, Scikit-learn y Polars. Reemplacé scripts lentos de Pandas con procesamiento multihilo en Polars, lo que aceleró la ejecución de los pipelines diarios de 4 horas a tan solo 32 minutos (reducción del 86% en tiempo de cómputo).

Diseñé, entrené y afiné un modelo de clasificación supervisada basado en XGBoost para predecir la probabilidad de que un paciente requiera reingreso a urgencias en un periodo menor a 30 días. El modelo alcanzó un área bajo la curva (ROC-AUC) de 0.89 y una tasa de recall del 83%, superando el sistema tradicional de reglas clínicas en 17 puntos porcentuales. Al implementarse en 4 hospitales piloto, las alertas preventivas del modelo ayudaron a los médicos a intervenir tempranamente, reduciendo las readmisiones imprevistas en un 14%.

### 2. Data Analyst Intern — RetailX Insights
*Enero 2025 – Junio 2025 | Monterrey, México*

En esta firma de consultoría de negocios apoyé en la estructuración de métricas comerciales para una cadena de supermercados con más de 60 sucursales a nivel regional. Escribí consultas analíticas complejas en SQL sobre almacenes de datos en Google BigQuery y PostgreSQL utilizando subconsultas correlacionadas, funciones de ventana (*window functions*) y Common Table Expressions (CTEs) para procesar millones de transacciones de puntos de venta.

Diseñé tableros analíticos interactivos en Power BI y Tableau consultados diariamente por más de 50 directores y gerentes de tienda. A través del análisis de series de tiempo, detecté cuellos de botella y desabastos cíclicos en inventarios de productos perecederos; estas conclusiones permitieron a la gerencia ajustar los pedidos semanales, reduciendo la merma en un 22% y generando un ahorro financiero estimado de \$320,000 MXN en un solo semestre. También automaticé mediante scripts en Python la extracción y envío de reportes matutinos, ahorrando 12 horas semanales de trabajo manual al equipo.

---

## 🚀 Proyectos

### 1. EcoForecast: Predicción de Calidad del Aire con Deep Learning
*Tecnologías: Python, PyTorch, LSTM, Pandas, NumPy, Matplotlib*

Diseñé e implementé un modelo predictivo de series temporales con redes neuronales recurrentes (LSTM) para pronosticar las concentraciones de contaminantes ambientales ($PM_{2.5}$ y $PM_{10}$) con 24 horas de anticipación en zonas urbanas de alta densidad. Recolecté y procesé más de 1.5 millones de lecturas horarias de sensores atmosféricos y variables meteorológicas (viento, humedad, temperatura) provenientes de APIs gubernamentales abiertas de los últimos 5 años.

Tras la optimización de hiperparámetros y regularización contra sobreajuste, el modelo alcanzó un Error Absoluto Medio (MAE) de solo 3.4 puntos en la escala de calidad del aire ($AQI$). El algoritmo superó la precisión de los métodos convencionales de promedio móvil autorregresivo (ARIMA) en un 24%, permitiendo generar alertas de contingencia ambiental con hasta 18 horas de ventaja operativa.

### 2. SmartCart: Sistema Híbrido de Recomendación para E-Commerce
*Tecnologías: Python, FastAPI, Scikit-learn, FastText, Redis, Docker*

Construí un microservicio de recomendaciones personalizadas de productos combinando técnicas de filtrado colaborativo basado en descomposición en valores singulares (SVD) con filtrado basado en contenido mediante embeddings semánticos de texto (FastText). El sistema calcula similitudes de coseno en tiempo real entre el historial del usuario y el catálogo de artículos.

Sometí el modelo a evaluaciones con el dataset de referencia MovieLens y un catálogo sintético de 20,000 productos, logrando un incremento del 26% en el Rango Recíproco Medio (Mean Reciprocal Rank - MRR) frente a métodos de recomendación estática por popularidad. Empaqueté la API REST con FastAPI y Docker, integrando una capa de caché en Redis para lograr tiempos de respuesta en el percentil 99 ($p99$) menores a 35 milisegundos ante tráfico concurrente.

