import csv


def read_file(filename):
    rows = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rows.append(row)
    return rows
# source https://docs.python.org/3/library/csv.html


file_name = '/Users/mac/penguins.csv'
# print(read_file(file_name))
