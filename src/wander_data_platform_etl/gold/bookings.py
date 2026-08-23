from pyspark import pipelines as dp
from pyspark.sql import functions as F

@dp.table(

    name="gold_booking_daily",
    comment="Daily booking and revenue metrics derived from validated Silver bookings.",

)
def gold_booking_daily():
    return (
        spark.read.table("silver_bookings")
        .groupBy("check_in")
        .agg(
            F.count("*").alias("total_bookings"),
            F.sum(F.when(F.col("status") == "confirmed", 1).otherwise(0)).alias(
                "confirmed_bookings"
            ),
            F.sum(F.when(F.col("status") == "completed", 1).otherwise(0)).alias(
                "completed_bookings"
            ),
            F.sum(F.when(F.col("status") == "cancelled", 1).otherwise(0)).alias(
                "cancelled_bookings"
            ),
            F.sum(F.when(F.col("status") == "pending", 1).otherwise(0)).alias(
                "pending_bookings"
            ),
            F.sum("total_amount").alias("total_revenue"),
            F.avg("total_amount").alias("average_booking_value"),
            F.avg("guests_count").alias("average_guests"),
        )
        .withColumnRenamed("check_in", "booking_date")
    )