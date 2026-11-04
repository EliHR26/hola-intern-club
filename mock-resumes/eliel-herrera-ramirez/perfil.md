# Perfil Profesional de Eliel Herrera Ramírez

> 📄 **Enlace a mi Resume (Google Docs):** [Pega aquí el enlace público de tu Google Doc](https://docs.google.com/document/d/TU_ID_AQUI/edit?usp=sharing)

---

## 📌 Instrucciones para Eliel
A continuación encontrarás tu experiencia y proyectos redactados en lenguaje narrativo y con datos desordenados. Tu trabajo es leer cada bloque, extraer los logros cuantificables y convertirlos en viñetas (*bullet points*) con la fórmula: **Verbo de acción + Métrica ($Y$) + Tarea/Herramienta ($Z$)** en tu documento de Google Docs de 1 sola página.

---

## 💼 Experiencia Laboral

### 1. Game Gameplay & Systems Intern — PixelForge Studios
*Junio 2025 – Diciembre 2025 | Remoto*

Me desempeñé como programador en un estudio independiente de videojuegos enfocado en el desarrollo de un título de acción y rol (ARPG) en Unity con C#. Cuando comencé a colaborar, el juego enfrentaba severos problemas de rendimiento: en niveles con más de 200 enemigos interactuando simultáneamente en pantalla, la tasa de fotogramas caía a 28 FPS y el recolector de basura de C# provocaba congelamientos frecuentes por asignación desmedida de memoria.

Para solucionar esto, diseñé e implementé una arquitectura de reutilización de entidades mediante *Object Pooling* y optimicé el pipeline de renderizado agrupando mallas mediante *Static & Dynamic Batching*, reduciendo las llamadas de dibujado (*draw calls*) en un 65%. Gracias a estas optimizaciones, el juego alcanzó una tasa fluida y estable de 60 FPS en computadoras de gama media y baja (un incremento de rendimiento del 114%), reduciendo el consumo de memoria RAM en un 38%. También programé el sistema de inventario y guardado de partidas serializado en JSON con cifrado AES-256, soportando más de 500 tipos de objetos con tiempos de carga menores a 300 milisegundos durante una prueba beta cerrada con más de 1,200 jugadores en Steam.

### 2. IoT & Embedded Systems Intern — AgroTech Innovations
*Enero 2025 – Mayo 2025 | Querétaro, México*

En esta empresa de tecnología agrícola colaboré en la programación de firmware para dispositivos de campo y sensores ambientales destinados a invernaderos de alta producción. Desarrollé en C++ sobre microcontroladores ESP32 utilizando el sistema operativo de tiempo real FreeRTOS, comunicando sensores de temperatura ambiental, radiación solar y humedad de suelo mediante buses I2C y SPI.

Diseñé un esquema de comunicación telemétrica ligero utilizando el protocolo MQTT con cifrado TLS sobre redes celulares de bajo consumo (LTE-M). Implementé rutinas avanzadas de suspensión profunda (*deep sleep*) para optimizar el consumo eléctrico, lo que extendió la duración de las baterías de los sensores en campo de 3 semanas a más de 8 meses (un incremento de autonomía superior al 900%). El sistema coordinó una red de 140 nodos distribuidos en 5 hectáreas de cultivo, transmitiendo más de 250,000 lecturas diarias a la nube con una tasa de pérdida de paquetes inferior al 0.08%, lo que permitió a los ingenieros agrónomos reducir el desperdicio de agua de riego en un 27%.

---

## 🚀 Proyectos

### 1. ChronoShift: Videojuego 2D con Mecánicas de Manipulación Temporal
*Tecnologías: Godot Engine, C#, GDScript, Aseprite, Git*

Diseñé y programé un videojuego de plataformas y puzles en 2D donde la mecánica central consiste en manipular el flujo temporal de objetos individuales (rebobinar, pausar o acelerar su trayectoria) para resolver acertijos físicos. Implementé el patrón de diseño *Command* y estructuras de datos en *Ring Buffers* circulares optimizados para registrar y reproducir hasta 30 segundos de estados físicos continuos consumiendo menos de 15 MB de memoria volátil.

El videojuego obtuvo el 1er lugar entre 42 proyectos participantes en una Game Jam regional de desarrollo de software. Fue publicado de forma gratuita en la plataforma Itch.io, donde acumuló más de 2,400 descargas únicas y una calificación comunitaria de 4.8 sobre 5 estrellas en sus primeros dos meses.

### 2. SmartFlora: Maceta Automatizada con ESP32 y Telemetría Web
*Tecnologías: C++, PlatformIO, ESP32, WebSockets, HTML5/CSS, Chart.js*

Construí un dispositivo mecatrónico doméstico para el monitoreo y riego inteligente de plantas de interiores. Programé un microcontrolador ESP32 en C++ para coordinar sensores capacitivos de humedad de suelo inmunes a la corrosión y accionar una minibomba peristáltica de precisión para dosificación de nutrientes.

Desarrollé un servidor web asíncrono embebido directamente en la memoria flash del ESP32 con una interfaz en HTML5 y WebSockets que permite a los usuarios calibrar rangos óptimos de hidratación y ver gráficas en vivo desde su teléfono móvil. El sistema mantuvo una exactitud de dosificación de $\pm 2$ ml por ciclo de riego, eliminó el 100% de la mortandad de plantas de prueba durante un periodo de ensayo de 90 días y opera de manera ininterrumpida con un consumo de energía promedio de tan solo 0.45 Watts.

