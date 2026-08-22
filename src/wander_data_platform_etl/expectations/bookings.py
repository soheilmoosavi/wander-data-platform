BOOKING_EXPECTATIONS = {
    "booking_id_not_null": "booking_id IS NOT NULL",
    "user_id_not_null": "user_id IS NOT NULL",
    "property_id_not_null": "property_id IS NOT NULL",
    "check_in_not_null": "check_in IS NOT NULL",
    "check_out_not_null": "check_out IS NOT NULL",
    "valid_booking_dates": "check_out >= check_in",
    "positive_guest_count": "guests_count > 0",
    "non_negative_total_amount": "total_amount >= 0",
    "valid_status": (
        "status IN ('pending', 'confirmed', 'cancelled', 'completed')"
    ),
}