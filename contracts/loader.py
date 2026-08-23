from pathlib import Path

import yaml

CONTRACT_PATH = Path(__file__).with_name("bookings.yml")

def load_booking_contract() -> dict:

    with CONTRACT_PATH.open() as file:

        return yaml.safe_load(file)

def build_booking_expectations() -> dict[str, str]:

    contract = load_booking_contract()

    expectations = {

        f"{column}_not_null": f"{column} IS NOT NULL"

        for column, definition in contract["columns"].items()

        if not definition.get("nullable", True)

    }

    for column, definition in contract["columns"].items():

        for constraint in definition.get("constraints", []):

            if constraint == f"{column} > 0":

                name = f"{column}_positive"

            elif constraint == f"{column} >= 0":

                name = f"{column}_non_negative"

            else:

                name = f"{column}_constraint"

            expectations[name] = constraint

    status_values = contract["columns"]["status"].get("allowed_values")

    if status_values:

        values = ", ".join(f"'{value}'" for value in status_values)

        expectations["valid_status"] = f"status IN ({values})"

    expectations["valid_booking_dates"] = "check_out >= check_in"

    return expectations