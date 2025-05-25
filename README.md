# Deserción Escolar - Conversión CSV a SQLite

Este proyecto convierte un archivo CSV con datos de deserción escolar en una base de datos SQLite lista para su análisis. Está preparado para funcionar localmente o integrarse con GitHub Actions para generar automáticamente el archivo `.db` al hacer cambios en el repositorio.

## Estructura del proyecto

```

bd/
├── static/
│   └── desersion\_escolar.csv       # Archivo fuente de datos
│   └── desersion\_escolar.db        # Archivo generado automáticamente
├── src/
│   └── convertir\_csv\_sqlite.py     # Script principal de conversión
├── .github/
│   └── workflows/
│       └── build\_sqlite.yml        # GitHub Actions para automatizar la conversión
├── setup.py                        # Configuración del paquete
└── README.md                       # Este archivo

````

## Requisitos

- Python 3.9 o superior
- pip
- (opcional) entorno virtual recomendado

## Instalación local

1. Clona el repositorio:

```bash
git clone https://github.com/ibarguen1018/BIGDATA-2025-1-2.git
````

2. Crea y activa un entorno virtual:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

3. Instala el proyecto en modo editable:

```bash
pip install -e .
```

## Uso

Una vez instalado, ejecuta el comando:

```bash
convertir-csv-sqlite
```

Esto leerá el archivo `static/desersion_escolar.csv` y generará `static/desersion_escolar.db`.

## Automatización con GitHub Actions

Este proyecto incluye un flujo de trabajo (`.github/workflows/build_sqlite.yml`) que:

* Se ejecuta automáticamente cuando cambias el CSV o el script.
* Genera el archivo `.db`.
* Lo sube como artefacto al historial de ejecuciones.

Puedes ejecutar el workflow manualmente desde la pestaña **Actions** en GitHub.
