# Perfil Profesional de Valentina Ballesteros Morales

> 📄 **Enlace a mi Resume (Google Docs):** [Pega aquí el enlace público de tu Google Doc](https://docs.google.com/document/d/TU_ID_AQUI/edit?usp=sharing)

---

## 📌 Instrucciones para Valentina
A continuación encontrarás tu experiencia y proyectos redactados en lenguaje narrativo y con datos desordenados. Tu trabajo es leer cada bloque, extraer los logros cuantificables y convertirlos en viñetas (*bullet points*) con la fórmula: **Verbo de acción + Métrica ($Y$) + Tarea/Herramienta ($Z$)** en tu documento de Google Docs de 1 sola página.

---

## 💼 Experiencia Laboral

### 1. AI & NLP Engineer Intern — Cognitiva Labs (Sistemas RAG)
*Junio 2025 – Diciembre 2025 | Remoto*

Me desempeñé en el equipo de ingeniería de inteligencia artificial de una startup que desarrolla agentes conversacionales para atención a clientes en corporativos del sector financiero y telecomunicaciones. Mi labor estuvo enfocada en la arquitectura de Recuperación Aumentada por Generación (RAG) construida con Python, LangChain y bases de datos vectoriales en Qdrant. La versión preliminar del asistente sufría de una tasa de alucinaciones (respuestas con datos falsos o imprecisos) del 23% y tardaba en promedio más de 4.5 segundos en responder debido a la búsqueda ineficiente en documentos densos de cientos de páginas.

Para resolver estas limitaciones, reestructuré el pipeline de indexación implementando fragmentación semántica contextual (*semantic chunking*) y un modelo de reclasificación (*re-ranking*) con Cohere. Además, diseñé esquemas de validación estricta de salidas con Pydantic y streaming de respuestas por sockets. Con estas mejoras, logré reducir la tasa de alucinaciones del 23% a solo 2.1% (una disminución de errores de más del 90%) y aceleré el tiempo de respuesta promedio a 1.2 segundos. En producción, el asistente gestionó más de 65,000 interacciones mensuales con una tasa de resolución automática en primer contacto (*First Contact Resolution*) del 79%, liberando más de 180 horas de trabajo mensual a los agentes humanos de soporte.

### 2. Junior Machine Learning Intern — Linguix Analytics
*Enero 2025 – Mayo 2025 | Ciudad de México, México*

En esta empresa especializada en analítica de reputación digital y minería de texto colaboré en el entrenamiento y optimización de modelos de procesamiento de lenguaje natural (NLP) para el análisis de sentimiento multiclase en millones de comentarios de redes sociales y reseñas de e-commerce en español. Trabajé con PyTorch y el ecosistema de Hugging Face Transformers adaptando arquitecturas preentrenadas basadas en BERT (BETO y RoBERTa).

Fine-tuneé y cuantilicé los modelos a precisión entera de 8 bits (INT8) con ONNX Runtime y TensorRT para optimizar su despliegue en servidores en la nube. Esta optimización redujo el peso del modelo en disco en un 60% y triplicó el rendimiento de procesamiento, alcanzando una tasa de inferencia superior a 400 oraciones analizadas por segundo por servidor. La exactitud general de clasificación (F1-score ponderado) aumentó de 0.74 a 0.88, lo que permitió a más de 30 marcas monitoreadas detectar picos de insatisfacción de clientes en tiempo real y responder un 45% más rápido ante incidentes de servicio.

---

## 🚀 Proyectos

### 1. NoteMind: Asistente Inteligente de Síntesis Académica y Flashcards
*Tecnologías: Python, FastAPI, OpenAI Whisper, Claude API, Streamlit, PyMuPDF*

Diseñé y programé una aplicación web pensada para estudiantes universitarios que permite cargar grabaciones de audio de clases presenciales y obtener de manera instantánea transcripciones completas, resúmenes estructurados por temas clave, mapas conceptuales en sintaxis Mermaid y bancos de preguntas de autoevaluación (*flashcards*). Implementé el modelo Whisper de OpenAI para el reconocimiento de voz local sin costo de API y orquesté la generación de síntesis mediante llamadas asíncronas con control de tokens.

La herramienta procesa audios de hasta 2 horas de duración en menos de 90 segundos, alcanzando una precisión de transcripción del 96% en terminología técnica y fórmulas de ingeniería. Durante la temporada de exámenes semestrales, la plataforma fue adoptada por más de 700 estudiantes universitarios, generando y exportando más de 4,000 resúmenes descargables en formatos PDF y Markdown con una tasa de satisfacción superior al 95%.

### 2. CodeScribe: Generador Automatizado de Documentación Técnica
*Tecnologías: Python, AST (Abstract Syntax Tree), LLMs, Click, PyPI, GitHub Actions*

Creé una herramienta de línea de comandos (CLI) en Python distribuida vía PyPI que analiza el árbol sintáctico abstracto (AST) de repositorios de software en Python, JavaScript y Go para deducir tipos, parámetros de entrada, valores de retorno y dependencias de cada función, generando docstrings completos bajo los formatos Google y Sphinx de manera automática.

El paquete superó las 1,800 descargas en PyPI y reunió más de 500 estrellas en su repositorio de GitHub. En pruebas de evaluación sobre 30 repositorios de código abierto con más de 12,000 líneas de código analizadas, la documentación autogenerada obtuvo una tasa de aceptación y conservación sin modificaciones del 91% en revisiones realizadas por desarrolladores humanos.

