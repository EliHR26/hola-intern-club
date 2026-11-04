# Perfil Profesional de Luis Torres Ramírez

> 📄 **Enlace a mi Resume (Google Docs):** [Pega aquí el enlace público de tu Google Doc](https://docs.google.com/document/d/TU_ID_AQUI/edit?usp=sharing)

---

## 📌 Instrucciones para Luis
A continuación encontrarás tu experiencia y proyectos redactados en lenguaje narrativo y con datos desordenados. Tu trabajo es leer cada bloque, extraer los logros cuantificables y convertirlos en viñetas (*bullet points*) con la fórmula: **Verbo de acción + Métrica ($Y$) + Tarea/Herramienta ($Z$)** en tu documento de Google Docs de 1 sola página.

---

## 💼 Experiencia Laboral

### 1. Cloud & DevOps Intern — SkyOps Cloud Solutions
*Julio 2025 – Diciembre 2025 | Remoto*

Me incorporé al equipo de operaciones en la nube de una consultora tecnológica para apoyar en la modernización y automatización de la infraestructura de un cliente de comercio electrónico. Antes de mi llegada, los despliegues de software se realizaban de forma manual mediante conexiones SSH a altas horas de la noche; el proceso tardaba hasta 4 horas por lanzamiento y provocaba caídas frecuentes en el servidor. Diseñé e implementé pipelines de integración y entrega continuas (CI/CD) completamente automatizados utilizando GitHub Actions, empaquetado de servicios en Docker y aprovisionamiento declarativo de infraestructura como código (IaC) con Terraform en Amazon Web Services (AWS).

Esta automatización redujo el tiempo total de despliegue de 4 horas a tan solo 7 minutos (una reducción del 97%), permitiendo al equipo de ingeniería pasar de desplegar una vez por semana a realizar hasta 12 despliegues diarios sin tiempos de inactividad (*zero-downtime rolling updates*) sobre clusters en AWS EKS (Kubernetes). Adicionalmente, configuré políticas de escalabilidad automática de pods (HPA) y la adopción estratégica de instancias Spot en AWS para entornos no productivos, logrando recortar los costos mensuales de infraestructura de la empresa en un 34% (un ahorro superior a los \$3,500 USD al mes).

### 2. DevSecOps & Security Analyst Intern — CyberShield Defense
*Enero 2025 – Junio 2025 | Ciudad de México, México*

En esta empresa de ciberseguridad corporativa colaboré en la adopción de prácticas de desarrollo seguro (*Shift-Left Security*). Mi responsabilidad principal fue integrar herramientas automatizadas de análisis de seguridad estático de código (SAST) y análisis de vulnerabilidades en dependencias abiertas (SCA) como SonarQube, Snyk y Trivy dentro del flujo de trabajo de más de 45 repositorios de software de la organización.

Durante mi gestión identifiqué, clasifiqué y coordiné la remediación de 68 vulnerabilidades de criticidad alta y crítica, tales como inyecciones SQL, exposición involuntaria de tokens en commits y dependencias con fallos de ejecución remota de código (RCE). Asimismo, ejecuté auditorías sobre las políticas de control de acceso e identidades (IAM) en cuentas de AWS y Google Cloud, revocando más de 130 permisos y roles sobredimensionados bajo el principio de menor privilegio; estas acciones fueron determinantes para que la compañía acreditara con éxito su auditoría de certificación SOC 2 Tipo II sin registrar hallazgos de incumplimiento.

---

## 🚀 Proyectos

### 1. VaultGuardian: Gestor de Secretos y Variables de Entorno por CLI
*Tecnologías: Go, AES-256-GCM, Argon2id, SQLite, Docker, GitHub Actions*

Diseñé y programé una herramienta de línea de comandos en Go pensada para equipos de software que necesitan compartir variables de entorno seguras (.env) y llaves criptográficas sin enviarlas por canales inseguros de chat. La herramienta cifra los datos localmente en la máquina del usuario empleando encriptación autenticada AES-256 en modo GCM y la función de derivación de claves resistente a ataques por fuerza bruta Argon2id.

El sistema ejecuta operaciones de cifrado y descifrado en menos de 15 milisegundos con una huella de memoria en reposo menor a 10 MB. La herramienta fue distribuida mediante Homebrew y GitHub Releases sumando más de 320 descargas comunitarias, y el código fuente fue auditado con analizadores estáticos de seguridad en Go (gosec) obteniendo una tasa de cero vulnerabilidades reportadas.

### 2. SentinelWatch: Honeypot y Sistema de Detección de Intrusos
*Tecnologías: Python, Elasticsearch, Kibana, Docker, Linux, Bash*

Construí un señuelo digital interactivo (*Honeypot*) en Python desplegado en instancias VPS públicas con el propósito de recolectar y analizar en tiempo real patrones de ciberataques y escaneos de puertos no autorizados emulando servicios vulnerables de SSH, Telnet y HTTP. Diseñé un pipeline que procesa los registros de eventos y los indexa inmediatamente en Elasticsearch para su visualización forense en paneles de control de Kibana.

A lo largo de un ensayo de 60 días en la red pública de internet, el sistema capturó y analizó más de 450,000 intentos de intrusión y fuerza bruta originados por más de 12,000 direcciones IP maliciosas únicas en todo el mundo. El monitor de alertas automáticas notificó intentos de explotación de vulnerabilidades conocidas con una latencia de detección inferior a 1 segundo desde la primera petición maliciosa.

