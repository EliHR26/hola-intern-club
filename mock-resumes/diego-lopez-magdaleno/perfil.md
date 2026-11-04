# 🌟 Perfil de Ejemplo Oficial: Diego López Magdaleno

> 📄 **Enlace a mi Resume (Google Docs):** [Ver Resume de Ejemplo de Diego en Google Docs](https://docs.google.com/document/d/1_mGQMc4xqCYAR6NgnCKkmIWuabkVmtUe/edit?usp=sharing&ouid=114020372992344974090&rtpof=true&sd=true)

---

> [!NOTE]
> ### 💡 ¿Cómo usar esta carpeta de ejemplo?
> Chicos de primero: este perfil es su **guía y referencia principal**.
> Aquí abajo verán cómo una experiencia laboral o un proyecto se describe primero como una **historia narrativa con métricas en bruto**, y cómo después se sintetiza en **viñetas de impacto (Fórmula XYZ)** tal como aparece en el [Google Doc oficial](https://docs.google.com/document/d/1_mGQMc4xqCYAR6NgnCKkmIWuabkVmtUe/edit?usp=sharing&ouid=114020372992344974090&rtpof=true&sd=true).

---

## 💼 Experiencia Laboral

### 1. Software Engineering Intern — Meta
*Menlo Park, California | Junio 2026 – Agosto 2026*  
**Enfoque:** Full-stack features for Instagram's logged-out discovery surfaces (`instagram.com/popular`).

#### 📖 La Historia Cruda (Contexto y Estadísticas):
Durante mi pasantía en Meta, me uní al equipo responsable de las superficies web públicas de Instagram para usuarios no autenticados, las cuales reciben un tráfico masivo de más de 3.1 millones de visitantes diarios y más de 199 millones de visualizaciones de página al mes. En este rol me encargué de idear, desarrollar y poner en producción 12 funcionalidades completas a nivel de producto. Para asegurar que ninguna modificación perjudicara la experiencia o las métricas de engagement, diseñé y ejecuté experimentos A/B que acumularon más de 150 millones de exposiciones antes de realizar despliegues masivos, utilizando React/Relay en frontend, Hack/GraphQL en el backend y Dataswarm para orquestación de datos.

Uno de mis mayores retos fue construir desde cero el sistema de *Category Hub* (`/popular/{broad-topic}`). Diseñé todo el flujo end-to-end: configuraciones estáticas, extractores de temas, resolvers de GraphQL, componentes interactivos en React y enrutamiento en Instagram Web con compuertas a nivel de controlador. Esto culminó en el lanzamiento de 54 páginas optimizadas para SEO, captando 2.7 millones de visitas diarias y más de 91 millones de sesiones orgánicas generadas por motores de búsqueda. Además, diseñé un pipeline de curaduría de contenido asistido por IA utilizando el modelo LLaMA 3.3 70B: las categorías semilla pasaban a Hive, Dataswarm activaba inferencias asíncronas para extraer los 5 temas en tendencia y los resultados se almacenaban en caché en TAO Ent con soporte heurístico para contingencias. Por último, re-arquitecturé la página de inicio Galileo con paginación diferida (*lazy scroll*), cuadrículas dinámicas responsivas y modales inmersivos de Reels, alcanzando un incremento de tráfico del +6.6% (390,000 visitas diarias adicionales) en más de 13.6 millones de sesiones únicas.

---

### 2. Software Engineering Intern — Meta
*Menlo Park, California | Junio 2025 – Agosto 2025*  
**Enfoque:** ClinicAll Project & Metrics Core Capabilities Team.

#### 📖 La Historia Cruda (Contexto y Estadísticas):
En mi primer verano en Meta colaboré en dos frentes clave: el desarrollo del sistema ClinicAll y soporte al equipo de Metrics Core Capabilities. Diseñé y construí ClinicAll, una plataforma integral de gestión hospitalaria que requería un control de acceso riguroso; implementé autenticación y autorización basada en roles (RBAC) con Auth0, React en frontend y un backend robusto en Node.js, PostgreSQL y Prisma ORM.

Para la gestión de citas de pacientes, diseñé un sistema de notificaciones en tiempo real utilizando WebSockets con Socket.IO, enrutando los mensajes a través de una cola con prioridades y cron jobs automatizados. Desarrollé también un motor de detección de interacciones farmacológicas para alertar sobre incompatibilidades entre medicamentos y síntomas preexistentes, modelando complejas relaciones muchos-a-muchos mediante una estructura de grafo en base de datos para garantizar consultas ultra-rápidas. Para mejorar la experiencia de los médicos, integré un buscador predictivo *typeahead* conectado a la API de la FDA y a bases de síntomas, incorporando además validaciones inteligentes de interacción. Por último, contribuí directamente en el código base interno de Meta resolviendo bugs y optimizando la confiabilidad de los sistemas de métricas corporativas.

---

## 🚀 Proyectos Principales

### 1. AURA Platform — 1er Lugar Nacional Sempra Infrastructure Hackathon
*Ensenada, B.C. | Enero 2026 – Mayo 2026*  
*Tecnologías: React, TypeScript, Supabase, AI Context Workflows*

#### 📖 La Historia Cruda (Contexto y Estadísticas):
Desarrollé la plataforma AURA, un sistema de gestión de aprendizaje (LMS) especializado en la capacitación de personal industrial en protocolos de prevención de riesgos y seguridad laboral. Utilizando React, TypeScript y Supabase, construí una arquitectura segura con navegación y autenticación controlada por roles de usuario.

El núcleo del proyecto fue un motor interactivo de simulación a pantalla completa para evaluación de riesgos en escenarios virtuales 2D/3D. Los operarios debían inspeccionar la escena e interactuar con puntos de interés (*hotspots*) responsivos colocados estratégicamente; el motor evaluaba su desempeño en tiempo real asignando calificaciones según la conducta y secuencia de decisiones tomada. Además, arquitecturé un flujo de trabajo de colaboración asistido por IA mediante un sistema de contexto basado en archivos estrictos, permitiendo que la IA se mantuviera fiel a las especificaciones técnicas del proyecto, recordara decisiones históricas y ejecutara tareas con alta precisión contextual.

---

### 2. Clash Royale Emote Recognition
*Ensenada, B.C. | Enero 2026 – Febrero 2026*  
*Tecnologías: Python, MediaPipe, OpenCV (CV2), scikit-learn, XGBoost, Random Forest, Joblib*

#### 📖 La Historia Cruda (Contexto y Estadísticas):
Construí un sistema de visión artificial en tiempo real capaz de reconocer y clasificar las icónicas reacciones (emotes) del videojuego Clash Royale mediante el análisis de expresiones faciales y gestos manuales del usuario frente a una cámara web. Utilicé Google MediaPipe para extraer landmarks anatómicos de las manos y blendshapes faciales en vivo, estructurando un dataset propio de 135 características numéricas a partir de señales de movimiento y gestos.

Entrené y ajusté clasificadores de aprendizaje automático supervisado con Random Forest y XGBoost utilizando pipelines de selección de características en scikit-learn, alcanzando una precisión sobresaliente de ~99.99% ROC-AUC en la clasificación multiclase de emotes. Diseñé un pipeline de inferencia reproducible en Python (NumPy, Pandas, scikit-learn) y exporté el modelo entrenado con Joblib para ejecutar predicciones instantáneas y mostrar el emote correspondiente en pantalla usando OpenCV (CV2).

---

## 💡 Cómo se traduce esto al Google Doc (Ejemplo de Bullet Points)

Cuando abras el [Google Doc de Diego](https://docs.google.com/document/d/1_mGQMc4xqCYAR6NgnCKkmIWuabkVmtUe/edit?usp=sharing&ouid=114020372992344974090&rtpof=true&sd=true), notarás cómo los párrafos de arriba se convierten en viñetas directas:

- ❌ **No escribas párrafos largos en el CV:** *"Trabajé en Instagram haciendo páginas de temas y les puse SEO y un modelo de LLaMA..."*
- ✅ **Escribe viñetas concisas con la fórmula XYZ:**
  - *"Built a full-stack Category Hub (/popular/{broad-topic}) system end-to-end (...), launching 54 SEO-optimized pages serving 2.7M daily visits with 91M+ organic search-driven sessions."*
  - *"Re-architected the Galileo (/popular) discovery home with scroll-based lazy pagination, responsive dynamic grids, and immersive reel modals, achieving a +6.6% traffic uplift (390K daily visits) across 13.6M unique sessions."*
