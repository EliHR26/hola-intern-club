# Perfil Profesional de Abraham Fernández

> 📄 **Enlace a mi Resume (Google Docs):** [Pega aquí el enlace público de tu Google Doc](https://docs.google.com/document/d/TU_ID_AQUI/edit?usp=sharing)

---

## 📌 Instrucciones para Abraham
A continuación encontrarás tu experiencia y proyectos redactados en lenguaje narrativo y con datos desordenados. Tu trabajo es leer cada bloque, extraer los logros cuantificables y convertirlos en viñetas (*bullet points*) con la fórmula: **Verbo de acción + Métrica ($Y$) + Tarea/Herramienta ($Z$)** en tu documento de Google Docs de 1 sola página.

---

## 💼 Experiencia Laboral

### 1. Backend Developer Intern — Finova Solutions (Fintech)
*Junio 2025 – Diciembre 2025 | Remoto*

Estuve apoyando al equipo de infraestructura financiera para modernizar el sistema de procesamiento de pagos y transferencias interbancarias, el cual se saturaba continuamente en días de quincena. Me encargué de colaborar en la migración de varios endpoints críticos de un backend monolítico en Node.js hacia microservicios desarrollados en Go, integrando colas de mensajería con RabbitMQ. 

Gracias a esta reingeniería, logramos reducir el tiempo de respuesta promedio de las transacciones de 1,200 ms a únicamente 180 ms (una mejora de latencia del 85%). Durante la temporada de mayor tráfico del año, el sistema soportó de manera estable un pico de 4,500 transacciones por segundo sin reportar caídas, procesando un volumen total equivalente a \$2.5 millones de dólares. Además, implementé un módulo de monitoreo y alertas automáticas con Prometheus y Grafana que alertaba al equipo ante fallas de red en menos de 30 segundos, reduciendo el tiempo de resolución de incidentes (MTTR) de 45 minutos a solo 8 minutos.

### 2. Software Engineer Intern — LogiTrack Global
*Enero 2025 – Mayo 2025 | Ciudad de México, México*

Entré a apoyar a una empresa dedicada al rastreo de flotas de transporte y envíos de paquetería en tiempo real. La base de datos central en PostgreSQL recibía lecturas GPS continuas y los servidores colapsaban con frecuencia. Diseñé e implementé una estrategia de caché de lectura distribuida utilizando Redis y particionamiento de tablas por rango temporal.

Esta solución disminuyó la carga sobre la base de datos principal en un 60%, logrando que la API de consulta soportara más de 120,000 peticiones diarias manteniendo un uptime del 99.95%. Adicionalmente, me involucré en la cultura de calidad de código: configuré pipelines de integración continua en GitHub Actions y redacté suites de pruebas unitarias e integración en Go, elevando la cobertura de pruebas del proyecto del 40% al 88%, lo que evitó al menos 15 bugs críticos en despliegues a producción.

---

## 🚀 Proyectos

### 1. Mini-S3: Sistema de Almacenamiento Distribuido de Archivos
*Tecnologías: Go, gRPC, Protocol Buffers, Docker*

Diseñé y programé desde cero un sistema de almacenamiento de objetos distribuido inspirado en AWS S3, enfocado en alta disponibilidad y tolerancia a fallos. El sistema fragmenta archivos grandes en chunks de 4 MB y los distribuye con redundancia en 5 nodos de almacenamiento independientes usando gRPC para comunicación de baja latencia.

Implementé una versión ligera del algoritmo de consenso Raft para coordinar los nodos y manejar la elección de líderes ante desconexiones. En pruebas de estrés y benchmarks locales, el cluster sostuvo una tasa de transferencia de lectura de hasta 350 MB/s. Sometí el sistema a pruebas de caos donde desconecté intencionalmente 2 de los 5 nodos en pleno proceso de escritura, logrando una tasa de recuperación y preservación de datos del 100% sin corrupción de archivos.

### 2. GuardGate: API Gateway con Rate Limiting Adaptativo
*Tecnologías: Rust, Redis, Tokio (Async Runtime), Grafana*

Construí un gateway de APIs de alto rendimiento en Rust para mitigar ataques de denegación de servicio (DoS) y proteger servicios web contra abuso de cuotas. Implementé el algoritmo Token Bucket respaldado por Redis para validar y limitar peticiones en tiempo real por IP y por clave de API.

En pruebas de carga con herramientas de benchmarking, el gateway procesó más de 15,000 solicitudes concurrentes por segundo agregando una sobrecarga de latencia minúscula de solo 2.1 milisegundos. El sistema identificó y bloqueó con éxito más de 80,000 solicitudes maliciosas de web-scraping en un periodo de prueba de 48 horas sin arrojar ningún falso positivo sobre usuarios autenticados.

