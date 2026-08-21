from pyspark import pipelines as dp
from pyspark.sql.functions import col


@dp.table(
    name="silver_bookings",
    comment="Validated booking records from bronze_bookings.",
)
def silver_bookings():
    return (
        spark.read.table("bronze_bookings")
        .filter(col("booking_id").isNotNull())
        .filter(col("user_id").isNotNull())
        .filter(col("property_id").isNotNull())
        .filter(col("check_out") >= col("check_in"))
        .filter(col("guests_count") > 0)
        .filter(col("total_amount") >= 0)
    )