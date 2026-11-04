# Perfil Profesional de Saúl Durán Miranda

> 📄 **Enlace a mi Resume (Google Docs):** [Pega aquí el enlace público de tu Google Doc](https://docs.google.com/document/d/TU_ID_AQUI/edit?usp=sharing)

---

## 📌 Instrucciones para Saúl
A continuación encontrarás tu experiencia y proyectos redactados en lenguaje narrativo y con datos desordenados. Tu trabajo es leer cada bloque, extraer los logros cuantificables y convertirlos en viñetas (*bullet points*) con la fórmula: **Verbo de acción + Métrica ($Y$) + Tarea/Herramienta ($Z$)** en tu documento de Google Docs de 1 sola página.

---

## 💼 Experiencia Laboral

### 1. Mobile App Developer Intern — FastBite Delivery (Logística Urbana)
*Junio 2025 – Diciembre 2025 | Remoto*

Trabajé en una plataforma de entrega de comida a domicilio y logística de última milla con más de 70,000 usuarios activos mensuales. Mi objetivo principal fue optimizar la aplicación móvil multiplataforma utilizada por más de 1,200 repartidores en activo, desarrollada en Flutter y Dart con backend en Firebase y Node.js. La aplicación anterior sufría de un drenado severo de batería y descalibración del tracking GPS en segundo plano, lo que desorientaba los tiempos de entrega y provocaba quejas continuas.

Reescribí el módulo de geolocalización en segundo plano implementando algoritmos de muestreo adaptativo con base en el acelerómetro del dispositivo y filtros de reducción de ruido espacial. Esta solución redujo el consumo de batería de la aplicación en un 35% por turno de trabajo y mejoró la exactitud del tiempo estimado de llegada (ETA) en un 22%. Asimismo, refactoricé el manejo de estados utilizando Riverpod y optimicé el cargado de imágenes en memoria, reduciendo el tiempo de arranque en frío de la aplicación de 3.8 segundos a 1.2 segundos; el sistema procesó más de 22,000 pedidos semanales manteniendo una tasa de sesiones libres de fallos (*crash-free sessions*) del 99.7%.

### 2. Junior Mobile Developer Intern — FinTrack App
*Enero 2025 – Mayo 2025 | Guadalajara, México*

En esta startup fintech enfocada en jóvenes universitarios colaboré en el desarrollo nativo para Android de una aplicación de finanzas personales, presupuestos y registro de gastos. Desarrollé nuevas interfaces de usuario declarativas y reactivas utilizando Kotlin y Jetpack Compose, siguiendo la arquitectura recomendada por Google (MVVM + Clean Architecture).

Implementé una capa de persistencia y sincronización *offline-first* utilizando Room Database y WorkManager de Android Jetpack, permitiendo que los usuarios registren sus transacciones sin conexión a internet y sincronizando los datos de forma automática e imperceptible al detectar conexión de red. Diseñé un panel de estadísticas y presupuestos con gráficos vectoriales interactivos, contribuyendo a que la valoración de la aplicación en Google Play Store aumentara de 3.9 a 4.6 estrellas con base en más de 1,400 reseñas. Adicionalmente, apliqué reglas de optimización con ProGuard/R8 y compresión de activos que redujeron el tamaño total de descarga del APK en un 28% (pasando de 45 MB a 32 MB).

---

## 🚀 Proyectos

### 1. FitPulse: Entrenador Móvil con Visión Artificial en el Dispositivo
*Tecnologías: Flutter, Dart, TensorFlow Lite, MediaPipe, Python*

Diseñé y programé una aplicación móvil de acondicionamiento físico que utiliza la cámara frontal del teléfono inteligente y modelos de visión por computadora embebidos (Pose Estimation) para contar repeticiones de ejercicios corporales (como flexiones y sentadillas) y alertar al usuario sobre desviaciones posturales en tiempo real, todo sin enviar video a la nube para proteger la privacidad.

Optimicé el pipeline de inferencia matemática para ejecutar el modelo a 30 fotogramas por segundo sostenidos en teléfonos inteligentes de gama media con un impacto despreciable de temperatura. En pruebas cuantitativas sobre más de 200 series de repeticiones de ejercicio, el algoritmo demostró una exactitud de conteo del 94%. El proyecto sumó más de 800 descargas durante su fase beta pública distribuida a través de TestFlight y releases directos de APK en GitHub.

### 2. EcoCommute: Carpooling y Movilidad Universitaria Compartida
*Tecnologías: React Native, Expo, Supabase, PostgreSQL, Google Maps API*

Desarrollé una aplicación móvil multiplataforma orientada a comunidades estudiantiles universitarias para compartir viajes en automóvil hacia el campus, reduciendo el tráfico vehicular y los gastos de transporte. Integré la API de Google Maps para el cálculo de rutas óptimas, un sistema de chat en tiempo real con WebSockets de Supabase y un algoritmo para prorratear de manera justa los costos de combustible entre los pasajeros.

La aplicación fue desplegada como piloto en una comunidad estudiantil de 600 universitarios verificados. A lo largo de un semestre académico, la plataforma facilitó con éxito más de 1,800 viajes compartidos, logrando evitar la emisión estimada de 4.2 toneladas de dióxido de carbono ($CO_2$) y alcanzando un índice de satisfacción del usuario del 96% en encuestas de salida.

