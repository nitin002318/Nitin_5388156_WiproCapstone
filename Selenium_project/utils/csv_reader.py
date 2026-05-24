import csv
import os


def get_test_data():

    data = []

    current_dir = os.path.dirname(__file__)

    file_path = os.path.join(
        current_dir,
        "..",
        "test_data",
        "men_test_data.csv"
    )

    file_path = os.path.abspath(file_path)

    with open(file_path, newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            data.append(
                (
                    row["size"],
                    row["donation"]
                )
            )

    return data