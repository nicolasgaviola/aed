# Algoritmos y Estructuras de Datos (AED)

Prácticas de la materia **Algoritmos y Estructuras de Datos** de la Licenciatura en Inteligencia Artificial.

---

## Requisitos

- [Python 3.14+](https://www.python.org/)
- [uv](https://docs.astral.sh/uv/) — gestor de entornos y dependencias
- [Visual Studio Code](https://code.visualstudio.com/) con las extensiones:
  - `ms-python.python`
  - `ms-toolsai.jupyter`

---

## Configuración inicial

```bash
# 1. Clonar el repositorio
git clone <url-del-repo>
cd aed

# 2. Instalar dependencias (crea el entorno virtual .venv automáticamente)
uv sync
```

---

## Ejecutar notebooks

1. Abrir la carpeta del proyecto en VS Code: `File > Open Folder`
2. Abrir cualquier archivo `.ipynb` desde el explorador de archivos
3. Seleccionar el kernel `.venv` en la esquina superior derecha del notebook
4. Ejecutar celdas con `Shift+Enter`

Para una guía detallada sobre el uso de Jupyter en VS Code, ver [docs/jupiter.md](docs/jupiter.md).

---

## Ejecutar scripts Python

```bash
uv run python main.py
uv run python modulo01/ejercicio2.py
```

---

## Estructura del proyecto

```text
aed/
├── content/           # Notebooks y archivos de ejercicios
│   └── ejercicio_01.ipynb
├── modulo01/          # Scripts del módulo 1
│   ├── holamundo.py
│   └── ejercicio2.py
├── docs/              # Documentación
│   └── jupiter.md     # Guía de uso de Jupyter en VS Code
├── main.py
├── pyproject.toml     # Configuración del proyecto y dependencias
└── uv.lock
```

---

## Agregar nuevas dependencias

```bash
uv add nombre-paquete
```

Esto actualiza `pyproject.toml` y `uv.lock` automáticamente.
