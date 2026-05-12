# 📊 Proyecto 4 - Automatización sakila → Python → Excel
## Sistema de Automatización y Análisis de Datos con Python, SQL y Excel

Proyecto de automatización de datos orientado al análisis, transformación y visualización de información mediante procesos ETL desarrollados en Python.
El sistema conecta con una base de datos relacional, ejecuta consultas SQL, procesa los datos con Pandas y genera archivos CSV preparados para su análisis en Excel mediante dashboards y tablas dinámicas.

✨ Arquitectura ETL ligera · Automatización con Python · Visualización en Excel

---

## 👥 Autores - Grupo 3
* **Rita Isabel Romero Ruiz**
* **Marco Ohimai Imouokhome**
* **Irene Condado Alcantarilla**

---

# 📖 Documentación
README.md (este archivo) - Guía completa del proyecto
Dashboard/README.md - Guía completa del Dashboard

---
# 🚀 Puesta en Marcha

## 1. Clonar el repositorio
```bash
git clone https://github.com/Bootcamp-DA-P2/automatizaci-n-mysql-python-excel_grupo3.git
```
Acceder a la carpeta del proyecto:
```cd automatizaci-n-mysql-python-excel_grupo3```

## 2. Instalar dependencias
```bash
# Instalar dependencias
pip install -r requirements.txt

# Configurar base de datos
# Edita el archivo .env con tus credenciales

# Ejecutar
python main.py
```

---

# 📁 Estructura del Proyecto

```txt
automatizaci-n-mysql-python-excel_grupo3/
│
├── main.py                    ⭐ EJECUTAR ESTE
│
├── src/                       📦 Código fuente
│   ├── __init__.py
│   ├── sakila_ETL.py          (extracción y transformación)
│   └── config.py              (configuración desde .env)
│
├── output/                    📂 Datos procesados
│   ├── DataFrame1.csv
│   ├── DataFrame2.csv
│   └── DataFrame3.csv
│
├── assets/   
│
├── dashboard/                 📊 Visualización
│   ├── Sakila_dashboard.xlsx
│   └── README.md
│
├── queries/                   🗄️ Consultas SQL
│   ├── DataFrame1.sql
│   ├── DataFrame2.sql
│   └── DataFrame3.sql
│
├── requirements.txt
├── .env                       🔒 Credenciales
├── .env.example
├── .gitignore
└── README.md
```

---

# ⚙️ CONFIGURACIÓN

## 1. Instalar Python y Base de Datos

### Requisitos:
    - Python 3.8 o superior

    - [MYSQL / POSTGRESQL / SQL SERVER]

    - Excel o Excel Online

## 2. Instalar dependencias
```bash
pip install -r requirements.txt
```
Ejemplo:
```bash
pip install pandas sqlalchemy openpyxl python-dotenv
```

## 3. Configurar conexión (.env)

Crea un archivo .env basado en .env.example con tus credenciales de acceso:
```
DB_USER=usuario
DB_PASSWORD=contraseña
DB_HOST=localhost
DB_PORT=3306
DB_NAME=sakila

```

---
# 🎯 USO

Ejecutar el proceso completo:

```bash
python main.py
```

Esto hará:

* ✅ Extrae datos desde la base de datos
* ✅ Transforma y analiza datos con Pandas
* ✅ Genera archivos CSV automáticamente
* ✅ Actualiza la información del dashboard

---

# 📂 Archivos generados

| Archivo       | Descripción                |
| ------------- | -------------------------- |
| DataFrame1.csv | [Descripción del análisis] |
| DataFrame2.csv | [Descripción del análisis] |
| DataFrame3.csv | [Descripción del análisis] |

---

# 📊 Dashboard y Análisis Final
El análisis final se centraliza en el archivo Sakila_dashboard.xlsx. Para comprender el funcionamiento de los filtros, segmentadores y métricas visualizadas, consulta la Guía del Dashboard[dashboard\README.md].
