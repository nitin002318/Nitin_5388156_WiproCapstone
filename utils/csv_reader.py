import csv

def get_test_data():

    with open(
        "test_data/men_test_data.csv",
        newline=""
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            return row