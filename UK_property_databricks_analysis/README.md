# 🏠 UAM MABA - Databricks Labs

Proyectos de análisis de datos con Databricks para el MABA (Master in Business Analytics) - UAM

## 📚 Proyecto

### UK Property Price Analysis
Análisis de transacciones inmobiliarias del Reino Unido con arquitectura Medallion (Bronze-Silver-Gold).

**Estructura de Notebooks:**
- `01_data_ingestion_exploration.ipynb`: Carga inicial y exploración de datos, EDA básico desde la tabla raw.
- `02_data_cleaning_transformation.ipynb`: Procesamiento, limpieza y transformación de datos. Genera las capas Bronze y Silver.
- `03_transformations.ipynb`: Generación de todas las tablas Gold, incluyendo análisis por ciudad, tendencias temporales, tipo de propiedad, distritos y categorías de precio.
- `04_sql_analysis.ipynb`: Análisis SQL y visualización sobre las tablas Gold, con consultas avanzadas y segmentación.
- `05_dashboard_summary.ipynb`: Resúmenes visuales y dashboards, enfocados en ciudades, tipos de propiedad y distritos usando las tablas Gold.

**Dataset:** HM Land Registry Price Paid Data, 2024-2025 (+1,500,000 transacciones)

---

## 🚦 Preparación y ejecución

### 1. Inicializa el entorno

Ejecuta primero el script `workspace_structure` para crear el esquema y los volúmenes Unity Catalog necesarios.

### 2. Descarga los archivos fuente (Yearly file)

1. Ve a: https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads
2. Descarga los archivos "Yearly file" para 2025 y 2024 (y opcionalmente 2023 para verificar funcionamiento del Auto Loader).
3. Sube los archivos al entorno Databricks a `workspace/uk_housing/ingestion`   

### 3. Configura la ingesta automática

Ejecuta el notebook o script `auto_loader_config` para habilitar la ingesta incremental y cargar los ficheros al volumen.

### 4. Ejecuta los notebooks de análisis

1. Abre y ejecuta `01_data_ingestion_exploration.ipynb` para explorar y transformar los datos hasta la capa Bronze.
2. Continúa con `02_data_cleaning_transformation.ipynb` para crear Silver y Gold.
3. Utiliza `03_transformations.ipynb` para crear las tablas Gold.
4. Realiza análisis SQL con `04_sql_analysis.ipynb`.
5. Presenta visualizaciones y dashboards con `05_dashboard_summary.ipynb`.

---

## 📊 Arquitectura y tablas

El pipeline de datos sigue el patrón Medallion. Tras cargar los archivos, los datos estarán en el volumen y luego en la tabla `[workspace.uk_housing.price_paid](#table)`. El proceso genera:

- Bronze: `[workspace.uk_housing.bronze_property_sales](#table)`
- Silver: `workspace.uk_housing.silver_property_sales`
- Gold:
  - `[workspace.uk_housing.gold_city_prices](#table)` (análisis por ciudad)
  - `[workspace.uk_housing.gold_temporal_trends](#table)` (tendencias y evolución temporal)
  - `[workspace.uk_housing.gold_property_analysis](#table)` (análisis por tipo de propiedad y ciudad)
  - `[workspace.uk_housing.gold_district_analysis](#table)` (análisis geográfico por distrito y evolución)
  - `[workspace.uk_housing.gold_price_category_analysis](#table)` (análisis por categorías de precio)

```
Yearly raw CSVs
   ↓
🥉 Bronze Layer
   └─ bronze_property_sales (tabla Delta raw)
   ↓
🥈 Silver Layer
   └─ silver_property_sales (datos limpios + enriquecidos)
   ↓
🥇 Gold Layer
   ├─ gold_city_prices
   ├─ gold_temporal_trends
   ├─ gold_property_analysis
   ├─ gold_district_analysis
   └─ gold_price_category_analysis
```

---

## 🔧 Tecnologías

- **Databricks ** - Plataforma de análisis y procesamiento
- **Apache Spark (PySpark)** - Motor de procesamiento distribuido
- **Delta Lake** - Almacenamiento transaccional para data lakes
- **SQL** - Consultas y análisis de datos
- **Unity Catalog** - Gobierno y gestión de datos
- **Auto Loader** - Ingesta incremental de archivos
- **Visualización Databricks** - Herramientas de visualización en notebooks y dashboarda


---

## 📝 Notas Importantes

- Los datos no se incluyen en el repositorio por tamaño. Descárgalos de la fuente oficial.
- Outputs pueden estar deshabilitados: ejecuta los notebooks para visualizar resultados en Databricks.

---

## 👥 Autores

**Dubraska Veroes**
**Teresa Duato**    
**Darío Ruiz**  
Master in Business Analytics (MABA) - UAM  
Fecha: Marzo 2026

---

## 📚 Referencias

- [HM Land Registry - Price Paid Data](https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads)
- [Databricks Documentation](https://docs.databricks.com/)
- [Delta Lake](https://delta.io/)
