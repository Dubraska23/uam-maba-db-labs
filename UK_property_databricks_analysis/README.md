# 🏠 UAM MABA - Databricks Labs

Proyectos de análisis de datos con Databricks para el MABA (Master in Business Analytics) - UAM

## 📚 Proyectos Incluidos

### 1. UK Property Price Analysis
Análisis de transacciones inmobiliarias del Reino Unido con arquitectura Medallion (Bronze-Silver-Gold).

**Notebooks:**
- `01_data_ingestion_exploration.ipynb` - Carga y exploración de datos
- `02_data_cleaning_transformation.ipynb` - Transformación Bronze → Silver → Gold

**Dataset:** HM Land Registry Price Paid Data (~105,000 transacciones)

---

## 📊 Cómo obtener los datos

### UK Property Dataset

**Descargar desde el navegador:**
1. Ve a: https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads
2. Descarga: "current month as a CSV file" (17.9 MB)
3. Renombra a: `price_paid_data.csv`

### Subir a Databricks:

1. En Databricks: **Data** → **Create or modify table**
2. Arrastra el archivo CSV
3. Configuración:
   - **Table name:** `price_paid_data`
   - **First row is header:** NO ❌
4. Click **"Create Table"**

---

## 🚀 Cómo ejecutar los notebooks

### Desde Databricks:

**Opción 1: Clonar el repositorio completo**
1. En Databricks, ve a **Repos** (menú izquierdo)
2. Click **"Add Repo"**
3. Pega la URL: `https://github.com/Dubraska23/uam-maba-db-labs`
4. Click **"Create Repo"**

**Opción 2: Importar notebooks individuales**
1. En Databricks Workspace, click **Import**
2. Selecciona **URL**
3. https://github.com/Dubraska23/uam-maba-db-labs/new/main/UK_property_databricks_analysis
4. Click **Import**

### Ejecutar en orden:
1. ✅ `01_data_ingestion_exploration.ipynb`
2. ✅ `02_data_cleaning_transformation.ipynb`
3. 🔜 `03_analysis_visualization.sql` (próximamente)

---

## 🏗️ Arquitectura
```
CSV Raw Data (105K registros)
    ↓
🥉 Bronze Layer
   └─ price_paid_data (tabla raw)
    ↓
🥈 Silver Layer
   └─ silver_property_sales (datos limpios + enriquecidos)
    ↓
🥇 Gold Layer
   ├─ gold_city_prices (análisis por ciudad)
   ├─ gold_temporal_trends (evolución temporal)
   └─ gold_property_analysis (análisis por tipo de propiedad)
```

---

## 🔧 Tecnologías

- **Databricks Community Edition**
- **Apache Spark (PySpark)**
- **Delta Lake**
- **SQL**
- **Unity Catalog**

---

## 📝 Notas Importantes

⚠️ **Los datos NO están incluidos en este repositorio** por su tamaño (>17 MB).  
👉 Descárgalos siguiendo las instrucciones de arriba.

⚠️ Los notebooks pueden mostrar outputs deshabilitados por el administrador de workspace.  
👉 Ejecútalos en tu propio Databricks para ver los resultados.

---

## 👥 Autor

**Dubraska**  
Master in Business Analytics (MABA) - UAM  
Fecha: Marzo 2026

---

## 📧 Contacto

Para colaborar o hacer preguntas sobre el proyecto, contacta a través de GitHub Issues.

---

## 📚 Referencias

- [HM Land Registry - Price Paid Data](https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads)
- [Databricks Documentation](https://docs.databricks.com/)
- [Delta Lake](https://delta.io/)
```

4. Click **"Commit new file"** (abajo)
