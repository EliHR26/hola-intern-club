# La Playlist del Intern Club

Convertir la playlist del salon en una pequena aplicacion funcional, en parejas, usando Git y GitHub.

---

## Organizacion del proyecto

Este directorio contiene todo lo necesario para la actividad de hoy:

- `playlist.py`: La lista de canciones (`PLAYLIST`). Cada cancion es un diccionario con `titulo`, `artista`, `genero` y `duracion_segundos`. Aqui cada quien agregara sus canciones favoritas.
- `funciones.py`: Modulo con las herramientas de analisis y reproduccion. Contiene el ejemplo resuelto (`duracion_total`) y las 5 funciones que los equipos implementaran.
- `main.py`: Script ejecutable que corre la demostracion en consola, muestra el resumen de la playlist y selecciona una cancion al azar.
- `test_playlist.py`: Suite sencilla de pruebas basadas en `assert` para verificar que cada funcion trabaje como se espera.
- `README.md`: Esta guia con las instrucciones completas, flujo de trabajo y agenda.

---

## Guia rapida: Como instalar y ejecutar Python en VS Code

Si aun no tienes Python o VS Code configurados en tu computadora, sigue estos pasos segun tu sistema operativo:

### 1. Instalar Python

#### En Windows:
1. Ve a [python.org/downloads](https://www.python.org/downloads/) y descarga la ultima version de Python 3.
2. Abre el instalador descargado.
3. **Paso critico:** En la primera pantalla, activa la casilla que dice **"Add python.exe to PATH"** (en la parte inferior). Si no la activas, tu terminal no encontrara el comando `python`.
4. Haz clic en **Install Now** y completa la instalacion.
5. Para verificar, abre PowerShell o la Terminal y escribe:
   ```powershell
   python --version
   ```

#### En Mac:
1. Ve a [python.org/downloads/macos/](https://www.python.org/downloads/macos/) y descarga el instalador oficial `.pkg`.
2. Ejecuta el archivo descargado y sigue el asistente hasta finalizar.
3. *(Opcional si usas Homebrew)*: Puedes abrir la Terminal y escribir:
   ```bash
   brew install python
   ```
4. Para verificar, abre la Terminal y escribe:
   ```bash
   python3 --version
   ```

---

### 2. Configurar y ejecutar en Visual Studio Code

1. **Instala la extension de Python:**
   - Abre VS Code.
   - Ve a la pestana de **Extensiones** en la barra lateral izquierda (o presiona `Ctrl+Shift+X` en Windows / `Cmd+Shift+X` en Mac).
   - Busca `Python` (creada por Microsoft) y haz clic en **Install**.

2. **Abre el proyecto:**
   - En el menu superior ve a `File > Open Folder...` (Archivo > Abrir carpeta...).
   - Selecciona la carpeta del repositorio `hola-intern-club`.

3. **Selecciona el interprete de Python:**
   - Presiona `Ctrl+Shift+P` (Windows) o `Cmd+Shift+P` (Mac).
   - Escribe `Python: Select Interpreter` y presiona Enter.
   - Elige la version recomendada de Python 3 instalada en tu equipo.

4. **Como ejecutar tu codigo:**
   - **Opcion recomendada (Terminal integrada de VS Code):**
     1. Abre la terminal con el atajo ``Ctrl + ` `` (o en el menu `Terminal > New Terminal`).
     2. Muevete a la carpeta de la actividad:
        ```bash
        cd intern-club/playlist
        ```
     3. Ejecuta el archivo que desees:
        - En Windows:
          ```powershell
          python main.py
          python test_playlist.py
          ```
        - En Mac:
          ```bash
          python3 main.py
          python3 test_playlist.py
          ```
   - **Opcion directa:** Abre `main.py` y haz clic en el boton de triangulo (**Run Python File**) ubicado en la esquina superior derecha del editor.

> **Nota sobre `__pycache__`:** Al ejecutar tus archivos de Python notaras que se crea automaticamente una carpeta llamada `__pycache__`. Esta carpeta contiene archivos temporales compilados (`.pyc`) para acelerar la ejecucion. **No debe subirse a Git ni a GitHub**, ya esta excluida en el archivo `.gitignore` del proyecto.

---

## Flujo de trabajo en GitHub (Paso a paso)

Trabajaremos en parejas. La regla de oro es: **una pareja, una funcion** (ademas de agregar sus canciones).

1. **Actualiza tu repositorio local:**
   Asegurate de estar en la rama principal y descargar los ultimos cambios:
   ```bash
   git checkout main
   git pull origin main
   ```

2. **Crea una rama de trabajo:**
   Usa la convencion `playlist/<tu-nombre>` (o el nombre de tu pareja):
   ```bash
   git checkout -b playlist/juan-y-maria
   ```

3. **Agrega tus canciones:**
   Abre `playlist.py` y agrega 1 o 2 canciones antes del cierre de la lista `PLAYLIST`, anotando sus nombres en un comentario.

4. **Implementa tu funcion asignada:**
   Abre `funciones.py` y busca la funcion que le toco a tu equipo. Reemplaza el `pass` y escribe tu solucion usando ciclos `for` basicos y condicionales `if`.

5. **Prueba tu codigo:**
   Abre `test_playlist.py`, descomenta la importacion y la prueba de tu funcion, y ejecuta:
   ```bash
   python3 test_playlist.py
   ```
   Tambien puedes probar el flujo completo con:
   ```bash
   python3 main.py
   ```

6. **Haz commit y push:**
   Guarda tus cambios y subelos a GitHub:
   ```bash
   git add playlist.py funciones.py test_playlist.py
   git commit -m "Implementa funcion filtrar_por_genero y agrega canciones de Juan y Maria"
   git push origin playlist/juan-y-maria
   ```

7. **Abre un Pull Request (PR):**
   Entra a GitHub, abre un PR apuntando hacia `main` y describe que funcion implementaron y que canciones sumaron.

8. **Revision cruzada (Code Review):**
   Revisa el PR de otra pareja, deja al menos un comentario constructivo o felicitacion en su codigo, y espera aprobacion antes de hacer merge.

---

## Menu de funciones

A continuacion se detallan las 6 funciones del modulo `funciones.py`:

### 1. `duracion_total(playlist)`
- **Que recibe:** `playlist` (lista de diccionarios).
- **Que regresa:** `str` con el formato `'X min Y seg'`.
- **Ejemplo:**
  ```python
  duracion_total(PLAYLIST)
  # Regresa: "10 min 32 seg"
  ```
- *Estado:* Ya implementada por el profesor como ejemplo modelo.

### 2. `filtrar_por_genero(playlist, genero)`
- **Que recibe:** `playlist` (lista de diccionarios) y `genero` (str).
- **Que regresa:** `list` con los diccionarios de las canciones que coinciden exactamente con el genero.
- **Ejemplo:**
  ```python
  filtrar_por_genero(PLAYLIST, "Rock")
  # Regresa: [{'titulo': 'De Musica Ligera', ...}, {'titulo': 'Rayando el Sol', ...}]
  ```

### 3. `cancion_mas_larga(playlist)`
- **Que recibe:** `playlist` (lista de diccionarios).
- **Que regresa:** `dict` de la cancion con mayor `duracion_segundos`. Si la lista esta vacia, regresa `None`.
- **Ejemplo:**
  ```python
  cancion_mas_larga(PLAYLIST)
  # Regresa: {'titulo': 'Rayando el Sol', 'artista': 'Mana', 'genero': 'Rock', 'duracion_segundos': 251}
  ```

### 4. `buscar_por_artista(playlist, artista)`
- **Que recibe:** `playlist` (lista de diccionarios) y `artista` (str).
- **Que regresa:** `list` con todas las canciones creadas por ese artista. Si no hay coincidencias, regresa una lista vacia `[]`.
- **Ejemplo:**
  ```python
  buscar_por_artista(PLAYLIST, "Selena")
  # Regresa: [{'titulo': 'Amor Prohibido', 'artista': 'Selena', 'genero': 'Tex-Mex', 'duracion_segundos': 169}]
  ```

### 5. `mezclar(playlist)`
- **Que recibe:** `playlist` (lista de diccionarios).
- **Que regresa:** `list` nueva con las mismas canciones en orden aleatorio (sin modificar la lista original).
- **Ejemplo:**
  ```python
  mezclar(PLAYLIST)
  # Regresa una nueva lista desordenada
  ```

### 6. `recomendar(playlist, genero)`
- **Que recibe:** `playlist` (lista de diccionarios) y `genero` (str).
- **Que regresa:** `dict` de una cancion seleccionada al azar de ese genero, o `None` si no existe ninguna.
- **Ejemplo:**
  ```python
  recomendar(PLAYLIST, "Rock")
  # Regresa: {'titulo': 'De Musica Ligera', 'artista': 'Soda Stereo', ...}
  ```

---

## Agenda de la clase

- **12:00 - 12:10**: Introduccion a la dinamica, explicacion de la estructura de diccionarios y listas.
- **12:10 - 12:25**: Demostracion en vivo (el profesor explica e implementa `duracion_total`).
- **12:25 - 13:20**: Trabajo en parejas (asignacion de funciones, resolucion de dudas, commits y PRs).
- **13:20 - 13:45**: Integracion en vivo: probar la aplicacion completa con todas las funciones de los alumnos.
- **13:45 - 14:00**: Revision cruzada de codigo (Code Review) y cierre de la sesion.

---

## Retos extra (Stretch challenges)

Si tu equipo termino antes de tiempo, intenten resolver estos dos retos:

1. **Recomendacion con limite de tiempo:** Modifica o crea `recomendar_corta(playlist, genero)` para que unicamente recomiende canciones con una duracion menor a 3 minutos (180 segundos).
2. **Top artistas:** Implementa `top_artistas(playlist)` que cuente cuantas canciones tiene cada artista y regrese el nombre del artista que aparece con mayor frecuencia en la lista.

---

## Como se que ya termine?

Has completado con exito la actividad cuando:
1. Tu rama tiene tus canciones agregadas en `playlist.py`.
2. La funcion asignada a tu pareja esta implementada y documentada en `funciones.py`.
3. Tu Pull Request esta abierto en GitHub con un titulo claro.
4. Las pruebas de tu funcion pasan en `test_playlist.py` (`python3 test_playlist.py`).
5. Dejaste al menos un comentario de revision constructivo en el Pull Request de otra pareja.
