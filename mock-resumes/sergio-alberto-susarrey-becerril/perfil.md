# Perfil Profesional de Sergio Alberto Susarrey Becerril

> 📄 **Enlace a mi Resume (Google Docs):** [Pega aquí el enlace público de tu Google Doc](https://docs.google.com/document/d/TU_ID_AQUI/edit?usp=sharing)

---

## 📌 Instrucciones para Sergio
A continuación encontrarás tu experiencia y proyectos redactados en lenguaje narrativo y con datos desordenados. Tu trabajo es leer cada bloque, extraer los logros cuantificables y convertirlos en viñetas (*bullet points*) con la fórmula: **Verbo de acción + Métrica ($Y$) + Tarea/Herramienta ($Z$)** en tu documento de Google Docs de 1 sola página.

---

## 💼 Experiencia Laboral

### 1. Robotics Software Intern — RobotiX Mechatronics
*Junio 2025 – Diciembre 2025 | Monterrey, México*

Me incorporé al equipo de robótica móvil autónoma (AMR) encargado de diseñar vehículos guiados para almacenes y centros de distribución logística. Mi trabajo se centró en la pila de percepción, localización y control de movimiento utilizando ROS 2 (Robot Operating System) y C++ sobre computadoras de procesamiento embebido NVIDIA Jetson. En ese momento, los vehículos presentaban oscilaciones abruptas al navegar por pasillos estrechos con estanterías metálicas y sufrían demoras críticas en el procesamiento de nubes de puntos de sensores LiDAR y cámaras de profundidad.

Diseñé e implementé nodos de percepción multihilo en C++ empleando la librería PCL (Point Cloud Library) y fusioné datos de odometría de ruedas con una unidad de medición inercial (IMU) mediante un Filtro de Kalman Extendido (EKF). Estas optimizaciones redujeron la latencia de procesamiento de percepción de 120 ms a únicamente 24 ms (un incremento del 80% en velocidad de respuesta), permitiendo a los robots elevar su velocidad máxima de navegación segura de 0.8 m/s a 1.5 m/s. La solución redujo los frenados de emergencia innecesarios por falsos obstáculos en un 40%, registrando más de 500 horas acumuladas de pruebas industriales continuas con cero incidentes de colisión.

### 2. Firmware Developer Intern — AutoSens Technologies
*Enero 2025 – Mayo 2025 | Remoto*

En esta empresa fabricante de telemetría y sensores automotrices apoyé en el desarrollo de firmware embebido en C para microcontroladores ARM Cortex-M (familia STM32) conectados a redes vehiculares de alta velocidad. Desarrollé controladores a nivel de registro para la lectura y decodificación de tramas del protocolo CAN Bus 2.0B y diagnósticos vehiculares estándar bajo la norma OBD-II, capturando variables críticas de motor (RPM, temperatura, presión de frenado y consumo volumétrico de gasolina).

Diseñé e implementé un cargador de arranque seguro (*Secure Bootloader*) capaz de realizar actualizaciones de firmware inalámbricas (FOTA) mediante Bluetooth Low Energy (BLE), lo que redujo el tiempo de actualización de software de cada vehículo de 35 minutos conectando cables en taller a solo 3 minutos de transmisión remota. El firmware fue validado en una flotilla experimental de 80 vehículos de transporte comercial, procesando más de 1.2 millones de mensajes CAN sin registrar pérdida de tramas y logrando un consumo de corriente en modo de reposo (*standby*) de apenas 14 microamperios para evitar la descarga de la batería del auto.

---

## 🚀 Proyectos

### 1. MiniRover-Nav: Vehículo Autónomo con Cartographer SLAM y ROS2
*Tecnologías: C++, ROS 2 Humble, Ubuntu Linux, LiDAR 2D, Raspberry Pi 4, STM32*

Construí y programé un robot móvil autónomo a escala 1:10 equipado con tracción en las 4 ruedas, un sensor LiDAR de 360 grados y odometría de precisión coordinada por un microcontrolador STM32 conectado vía UART a una Raspberry Pi 4. Implementé algoritmos de mapeo y localización simultáneos (Cartographer SLAM) y configuré la pila de navegación Nav2 adaptando planificadores de ruta globales ($A^*$) y seguimiento de trayectoria local (*Pure Pursuit*).

El vehículo demostró la capacidad de mapear y navegar de forma 100% autónoma en recintos interiores cerrados de hasta 150 metros cuadrados, logrando una precisión posicional milimétrica con un margen de error menor a 2.5 centímetros frente a medidas reales de terreno. En pruebas de evasión de obstáculos móviles imprevistos, el sistema recalculó rutas alternativas completando los circuitos en un 30% menos tiempo que las maniobras operadas manualmente.

### 2. AeroStabilize: Controlador de Vuelo para Cuadricóptero en Bare-Metal C
*Tecnologías: C, STM32F4, FreeRTOS, I2C, SPI, PWM, Filtros Complementarios*

Diseñé y programé desde cero el firmware de control de vuelo para un dron cuadricóptero sobre un microcontrolador STM32F401 (ARM Cortex-M4 a 84 MHz) sin recurrir a frameworks prefabricados de drones comerciales. Programé los controladores de periféricos para leer un giroscopio y acelerómetro MPU-6050 vía I2C a alta velocidad, procesando las señales angulares con filtros complementarios para eliminar el ruido de vibración de los motores.

Implementé un lazo de control cerrado con reguladores PID duales en cascada para calcular las correcciones de orientación y modular señales de salida PWM a 400 Hz hacia los variadores electrónicos de velocidad (ESC) de los motores. El bucle de control principal operó a una frecuencia constante y determinista de 500 Hz con un jitter temporal inferior a 12 microsegundos, garantizando la estabilización del dron con una desviación angular máxima de $\pm 1.2$ grados incluso ante ráfagas de viento artificial de hasta 25 km/h.

