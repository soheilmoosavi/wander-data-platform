from pyspark import pipelines as dp


SOURCE_TABLE = (
    "databricks_wanderbricks_dataset_dais_2025"
    ".wanderbricks.bookings"
)


@dp.table(
    name="bronze_bookings",
    comment="Raw booking records ingested from the Wanderbricks source dataset.",
)
def bronze_bookings():
    return spark.read.table(SOURCE_TABLE)