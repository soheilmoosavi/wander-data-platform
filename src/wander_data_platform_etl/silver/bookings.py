from pyspark import pipelines as dp

from expectations.bookings import BOOKING_EXPECTATIONS


@dp.table(
    name="silver_bookings",
    comment="Validated booking records from bronze_bookings.",
)
@dp.expect_all_or_drop(BOOKING_EXPECTATIONS)
def silver_bookings():
    return spark.read.table("bronze_bookings")
