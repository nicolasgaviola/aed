# Jupyter Notebooks en VS Code

Guía completa para usar Jupyter Notebooks dentro de Visual Studio Code con el gestor de entornos `uv`.

---

## ¿Qué es Jupyter Notebook?

Jupyter Notebook es un entorno interactivo que permite combinar código Python, texto con formato (Markdown), ecuaciones y visualizaciones en un mismo documento `.ipynb`. Es ideal para exploración de datos, algoritmos paso a paso y aprendizaje interactivo.

Cada documento se divide en **celdas** que pueden ser:

- **Code**: contienen código Python ejecutable.
- **Markdown**: contienen texto con formato, títulos, listas, fórmulas, etc.

---

## Requisitos previos

### 1. Extensiones de VS Code

Instalar las siguientes extensiones desde el Marketplace de VS Code (ícono de cuadrados en la barra lateral):

| Extensión | ID | Para qué sirve |
|---|---|---|
| **Python** | `ms-python.python` | Soporte general de Python |
| **Jupyter** | `ms-toolsai.jupyter` | Abrir y editar archivos `.ipynb` |

Para instalarlas por terminal:

```bash
code --install-extension ms-python.python
code --install-extension ms-toolsai.jupyter
```

### 2. Dependencias del proyecto (gestionadas con `uv`)

Este proyecto usa `uv` como gestor de entornos y dependencias. Para agregar Jupyter:

```bash
uv add jupyter ipykernel
```

Esto actualiza automáticamente `pyproject.toml` y `uv.lock`.

Para sincronizar el entorno después de clonar el repositorio o actualizar dependencias:

```bash
uv sync
```

---

## Seleccionar el kernel correcto en VS Code

El **kernel** es el intérprete de Python que ejecuta el código en el notebook. Hay que apuntar al entorno virtual creado por `uv` (`.venv`).

1. Abrir un archivo `.ipynb` en VS Code.
2. En la esquina superior derecha del notebook aparece el botón **"Select Kernel"** (o el nombre del kernel actual).
3. Hacer clic → seleccionar **"Python Environments..."**.
4. Elegir el entorno que termina en `.venv` dentro de la carpeta del proyecto.
   - Ejemplo: `.../aed/.venv/bin/python`

> Si el entorno `.venv` no aparece en la lista, ejecutar en terminal `uv sync` y luego recargar la ventana de VS Code con `Ctrl+Shift+P` → "Developer: Reload Window".

---

## Estructura de un notebook `.ipynb`

```
Notebook
├── Celda Markdown  →  Título, descripción, contexto
├── Celda Code      →  import, definiciones, lógica
├── Celda Code      →  pruebas, resultados, prints
└── Celda Markdown  →  Conclusiones o explicación del resultado
```

---

## Atajos de teclado esenciales

### Modo comando (celda seleccionada, borde azul — presionar `Esc`)

| Atajo | Acción |
|---|---|
| `Enter` | Entrar en modo edición |
| `A` | Insertar celda **arriba** (above) |
| `B` | Insertar celda **abajo** (below) |
| `D D` | Eliminar celda seleccionada |
| `M` | Convertir celda a **Markdown** |
| `Y` | Convertir celda a **Code** |
| `Shift+Enter` | Ejecutar celda y pasar a la siguiente |
| `Ctrl+Enter` | Ejecutar celda sin moverse |

### Modo edición (dentro de la celda, borde verde — presionar `Enter`)

| Atajo | Acción |
|---|---|
| `Esc` | Salir a modo comando |
| `Shift+Enter` | Ejecutar celda y bajar |
| `Ctrl+Z` | Deshacer |
| `Tab` | Autocompletar |
| `Shift+Tab` | Ver documentación de función |

---

## Diferencia clave: notebooks vs scripts `.py`

En un script `.py`, `__file__` está disponible y contiene la ruta del archivo. En un notebook Jupyter, **`__file__` no existe**, porque el notebook no es un archivo ejecutado directamente por Python.

**Solución para rutas relativas en notebooks:**

```python
# En lugar de:
# ruta = os.path.join(os.path.dirname(__file__), "archivo.csv")  # ❌ no funciona en notebooks

# Usar:
import os
ruta = os.path.join(os.getcwd(), "archivo.csv")  # ✅ devuelve el directorio de trabajo actual
```

> El directorio de trabajo (`cwd`) en VS Code es la raíz del proyecto cuando se abre la carpeta con `File > Open Folder`.

---

## Flujo de trabajo típico

```bash
# 1. Instalar/actualizar dependencias
uv sync

# 2. Abrir VS Code en la raíz del proyecto
code .

# 3. Abrir un notebook desde el explorador de archivos (panel izquierdo)

# 4. Seleccionar el kernel .venv (solo la primera vez por proyecto)

# 5. Ejecutar celdas con Shift+Enter
```

---

## Buenas prácticas

- Nombrar los notebooks con el formato `modulo_XX_tema.ipynb` (ej: `modulo01_listas.ipynb`).
- Incluir una celda Markdown al inicio con el título y descripción del ejercicio.
- Reiniciar el kernel antes de entregar (`Kernel > Restart & Run All`) para asegurarse de que las celdas corren en orden.
- No depender del orden de ejecución: escribir celdas que funcionen de arriba a abajo.
- Hacer `uv sync` cada vez que se agregue una nueva dependencia para mantener el `uv.lock` actualizado.
