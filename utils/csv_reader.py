import csv
import os


def get_test_data():

    file_path = os.path.join(
        os.getcwd(),
        "test_data",
        "men_test_data.csv"
    )

    data_list = []

    with open(file_path, newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            data_list.append(
                (
                    row["size"],
                    row["donation"]
                )
            )

    return data_list