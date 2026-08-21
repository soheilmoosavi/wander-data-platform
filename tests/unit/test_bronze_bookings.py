from pyspark.sql import SparkSession


def test_bronze_bookings_preserves_source_records():
    spark = (
        SparkSession.builder
        .master("local[2]")
        .appName("wander-data-platform-tests")
        .getOrCreate()
    )

    data = [
        (1, 101, 1001, 2, -50.0, "pending"),
        (2, 102, 1002, 1, 250.0, "confirmed"),
    ]

    columns = [
        "booking_id",
        "user_id",
        "property_id",
        "guests_count",
        "total_amount",
        "status",
    ]

    df = spark.createDataFrame(data, columns)

    # Bronze must preserve the source records.
    # Data-quality filtering belongs in Silver.
    assert df.count() == 2
    assert df.filter(df.total_amount < 0).count() == 1

    spark.stop()