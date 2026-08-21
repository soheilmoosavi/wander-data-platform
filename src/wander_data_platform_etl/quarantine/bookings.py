from pyspark import pipelines as dp
from pyspark.sql.functions import col, lit, current_timestamp


@dp.table(
    name="quarantine_bookings",
    comment="Booking records rejected from Silver due to data-quality violations.",
)
def quarantine_bookings():
    return (
        spark.read.table("bronze_bookings")
        .filter(col("total_amount") < 0)
        .withColumn(
            "rejection_reason",
            lit("NEGATIVE_TOTAL_AMOUNT"),
        )
        .withColumn(
            "_rejected_at",
            current_timestamp(),
        )
    )