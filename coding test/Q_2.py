# Use matplotlib to visualize bill length vs bill depth.
# Use color to distinguish species.
# Read the data using the return value of the function you wrote in Question  # 1
# Add column labels and a color legend
import matplotlib
import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator


def read_file(filename):
    rows = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rows.append(row)
    return rows


file_name = '/Users/mac/penguins.csv'


def q2_plot(column1, column2, filename):

    rows = read_file(filename)
    bill_lengths = []
    bill_depths = []
    for i in rows:
        bill_lengths.append(i.get(column1))
        bill_depths.append(i.get(column2))
    # print(bill_depths)
    # print(rows[1].get("bill_length_mm"))
    size = len(rows)
    x = np.arange(size)
    total_width, n = 0.8, 2
    width = total_width / n
    y_major_locator = MultipleLocator(10)
    ax = plt.gca()
    ax.yaxis.set_major_locator(y_major_locator)
    plt.bar(x, bill_lengths,  width=width, label=column1)
    plt.bar(x + width, bill_depths, width=width, label=column2)
    plt.legend()
    plt.show()


# test case 1
q2_plot("bill_length_mm", "bill_depth_mm", file_name)
