# 🚀 Misión: Creando tu Primer Tech Resume (CV de Impacto)

¡Bienvenidos a la actividad de creación de Resume del **Intern Club**! 

Aunque estés en primer semestre y sientas que aún no tienes proyectos gigantes o experiencia profesional real, **aprender a redactar y estructurar un CV técnico de impacto es una de las habilidades más valiosas que aprenderás en la universidad**.

---

## 🎯 El Objetivo de la Dinámica

En la carpeta con tu nombre encontrarás un archivo llamado `perfil.md`. En él te hemos asignado una **historia ficticia profesional**:
- **2 Experiencias Laborales**
- **2 Proyectos Técnicos**

Todo está redactado en forma de **narrativa y párrafos informales con estadísticas y métricas sueltas**. 

> **Tu misión:** Tomar esa información "cruda", analizar los datos clave y transformarla en un **Resume profesional en Google Docs de 1 página** con viñetas (*bullet points*) usando la **Fórmula de Google (XYZ)**.

---

## 🧠 La Fórmula de Google (Fórmula X-Y-Z)

Los reclutadores de empresas como Google, Microsoft o Meta revisan un CV en promedio durante **6 a 10 segundos**. No leen párrafos largos; buscan viñetas concretas.

La estructura ganadora para cada viñeta es:

$$\text{Logré } [X] \text{ medido por } [Y] \text{ haciendo } [Z]$$

- **$X$ (Acción / Resultado):** ¿Qué lograste o qué construiste? (Empieza siempre con un verbo de acción en pasado o presente).
- **$Y$ (Métrica cuantitativa):** ¿Cómo se mide el impacto? (Porcentajes, número de usuarios, milisegundos de latencia, dinero ahorrado, transacciones).
- **$Z$ (Cómo lo hiciste / Tecnologías):** ¿Qué herramientas, algoritmos o métodos utilizaste?

### ❌ Ejemplo débil (Como te lo da la vida o el perfil):
> *"Trabajé en el backend de la tienda y la hice más rápida porque optimicé la base de datos con Redis para que no se cayera en las ventas."*

### ✅ Ejemplo de impacto (Como debe quedar en tu Resume):
> *"Optimicé el tiempo de respuesta del catálogo en un 42% para más de 50,000 usuarios activos mediante la implementación de una capa de caché distribuida en Redis y PostgreSQL."*

### 🌟 Carpeta de Ejemplo Oficial
Si tienes dudas de cómo debe verse el resultado final, revisa la carpeta:
👉 [`mock-resumes/diego-lopez-magdaleno/perfil.md`](diego-lopez-magdaleno/perfil.md)  
Allí encontrarás el ejemplo real de Diego con su historia desglosada y el enlace a su **Google Doc de referencia**.

---

## 📋 Paso a Paso para la Actividad

### Paso 1: Encuentra tu archivo
Entra a la carpeta `mock-resumes/` y abre tu carpeta personal (ejemplo: `mock-resumes/eliel-herrera-ramirez/perfil.md`).

### Paso 2: Copia la plantilla oficial en Google Docs
1. Abre el enlace de la plantilla de Diego:  
   👉 **[Plantilla Oficial de Resume (Google Docs)](https://docs.google.com/document/d/1_mGQMc4xqCYAR6NgnCKkmIWuabkVmtUe/edit?usp=sharing&ouid=114020372992344974090&rtpof=true&sd=true)**
2. En el menú superior de Google Docs, ve a **Archivo (File) > Hacer una copia (Make a copy)** y guárdalo en tu propio Google Drive con el nombre `Resume - Tu Nombre`.
3. Al usar esta plantilla ya tienes el formato, fuentes, espaciados y márgenes profesionales listos. Recuerda mantener estas reglas de oro:
   - **Máximo 1 página** (imprescindible: no te pases a una segunda hoja).
   - Sin fotografía (estándar internacional de la industria tech).
   - Reemplaza las secciones con tus datos ficticios y reales:
     1. **Header:** Tu nombre completo (arriba), datos de contacto, enlaces a tu GitHub y LinkedIn.
     2. **Educación:** Universidad, carrera (*Ingeniería en Software / Computación*), fecha esperada de graduación.
     3. **Experiencia Laboral:** Tus 2 puestos asignados en tu `perfil.md` adaptados a viñetas XYZ.
     4. **Proyectos:** Tus 2 proyectos asignados adaptados a viñetas XYZ.
     5. **Habilidades Técnicas:** Lenguajes de programación, librerías, bases de datos y herramientas.

### Paso 3: Extrae las métricas y redacta tus viñetas
Revisa tu `perfil.md`. Encuentra los números (usuarios, porcentajes de optimización, volumen de datos) y conviértelos en viñetas directas y contundentes con verbos de acción:
- *Desarrollé, Diseñé, Implementé, Automaticé, Reduje, Incrementé, Orquesté, Lideré, Migré, Optimicé.*

### Paso 4: Obtén el enlace de tu Google Doc
1. En Google Docs, da clic en el botón azul **Compartir** (arriba a la derecha).
2. En "Acceso general", cambia a: **Cualquier persona con el enlace** en modo **Lector**.
3. Copia el enlace.

### Paso 5: Pega el enlace en tu `perfil.md`
Abre tu `perfil.md` en tu editor, ve a la primera línea y reemplaza el enlace de ejemplo con el enlace real a tu Google Doc:
```markdown
> 📄 **Enlace a mi Resume (Google Docs):** [Ver mi Resume en Google Docs](https://docs.google.com/document/d/TU_ID_DE_DOCUMENTO/edit?usp=sharing)
```

### Paso 6: Haz Commit y Push
Guarda tu archivo, abre tu terminal (o la pestaña de Git en VS Code) y envía tus cambios:
```bash
git add mock-resumes/tu-nombre-apellido/perfil.md
git commit -m "Agrego enlace de mi mock resume en Google Docs"
git push origin tu-rama
```
Por último, abre tu **Pull Request** en GitHub para revisión y retroalimentación. ¡A romperla! 🚀

