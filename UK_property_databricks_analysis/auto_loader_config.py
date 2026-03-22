# Configuración de Auto Loader para cargar archivos CSV desde un volumen
from pyspark.sql import SparkSession

# Rutas
volume_path = "/Volumes/workspace/uk_housing/ingestion"
target_table = "workspace.uk_housing.price_paid"
checkpoint_location = "/Volumes/workspace/uk_housing/checkpoints/price_paid"

# Nombres de las columnas
column_names = [
    "transaction_id", "price", "date_of_transfer", "postcode",
    "property_type", "old_new", "duration", "paon", "saon",
    "street", "locality", "town_city", "district", "county",
    "ppd_category_type", "record_status", "metadata"
]

# Configurar Auto Loader con inferencia de esquema
df = (spark.readStream
    .format("cloudFiles")
    .option("cloudFiles.format", "csv")
    .option("cloudFiles.schemaLocation", checkpoint_location + "/schema")
    .option("header", "false")
    .option("delimiter", ",")  # Carácter de separación (coma)
    .option("escape", "\"")  # Carácter de escape (comillas dobles)
    .option("quote", "\"")  # Carácter de comillas
    .option("cloudFiles.inferColumnTypes", "true")  # Infiere tipos de datos
    .load(volume_path))

# Verificar número de columnas antes de renombrar
print(f"Número de columnas leídas: {len(df.columns)}")
print(f"Número de nombres a asignar: {len(column_names)}")

# Renombrar columnas con los nombres personalizados (selecciona solo las primeras 16 columnas de datos)
df_renamed = df.toDF(*column_names)

# Escribir a la tabla destino
query = (df_renamed.writeStream
    .option("checkpointLocation", checkpoint_location)
    .trigger(availableNow=True)  # Procesa todos los archivos disponibles y se detiene
    .toTable(target_table))

# Esperar a que termine el procesamiento
query.awaitTermination()

print(f"✓ Auto Loader configurado correctamente")
print(f"✓ Tabla creada: {target_table}")
print(f"✓ Archivos cargados desde: {volume_path}")